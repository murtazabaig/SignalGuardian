# SignalGuardian (Public Shell)

This repository is the public-facing shell for SignalGuardian. It provides
architecture documentation, interfaces, and stub implementations only.

Core logic and proprietary algorithms live in the private repository.

## Contents
- docs/ARCHITECTURE.md: System-level architecture overview
- docs/INTERFACES.md: Interface contracts and data shapes
- docs/STUBS.md: Stub behavior and extension notes
- src/signalguardian: Interface definitions and stub classes

## How this integrates with the private core
This shell expects a private package named `signalguardian_core` to be
available at runtime. The public stubs will raise a clear error if the
private core is not installed.

## Quick start (public shell)
This repo is for visibility and documentation. It does not run the bot.
Install the private core package to run SignalGuardian.
