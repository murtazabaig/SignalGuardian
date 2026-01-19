# SignalGuardian (Public Shell)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Repo](https://img.shields.io/badge/public-shell-lightgrey)
![Docs](https://img.shields.io/badge/docs-architecture%20%7C%20interfaces%20%7C%20stubs-informational)

This repository is the public-facing shell for SignalGuardian. It provides
architecture documentation, interfaces, and stub implementations only.

Core logic and proprietary algorithms live in the private repository.

## Status
- Public shell only (docs + interfaces + stubs)
- Private core required to run SignalGuardian

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

## Pricing

### Starter
$29 / month  
$290 / year (2 months free)

Includes
- Telegram alerts for basic signals
- Limited asset pairs and timeframes
- Standard risk parameters
- Daily signal summaries
- Community-level support

Best for
- Retail traders
- Beginners testing automated signals

Free trial
- 7-day free trial
- No setup fee

---

### Pro
$79 / month  
$790 / year (2 months free)

Includes
- Everything in Starter
- Advanced multi-timeframe scanning
- Risk-adjusted position sizing
- Custom alert rules
- Performance reporting
- Priority updates

Best for
- Active traders
- Semi-professional users

Free trial
- 7-day free trial
- No setup fee

---

### Elite
$199 / month  
$1,990 / year

Includes
- Everything in Pro
- High-frequency signal engine
- Custom strategies per user
- Dedicated Telegram bot instance
- Early access to new features
- Priority support

Best for
- Professional traders
- Signal resellers
- Power users

Free trial
- No free trial
- 1-time onboarding included

---

### Enterprise / Custom
Starting at $500+ / month (custom pricing)

Includes
- Fully custom signal logic
- Private deployment
- Custom exchanges and assets
- SLA-backed support
- Strategy confidentiality
- Integration with existing systems

Best for
- Funds
- Trading teams
- Businesses

Free trial
- No
- Paid setup depending on scope

## Why pricing exists
- Prevents abuse, spam, and unqualified usage
- Funds infrastructure, maintenance, and support
- Keeps quality high and development focused

## Attribution & usage notice
SignalGuardian is proprietary software. Redistribution, resale, or commercial
use without explicit permission is prohibited. Contact for licensing,
enterprise access, or custom deployments.

## Contact / Purchase
All plans require approval and onboarding.
https://murtazabaig.vercel.app/

---

Made by M. Murtaza Baig
