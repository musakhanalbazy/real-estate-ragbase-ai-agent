"""Rebuild the knowledge base vector store from the command line.

Run this after editing knowledge_base/company_data.py:

    python -m jobs.rebuild_knowledge_base_job

(Equivalent to hitting POST /admin/reindex on a running server, but handy
when you just want to refresh the local data/chroma_db folder offline.)
"""

from app import settings  # noqa: F401  (loads .env, validates OPENAI_API_KEY)
from knowledge_base.vector_store import rebuild_vector_store

if __name__ == "__main__":
    print("Rebuilding knowledge base vector store...")
    rebuild_vector_store()
    print("Done. data/chroma_db has been refreshed.")
