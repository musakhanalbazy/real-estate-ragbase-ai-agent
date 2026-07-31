"""Request/response models for the FastAPI HTTP layer (web chat widget + admin routes)."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """Incoming message from the web chat widget."""
    message: str
    session_id: Optional[str] = None  # generated client-side, persists memory across page loads


class ChatResponse(BaseModel):
    answer: str
    session_id: str


class ConversationMessageOut(BaseModel):
    """One row from the conversations table."""
    id: int
    session_id: str
    platform: str
    role: str
    message: str
    token_count: int
    created_at: datetime


class ConversationSummaryOut(BaseModel):
    """Aggregated summary for one conversation session."""
    session_id: str
    platform: str
    message_count: int
    total_tokens: int
    started_at: datetime
    last_message_at: datetime


class LeadOut(BaseModel):
    """One row of the /admin/leads report."""
    user_id: str
    platform: str
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    property_type: Optional[str] = None
    city_or_area: Optional[str] = None
    budget_range: Optional[str] = None
    financing_method: Optional[str] = None
    purchase_timeline: Optional[str] = None
    preferred_call_time: Optional[str] = None
    site_visit_requested: bool = False
    stage: str
    score: int
    message_count: int
    handoff_requested: bool
    updated_at: datetime
