from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
AGENT_ROOT = REPO_ROOT / "agent"

if str(AGENT_ROOT) not in sys.path:
    sys.path.insert(0, str(AGENT_ROOT))


@pytest.fixture(autouse=True)
def memory_store(monkeypatch: pytest.MonkeyPatch):
    """Keep tests hermetic: in-memory store, no live LLM/embedding/tracing calls."""
    monkeypatch.setenv("STORE_BACKEND", "memory")
    monkeypatch.delenv("REDIS_URL", raising=False)
    monkeypatch.delenv("UPSTASH_REDIS_REST_URL", raising=False)
    monkeypatch.delenv("UPSTASH_REDIS_REST_TOKEN", raising=False)
    monkeypatch.delenv("UPSTASH_VECTOR_REST_URL", raising=False)
    monkeypatch.delenv("UPSTASH_VECTOR_REST_TOKEN", raising=False)
    # main.py's load_dotenv can leak real keys into os.environ once any test
    # imports the app; the parser/eval tests assert offline fallback behavior.
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("PHOENIX_COLLECTOR_ENDPOINT", raising=False)

    from store import redis_client

    redis_client._ESTATES.clear()
    redis_client._VECTORS.clear()
    redis_client._USERS.clear()
    redis_client._USER_EMAILS.clear()
    redis_client._SESSIONS.clear()
    redis_client._DOC_FILES.clear()
    redis_client._REDIS_CLIENT = None
    redis_client._REDIS_CLOUD_CLIENT = None
    redis_client._VECTOR_CLIENT = None

    yield

    redis_client._ESTATES.clear()
    redis_client._VECTORS.clear()
    redis_client._USERS.clear()
    redis_client._USER_EMAILS.clear()
    redis_client._SESSIONS.clear()
    redis_client._DOC_FILES.clear()
