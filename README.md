# Tanveer Associates AI Assistant

A LangGraph agent that answers real estate questions from a RAG knowledge
base, captures and qualifies leads using Tanveer Associates' own sales
playbook, and hands off to a human when needed -- reachable from
WhatsApp, Facebook Messenger, and an embeddable web chat widget.

Built on **PostgreSQL** for both conversation memory and the leads/CRM
store (no SQLite anywhere in this version).

## How it's organized

| Folder                  | What lives here                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `conversation_layer/` | The LangGraph brain: state schema, the 3 tools (RAG search, lead capture, handoff), system prompt, and the graph itself (`agent` node ⟷ `tools` node loop)     |
| `webhook/`            | One file per channel:`whatsapp_webhook.py`, `messenger_webhook.py`, `web_chat_webhook.py`, plus `message_sender.py` for outbound replies                    |
| `knowledge_base/`     | `company_data.py` (Tanveer Associates' projects, pricing plans, and the lead-qualification playbook), `vector_store.py` (Chroma), `retriever.py` (RAG search) |
| `memory/`             | `short_term_memory.py` (LangGraph's **PostgreSQL** checkpointer) and `long_term_memory.py` (leads/CRM table in **PostgreSQL**)                      |
| `lead_intelligence/`  | `lead_scoring.py` (the platform-aware stage classifier), `lead_schema.py` (Lead model)                                                                          |
| `schema/`             | Pydantic request/response models for the HTTP API                                                                                                                   |
| `jobs/`               | `rebuild_knowledge_base_job.py` -- CLI to reindex after editing company data                                                                                      |
| `reporting/`          | `leads_report.py` -- export captured leads to CSV                                                                                                                 |
| `app/`                | `main.py` (FastAPI app + routes), `settings.py` (all env vars in one place)                                                                                     |
| `frontend/`           | The embeddable web chat widget                                                                                                                                      |
| `data/`               | Runtime storage for the Chroma vector DB only (leads and conversation memory now live in Postgres)                                                                  |

## The lead-qualification flow

This is the part that's specific to Tanveer Associates, and it's driven
directly by the **"Lead Qualification Questions"** category inside
`knowledge_base/company_data.py` -- that section is the actual sales
playbook, and `lead_intelligence/lead_scoring.py` encodes its exact
stage rules so the two never drift apart:

1. Answer the property question first (RAG).
2. Ask property type, city/area, budget range, and financing method.
3. Contact info required differs **by platform** (`lead_scoring.py:REQUIRED_CONTACT_FIELDS`):
   - WhatsApp: name only (phone is auto-filled from the sender's number)
   - Messenger: name + phone
   - Web chat: name + phone (email optional)
4. Once budget + contact are complete, ask for a call time and offer a site visit.

Stages (exact labels from the knowledge base):

| Stage                                      | Meaning                                                         |
| ------------------------------------------ | --------------------------------------------------------------- |
| `new`                                    | Conversation just started                                       |
| `not_interested`                         | Property interest expressed, but budget/financing still unknown |
| `ready_for_call_missing_contact_details` | Budget confirmed, but required contact info missing             |
| `qualified_missing_call_time`            | Budget + contact complete, no call time yet                     |
| `qualified_ready_for_call`               | Budget + contact + call time all set                            |

## The "intelligent" lead capture tool

`conversation_layer/tools.py`'s `save_lead_info` does more than just
save fields:

- **Auto-fills the phone number on WhatsApp** from the sender's `user_id`
  (the WhatsApp number *is* the identifier), so the model never has to
  ask for it on that channel.
- **Validates email and phone format** before saving -- an obviously
  malformed value (e.g. `"not-an-email"`) is rejected and the model is
  told so, instead of a bad value silently landing in the CRM.
- **Merges, never overwrites** -- calling it again with only a new field
  keeps everything already known.
- **Reports exactly what's still missing** in its return message (e.g.
  `"Still missing: budget_range, preferred_call_time"`), so the system
  prompt's "only ask for what's missing" instruction actually has
  something concrete to work from, instead of the model guessing.

## PostgreSQL setup

```bash
createdb tanveer_associates
```

Both memory layers share one `DATABASE_URL` (`app/settings.py`):

- `memory/short_term_memory.py` uses LangGraph's `PostgresSaver` -- it
  calls `.setup()` on first run to create its own checkpoint tables.
- `memory/long_term_memory.py` creates a single `leads` table itself on
  first use (see the `_SCHEMA` constant in that file).

No manual migrations needed -- both create their tables automatically
the first time the app runs against an empty database.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# then edit .env: OPENAI_API_KEY and DATABASE_URL are both required.

createdb tanveer_associates   # or whatever DB name you put in DATABASE_URL
```

Build the knowledge base once before your first run:

```bash
python -m jobs.rebuild_knowledge_base_job
```

Run the server:

```bash
python run_server.py
# or: uvicorn app.main:app --reload
```

- Web chat widget: `http://localhost:8000/widget`
- Health check: `http://localhost:8000/`
- Leads (JSON): `http://localhost:8000/admin/leads`
- Leads (CSV): `python -m reporting.leads_report [stage]`
- Reindex knowledge base: `POST http://localhost:8000/admin/reindex`

## Connecting WhatsApp and Messenger

Both use the same Meta Graph API and the same `VERIFY_TOKEN` from `.env`.

1. Expose your local server publicly for testing (e.g. `ngrok http 8000`).
2. In Meta's App Dashboard, set the webhook callback URL to:
   - WhatsApp: `https://<your-domain>/webhook/whatsapp`
   - Messenger: `https://<your-domain>/webhook/messenger`
3. Use the same `VERIFY_TOKEN` value you put in `.env`.
4. Fill in `WHATSAPP_TOKEN`, `WHATSAPP_PHONE_NUMBER_ID`, and
   `PAGE_ACCESS_TOKEN` in `.env`, then restart the server.

## Editing company knowledge

Add or edit entries in `knowledge_base/company_data.py` (grouped by
category -- including the lead qualification playbook itself), then run
`python -m jobs.rebuild_knowledge_base_job` (or hit `POST /admin/reindex`
on a running server) to re-embed everything.

## Tuning lead scoring

Weights, required-contact-fields-per-platform, and stage thresholds all
live in `lead_intelligence/lead_scoring.py` -- plain rule-based logic (no
extra LLM call), so it's fast, free, and easy to tune as you learn what
a real qualified Tanveer Associates lead looks like.

## Human handoff

When the agent calls `escalate_to_human`, the conversation is flagged in
the leads table (`handoff_requested`, `handoff_reason`). Wire up a real
notification (Slack, email) by posting to `HANDOFF_NOTIFY_WEBHOOK_URL`
from `conversation_layer/tools.py`'s `escalate_to_human` -- left as a
TODO since it depends on where your team wants alerts.

## What changed from the previous (GoForeign) version

- Swapped the knowledge base to Tanveer Associates' real content (309
  facts across projects, pricing, team, FAQs, and the lead-qualification
  playbook).
- Replaced generic "capture name/phone/email/interest" lead fields with
  real estate-specific ones: `property_type`, `city_or_area`,
  `budget_range`, `financing_method`, `purchase_timeline`,
  `preferred_call_time`, `site_visit_requested`.
- Replaced the generic point-based lead scorer with an exact
  state-machine classifier matching the 5 stage labels defined in the
  company's own knowledge base.
- Made `save_lead_info` platform-aware (different required contact
  fields per channel) and added input validation + "what's still
  missing" feedback -- the "more intelligent" part of this update.
- Migrated both memory layers from SQLite to **PostgreSQL**
  (`langgraph-checkpoint-postgres` for conversation memory, raw
  `psycopg`/`psycopg_pool` with `ON CONFLICT` upserts for the leads table).
