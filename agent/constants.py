"""Repo-wide constants with no dependencies of their own, so both the schema
layer and the store layer can import from here without a circular import
(store/redis_client.py imports from schemas/api.py, so schemas/api.py can't
import DEFAULT_ESTATE_ID back from the store)."""

from __future__ import annotations

DEFAULT_ESTATE_ID = "demo-milligan"
