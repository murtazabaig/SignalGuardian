"""Public interfaces for SignalGuardian core modules."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Signal:
    symbol: str
    side: str
    confidence: float
    reason: Dict[str, object]


@dataclass(frozen=True)
class WarningSignal:
    warning_type: str
    severity: str
    message: str
    metadata: Dict[str, object]


class MarketStructureEngine(ABC):
    @abstractmethod
    def analyze(self, symbol: str, ohlcv: List[List[float]]) -> Dict[str, object]:
        raise NotImplementedError


class LiquidityEngine(ABC):
    @abstractmethod
    def analyze(self, symbol: str, ohlcv: List[List[float]]) -> Dict[str, object]:
        raise NotImplementedError


class FvgEngine(ABC):
    @abstractmethod
    def analyze(self, symbol: str, ohlcv: List[List[float]]) -> Dict[str, object]:
        raise NotImplementedError


class OrderBlockEngine(ABC):
    @abstractmethod
    def analyze(self, symbol: str, ohlcv: List[List[float]]) -> Dict[str, object]:
        raise NotImplementedError


class WarningEngine(ABC):
    @abstractmethod
    def detect(self, universe: List[str]) -> List[WarningSignal]:
        raise NotImplementedError


class ScannerEngine(ABC):
    @abstractmethod
    def scan(self, symbol: str) -> Optional[Signal]:
        raise NotImplementedError


class ScoringEngine(ABC):
    @abstractmethod
    def score(self, symbol: str, features: Dict[str, object]) -> Dict[str, object]:
        raise NotImplementedError


class PlannerEngine(ABC):
    @abstractmethod
    def plan(self, symbol: str, side: str, context: Dict[str, object]) -> Dict[str, object]:
        raise NotImplementedError
