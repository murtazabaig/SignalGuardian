# Stubs

Stub classes in `src/signalguardian/stubs.py` raise a clear error if the private
core package is not installed. This ensures:
- Public repo is safe to share
- Runtime usage requires the private core

To run the full system, install the private core package:
- `signalguardian_core` (private repo)
