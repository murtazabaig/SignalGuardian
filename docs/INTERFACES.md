# Interfaces

The public shell provides abstract interfaces for the private core.

Key contracts:
- MarketStructureEngine.analyze(symbol, ohlcv) -> dict
- LiquidityEngine.analyze(symbol, ohlcv) -> dict
- FvgEngine.analyze(symbol, ohlcv) -> dict
- OrderBlockEngine.analyze(symbol, ohlcv) -> dict
- WarningEngine.detect(universe) -> list[WarningSignal]
- ScannerEngine.scan(symbol) -> Signal | None
- ScoringEngine.score(symbol, features) -> dict
- PlannerEngine.plan(symbol, side, context) -> dict

See `src/signalguardian/interfaces.py` for types and required methods.
