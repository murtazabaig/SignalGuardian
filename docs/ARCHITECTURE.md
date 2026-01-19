# Architecture (Public)

SignalGuardian is split into a public shell and a private core.

Public shell (this repo):
- Architecture and interface documentation
- API contracts and stub implementations
- Non-sensitive examples

Private core (separate repo):
- Signal generation algorithms
- Risk engine and proprietary scoring
- Production configs and deployment artifacts

High-level flow:
1) ScannerEngine fetches market data and builds feature sets.
2) ScoringEngine ranks candidates and produces decision scores.
3) PlannerEngine constructs trade plans and risk levels.
4) WarningEngine emits risk and market-wide alerts.

The public shell does not execute any trading logic.
