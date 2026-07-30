"""Retrieval helpers on top of the Chroma vector store.

This is the piece that guarantees RAG runs *before* the model answers:
conversation_layer/tools.py's search_knowledge_base tool calls
retrieve_documents() and returns the result as tool output, which the
agent must read before it is allowed to produce a final answer
(enforced by the system prompt in conversation_layer/system_prompt.py).
"""

from typing import List

from langchain_core.documents import Document

from knowledge_base.vector_store import load_vector_store

# Loaded once per process. refresh() swaps this out after a reindex.
_store = load_vector_store()


def refresh() -> None:
    """Reload the in-memory store reference after knowledge_base data changes."""
    global _store
    _store = load_vector_store()


def retrieve_documents(query: str, top_k: int = 5) -> List[Document]:
    """Return the top-k most relevant knowledge base chunks for a query."""
    retriever = _store.as_retriever(search_kwargs={"k": top_k})
    return retriever.invoke(query)


def format_context(documents: List[Document]) -> str:
    """Flatten retrieved documents into a single context string for the LLM."""
    if not documents:
        return "No relevant information found in the knowledge base."
    return "\n\n".join(doc.page_content for doc in documents)
