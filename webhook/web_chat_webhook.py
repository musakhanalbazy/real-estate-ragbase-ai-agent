"""HTTP endpoint backing the embeddable web chat widget (frontend/index.html).

Not a Meta webhook -- just a plain JSON API. Kept in this package anyway
since it's the third "channel" alongside WhatsApp and Messenger, and goes
through the exact same run_turn()/graph/memory/RAG pipeline.
"""

import logging
import uuid

from fastapi import APIRouter

from conversation_layer.graph import run_turn
from schema.api_schema import ChatRequest, ChatResponse

logger = logging.getLogger("tanveer.web_chat_webhook")

router = APIRouter(prefix="/chat", tags=["web-chat"])


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    if not request.message or not request.message.strip():
        return ChatResponse(answer="Please enter a valid message.", session_id=request.session_id or "")

    # First message from a browser tab won't have a session_id yet -- mint one
    # and hand it back so the widget can store it (e.g. in localStorage) and
    # send it on every future call, which is what gives the web channel memory.
    session_id = request.session_id or str(uuid.uuid4())

    try:
        answer = run_turn(message=request.message, platform="web", user_id=session_id)
    except Exception:
        logger.exception("Agent failed on web chat message")
        answer = "Sorry, something went wrong on our end. Please try again shortly."

    return ChatResponse(answer=answer, session_id=session_id)
