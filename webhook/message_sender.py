"""Sends replies back out to WhatsApp / Messenger via the Meta Graph API."""

import logging

import httpx

from app.settings import (
    MESSENGER_PAGE_ACCESS_TOKEN,
    WHATSAPP_PHONE_NUMBER_ID,
    WHATSAPP_TOKEN,
)

logger = logging.getLogger("tanveer.message_sender")

MESSENGER_GRAPH_URL = "https://graph.facebook.com/v19.0/me/messages"
WHATSAPP_GRAPH_URL_TMPL = "https://graph.facebook.com/v20.0/{phone_id}/messages"


async def send_messenger_message(recipient_id: str, text: str) -> None:
    """Send a plain text reply to a Facebook Messenger user."""
    params = {"access_token": MESSENGER_PAGE_ACCESS_TOKEN}
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text},
        "messaging_type": "RESPONSE",
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(MESSENGER_GRAPH_URL, params=params, json=payload)
        if resp.status_code != 200:
            logger.error("Messenger send failed (%s): %s", resp.status_code, resp.text)


async def send_whatsapp_message(to_phone: str, text: str) -> None:
    """Send a plain text reply to a WhatsApp user."""
    url = WHATSAPP_GRAPH_URL_TMPL.format(phone_id=WHATSAPP_PHONE_NUMBER_ID)
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to_phone,
        "type": "text",
        "text": {"body": text},
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, headers=headers, json=payload)
        if resp.status_code != 200:
            logger.error("WhatsApp send failed (%s): %s", resp.status_code, resp.text)
