"""WhatsApp Cloud API webhook.

Meta calls GET /webhook/whatsapp once, at setup time, to verify ownership.
After that, every inbound message arrives as a POST here.
"""

import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Query, Request, Response

from app.settings import META_VERIFY_TOKEN
from conversation_layer.graph import run_turn
from webhook.message_sender import send_whatsapp_message

logger = logging.getLogger("tanveer.whatsapp_webhook")

router = APIRouter(prefix="/webhook/whatsapp", tags=["whatsapp"])


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

    if body.get("object") != "whatsapp_business_account":
        return {"status": "ignored"}

    for entry in body.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            for msg in value.get("messages", []):
                sender = msg.get("from")
                msg_type = msg.get("type")

                if not sender:
                    continue

                if msg_type == "text":
                    text = msg.get("text", {}).get("body", "").strip()
                    if not text:
                        continue
                    try:
                        reply = run_turn(message=text, platform="whatsapp", user_id=sender)
                    except Exception:
                        logger.exception("Agent failed on WhatsApp message from %s", sender)
                        reply = "Sorry, something went wrong on our end. Please try again shortly."
                    await send_whatsapp_message(sender, reply)
                else:
                    await send_whatsapp_message(
                        sender, "Sorry, I can only process text messages right now."
                    )

    return {"status": "ok"}
