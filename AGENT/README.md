# NovaTech ERP — AI Agent Knowledge Base

> **Purpose**: Permanent project context for AI coding agents. Read this first to understand the project before any implementation.

## Quick Facts

| Item | Value |
|------|-------|
| **App** | `novatech_erp` v0.0.1 |
| **Framework** | Frappe v16 |
| **Dependencies** | `frappe`, `erpnext`, `hrms` |
| **Python** | ≥ 3.14 |
| **Company** | NovaTech Solutions Ltd. (Bangladesh) |
| **License** | MIT |

## Reading Order

Read these files **in sequence** before starting any work:

| # | File | Purpose |
|---|------|---------|
| 1 | [AGENT_INSTRUCTIONS.md](AGENT_INSTRUCTIONS.md) | **Start here.** Rules and workflow every agent must follow. |
| 2 | [ARCHITECTURE.md](ARCHITECTURE.md) | Project structure, app layout, framework layers. |
| 3 | [MODULES.md](MODULES.md) | Module organization, doctypes, naming conventions. |
| 4 | [REQUIREMENTS.md](REQUIREMENTS.md) | Business requirements summary (links to detailed docs). |
| 5 | [STANDARDS.md](STANDARDS.md) | Coding standards, naming, file structure rules. |
| 6 | [PATTERNS.md](PATTERNS.md) | Implementation patterns, reusable utilities, controllers. |
| 7 | [HOOKS.md](HOOKS.md) | hooks.py usage, APIs, scheduled tasks, events. |
| 8 | [CUSTOMIZATIONS.md](CUSTOMIZATIONS.md) | Current customizations on standard DocTypes. |
| 9 | [TESTING.md](TESTING.md) | Testing strategy and conventions. |
| 10 | [WORKFLOW.md](WORKFLOW.md) | Development workflow: branching, PRs, bench commands. |
| 11 | [UPGRADE_SAFETY.md](UPGRADE_SAFETY.md) | Rules for upgrade-safe development. |

## Current State

The app is in **early development**. Only standard HRMS field customizations exist. No custom DocTypes, controllers, scripts, reports, or dashboards have been built yet.

## Detailed Requirements

Full business requirements are in `docs/Business Requirements/`:

- [`main.md`](../docs/Business%20Requirements/main.md) — Company-wide ERP scope
- [`hr.md`](../docs/Business%20Requirements/hr.md) — HR module detailed spec
- [`project.md`](../docs/Business%20Requirements/project.md) — Project management spec

## File Map

```
AGENT/
├── README.md                 ← You are here
├── AGENT_INSTRUCTIONS.md     ← Agent rules & documentation policy
├── ARCHITECTURE.md           ← Project structure & framework layers
├── MODULES.md                ← Module & doctype organization
├── REQUIREMENTS.md           ← Business requirements summary
├── STANDARDS.md              ← Coding standards & naming conventions
├── PATTERNS.md               ← Implementation patterns
├── HOOKS.md                  ← Hooks, APIs, events, schedulers
├── CUSTOMIZATIONS.md         ← Current field customizations
├── TESTING.md                ← Testing strategy
├── WORKFLOW.md               ← Dev workflow & bench commands
└── UPGRADE_SAFETY.md         ← Upgrade-safe development rules
```

---

*Last updated: 2026-07-30*
