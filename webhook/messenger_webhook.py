"""Facebook Messenger webhook (Meta Graph API, page-level events)."""

import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Query, Request, Response

from app.settings import META_VERIFY_TOKEN
from conversation_layer.graph import run_turn
from webhook.message_sender import send_messenger_message

logger = logging.getLogger("tanveer.messenger_webhook")

router = APIRouter(prefix="/webhook/messenger", tags=["messenger"])


@router.get("")
def verify_webhook(
    hub_mode: Optional[str] = Query(None, alias="hub.mode"),
    hub_verify_token: Optional[str] = Query(None, alias="hub.verify_token"),
    hub_challenge: Optional[str] = Query(None, alias="hub.challenge"),
):
    if hub_mode == "subscribe" and hub_verify_token == META_VERIFY_TOKEN:
        return Response(content=hub_challenge, media_type="text/plain")
    raise HTTPException(status_code=403, detail="Verification failed")


@router.post("")
async def receive_message(request: Request):
    body = await request.json()

    if body.get("object") != "page":
        return {"status": "ignored"}

    for entry in body.get("entry", []):
        for event in entry.get("messaging", []):
            sender_id = event.get("sender", {}).get("id")
            if not sender_id:
                continue

            message = event.get("message", {})

            if "text" in message:
                text = message["text"].strip()
                if not text:
                    continue
                reply = await _safe_run_turn(text, sender_id)
                await send_messenger_message(sender_id, reply)

            elif "attachments" in message:
                await send_messenger_message(
                    sender_id, "Sorry, I can only process text messages right now."
                )

            elif "postback" in event:
                payload = event["postback"].get("payload", "")
                if payload:
                    reply = await _safe_run_turn(payload, sender_id)
                    await send_messenger_message(sender_id, reply)

    return {"status": "ok"}


async def _safe_run_turn(text: str, sender_id: str) -> str:
    try:
        return run_turn(message=text, platform="messenger", user_id=sender_id)
    except Exception:
        logger.exception("Agent failed on Messenger message from %s", sender_id)
        return "Sorry, something went wrong on our end. Please try again shortly."
