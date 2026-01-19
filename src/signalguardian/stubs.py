"""Stub implementations that require the private core."""

from __future__ import annotations

from typing import Dict, List, Optional

from .interfaces import (
    MarketStructureEngine,
    LiquidityEngine,
    FvgEngine,
    OrderBlockEngine,
    WarningEngine,
    ScannerEngine,
    ScoringEngine,
    PlannerEngine,
    Signal,
    WarningSignal,
)


class _CoreMissingError(RuntimeError):
    pass


def _missing_core() -> _CoreMissingError:
    return _CoreMissingError(
        "signalguardian_core is required. Install the private core package."
    )


class StubMarketStructureEngine(MarketStructureEngine):
    def analyze(self, symbol: str, ohlcv: List[List[float]]) -> Dict[str, object]:
        raise _missing_core()


class StubLiquidityEngine(LiquidityEngine):
    def analyze(self, symbol: str, ohlcv: List[List[float]]) -> Dict[str, object]:
        raise _missing_core()


class StubFvgEngine(FvgEngine):
    def analyze(self, symbol: str, ohlcv: List[List[float]]) -> Dict[str, object]:
        raise _missing_core()


class StubOrderBlockEngine(OrderBlockEngine):
    def analyze(self, symbol: str, ohlcv: List[List[float]]) -> Dict[str, object]:
        raise _missing_core()


class StubWarningEngine(WarningEngine):
    def detect(self, universe: List[str]) -> List[WarningSignal]:
        raise _missing_core()


class StubScannerEngine(ScannerEngine):
    def scan(self, symbol: str) -> Optional[Signal]:
        raise _missing_core()


class StubScoringEngine(ScoringEngine):
    def score(self, symbol: str, features: Dict[str, object]) -> Dict[str, object]:
        raise _missing_core()


class StubPlannerEngine(PlannerEngine):
    def plan(self, symbol: str, side: str, context: Dict[str, object]) -> Dict[str, object]:
        raise _missing_core()
