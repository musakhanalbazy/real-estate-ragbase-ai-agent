"""Conversation memory: human-readable message log in PostgreSQL.

Stores every user ↔ assistant message as plain text in a dedicated
`conversations` table, completely separate from LangGraph's opaque
checkpoint blobs.  This gives you:

  • A clear audit trail you can SELECT and read directly in pgAdmin/psql.
  • A configurable history window so only the last N messages are sent
    to OpenAI on each turn, keeping API token usage predictable.
"""

import os
from datetime import datetime, timezone
from typing import Optional

from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:687254@localhost:5432/tanveer_associates"
)

_SCHEMA = """
CREATE TABLE IF NOT EXISTS conversations (
    id                SERIAL       PRIMARY KEY,
    session_id        TEXT         NOT NULL,
    platform          TEXT         NOT NULL,
    role              TEXT         NOT NULL,
    message           TEXT         NOT NULL,
    token_count       INTEGER      NOT NULL DEFAULT 0,
    created_at        TIMESTAMPTZ  NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_conv_session  ON conversations (session_id);
CREATE INDEX IF NOT EXISTS idx_conv_created  ON conversations (created_at);
CREATE INDEX IF NOT EXISTS idx_conv_platform ON conversations (platform);
"""

# ---------- connection pool (shared with long_term_memory) ----------
_pool: Optional[ConnectionPool] = None


def _get_pool() -> ConnectionPool:
    global _pool
    if _pool is None:
        _pool = ConnectionPool(DATABASE_URL, min_size=1, max_size=10, open=True)
        with _pool.connection() as conn:
            conn.execute(_SCHEMA)
            conn.commit()
    return _pool


# ---------- token estimation ----------
def estimate_tokens(text: str) -> int:
    """Rough token count: ~4 chars per token for English text.

    Good enough for budgeting; avoids importing tiktoken (heavy dependency).
    """
    return max(1, len(text) // 4)


# ---------- write ----------
def save_message(
    session_id: str,
    platform: str,
    role: str,
    message: str,
) -> dict:
    """Insert one message row. Returns the saved record as a dict."""
    now = datetime.now(timezone.utc)
    tokens = estimate_tokens(message)
    pool = _get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """
                INSERT INTO conversations
                    (session_id, platform, role, message, token_count, created_at)
                VALUES
                    (%s, %s, %s, %s, %s, %s)
                RETURNING *
                """,
                (session_id, platform, role, message, tokens, now),
            )
            row = cur.fetchone()
        conn.commit()
    return dict(row)


# ---------- read (capped — for feeding back to the LLM) ----------
MAX_HISTORY_MESSAGES = int(os.getenv("MAX_HISTORY_MESSAGES", "10"))


def get_recent_messages(session_id: str, limit: int = MAX_HISTORY_MESSAGES) -> list[dict]:
    """Return the last *limit* messages for this session, oldest-first.

    This is what gets appended to the LLM context on each turn.
    Keeping 'limit' small (default 10 = 5 user+assistant pairs)
    directly reduces OpenAI token spend.
    """
    pool = _get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """
                SELECT role, message, created_at
                FROM conversations
                WHERE session_id = %s
                ORDER BY created_at DESC
                LIMIT %s
                """,
                (session_id, limit),
            )
            rows = [dict(r) for r in cur.fetchall()]
    # Reverse so they're in chronological order for the LLM
    rows.reverse()
    return rows


# ---------- read (full — for admin / reporting) ----------
def get_full_conversation(session_id: str) -> list[dict]:
    """Return every message for a session. Used by /admin/conversations."""
    pool = _get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                """
                SELECT id, session_id, platform, role, message,
                       token_count, created_at
                FROM conversations
                WHERE session_id = %s
                ORDER BY created_at ASC
                """,
                (session_id,),
            )
            return [dict(r) for r in cur.fetchall()]


def list_conversations(platform: Optional[str] = None) -> list[dict]:
    """Return a summary of all conversation sessions for admin listing."""
    pool = _get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            if platform:
                cur.execute(
                    """
                    SELECT session_id, platform,
                           COUNT(*)            AS message_count,
                           SUM(token_count)    AS total_tokens,
                           MIN(created_at)     AS started_at,
                           MAX(created_at)     AS last_message_at
                    FROM conversations
                    WHERE platform = %s
                    GROUP BY session_id, platform
                    ORDER BY MAX(created_at) DESC
                    """,
                    (platform,),
                )
            else:
                cur.execute(
                    """
                    SELECT session_id, platform,
                           COUNT(*)            AS message_count,
                           SUM(token_count)    AS total_tokens,
                           MIN(created_at)     AS started_at,
                           MAX(created_at)     AS last_message_at
                    FROM conversations
                    GROUP BY session_id, platform
                    ORDER BY MAX(created_at) DESC
                    """
                )
            return [dict(r) for r in cur.fetchall()]
