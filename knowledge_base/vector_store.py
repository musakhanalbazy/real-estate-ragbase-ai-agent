"""Chroma vector store: build, load, and rebuild the company knowledge base."""

import os
import shutil
from typing import List

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from knowledge_base.company_data import get_company_documents

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "data/chroma_db")

_embeddings = OpenAIEmbeddings()


def _split_documents(documents: List[Document]) -> List[Document]:
    """Split documents into smaller chunks for better retrieval quality."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)


def build_vector_store() -> Chroma:
    """Build a brand new Chroma vector store from the company knowledge base."""
    documents = get_company_documents()
    chunks = _split_documents(documents)
    os.makedirs(CHROMA_DB_PATH, exist_ok=True)
    return Chroma.from_documents(
        documents=chunks,
        embedding=_embeddings,
        persist_directory=CHROMA_DB_PATH,
    )


def load_vector_store() -> Chroma:
    """Load the existing Chroma store from disk, or build one if it's missing."""
    if os.path.exists(CHROMA_DB_PATH) and os.listdir(CHROMA_DB_PATH):
        return Chroma(
            persist_directory=CHROMA_DB_PATH,
            embedding_function=_embeddings,
        )
    return build_vector_store()


def rebuild_vector_store() -> Chroma:
    """Delete the existing store and rebuild it from the current company data.

    Call this after editing knowledge_base/company_data.py, or hit the
    POST /admin/reindex endpoint, which calls this for you.
    """
    if os.path.exists(CHROMA_DB_PATH):
        try:
            store = Chroma(
                persist_directory=CHROMA_DB_PATH,
                embedding_function=_embeddings,
            )
            store.delete_collection()
        except Exception:
            shutil.rmtree(CHROMA_DB_PATH)
    return build_vector_store()
