"""Streamlit local chat UI for Tanveer Associates AI Assistant.

Talks to the FastAPI /chat endpoint — make sure run_server.py is running.
Messages are saved to the existing conversations & leads tables automatically.
"""

import os
import uuid
import streamlit as st
import httpx

FASTAPI_BASE_URL = os.getenv("FASTAPI_BASE_URL", "http://localhost:8000")

st.set_page_config(page_title="Tanveer Associates AI Assistant", layout="centered")
st.title("🏠 Tanveer Associates AI Assistant")
st.caption("Local chat UI — make sure run_server.py is running first.")


# ---------- session helpers ----------
def new_session_id():
    return str(uuid.uuid4())


if "session_id" not in st.session_state:
    st.session_state.session_id = new_session_id()
if "messages" not in st.session_state:
    st.session_state.messages = []


def reset_chat():
    st.session_state.messages = []
    st.session_state.session_id = new_session_id()
    st.rerun()


# ---------- API call with full error handling ----------
def send_message(text, session_id):
    """Call /chat endpoint. Returns (reply, session_id) or (error_msg, session_id)."""
    try:
        resp = httpx.post(
            f"{FASTAPI_BASE_URL}/chat",
            json={"message": text, "session_id": session_id},
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("answer", "(empty reply)"), data.get("session_id", session_id)

    except httpx.ConnectError:
        return "❌ **Connection failed.** Is `run_server.py` running on " + FASTAPI_BASE_URL + "?", session_id
    except httpx.TimeoutException:
        return "⏳ **Request timed out.** The server took too long to respond.", session_id
    except httpx.HTTPStatusError as e:
        return f"⚠️ **Server error {e.response.status_code}:** {e.response.text[:200]}", session_id
    except Exception as e:
        return f"❌ **Unexpected error:** {e}", session_id


# ---------- sidebar ----------
with st.sidebar:
    st.subheader("Session")
    sid = st.text_input("Session ID", value=st.session_state.session_id, key="sid_input")
    if sid.strip():
        st.session_state.session_id = sid.strip()
    if st.button("🔄 Reset chat"):
        reset_chat()
    st.code(st.session_state.session_id, language=None)

    st.divider()
    st.caption(
        "Same session IDs as web widget, WhatsApp & Messenger. "
        "All messages saved to conversations & leads tables."
    )

# ---------- chat history ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- chat input ----------
prompt = st.chat_input("Type a message")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply, new_sid = send_message(prompt, st.session_state.session_id)
            st.session_state.session_id = new_sid
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
