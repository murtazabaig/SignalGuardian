"""Private core loader for SignalGuardian public shell."""

from __future__ import annotations

from importlib import import_module
from types import ModuleType


def load_core() -> ModuleType:
    """Load the private core package or raise a clear error."""
    try:
        return import_module("signalguardian_core")
    except Exception as exc:  # pragma: no cover - import guard
        raise RuntimeError(
            "signalguardian_core is required. Install the private core package."
        ) from exc
