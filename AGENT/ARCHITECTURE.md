# Project Architecture

## App Structure

```
novatech_erp/                          ← App root (Git repo)
├── pyproject.toml                     ← Build config (flit), ruff settings
├── .pre-commit-config.yaml            ← Pre-commit hooks (ruff, prettier, eslint)
├── .github/workflows/                 ← CI (ci.yml, linter.yml)
├── docs/                              ← Business requirements & user guides
│   ├── Business Requirements/         ← Detailed specs per module
│   └── user-guide/                    ← End-user documentation
├── AGENT/                             ← AI agent knowledge base (this folder)
└── novatech_erp/                      ← App Python package
    ├── __init__.py                    ← __version__
    ├── hooks.py                       ← Frappe hooks (events, includes, scheduler)
    ├── modules.txt                    ← Declared modules: "Novatech Erp"
    ├── patches.txt                    ← Migration patches (empty)
    ├── config/                        ← App configuration
    ├── novatech_erp/                  ← Module directory
    │   ├── custom/                    ← DocType customizations (JSON)
    │   ├── doctype/                   ← Custom DocTypes (not yet created)
    │   ├── report/                    ← Custom reports (not yet created)
    │   ├── page/                      ← Custom pages (not yet created)
    │   └── dashboard/                 ← Dashboards (not yet created)
    ├── public/                        ← Client-side assets (JS, CSS, images)
    ├── templates/                     ← Jinja templates, web pages
    └── patches/                       ← Data migration patches
```

## Frappe Framework Layers

```
┌─────────────────────────────────────────┐
│           Client Layer (JS)             │  ← Form scripts, pages, dashboards
├─────────────────────────────────────────┤
│           API Layer (Whitelisted)       │  ← @frappe.whitelisted functions
├─────────────────────────────────────────┤
│           Controller Layer (Python)     │  ← DocType class methods
├─────────────────────────────────────────┤
│           Model Layer (DocType JSON)    │  ← Schema, fields, permissions
├─────────────────────────────────────────┤
│           Database Layer (MariaDB)      │  ← Tables, queries, migrations
└─────────────────────────────────────────┘
```

## Key Framework Concepts

### DocType Lifecycle

```
before_insert → validate → before_save → before_insert (new) → after_insert → on_update → on_change → after_save
```

For existing docs: `validate → before_save → on_update → on_change → after_save`

### Standard Controller Methods

| Method | Purpose |
|--------|---------|
| `validate()` | Run before save. Enforce business rules. |
| `before_save()` | Runs after validate, before DB write. |
| `after_insert()` | Runs once after first insert. |
| `on_update()` | Runs after every save. |
| `on_submit()` | Runs on Submit (for submittable docs). |
| `on_cancel()` | Runs on Cancel. |
| `before_naming()` | Custom naming logic before doc is named. |
| `autoname()` | Define naming series. |

### Frappe ORM Basics

```python
# Create
doc = frappe.get_doc({"doctype": "My DocType", "field": "value"})
doc.insert()

# Read
doc = frappe.get_doc("My DocType", "name")
val = doc.field_name

# Update
doc.field_name = "new value"
doc.save()

# Delete
frappe.delete_doc("My DocType", "name")

# List / Query
frappe.get_list("My DocType", filters={...}, fields=[...])

# RPC
frappe.get_attr("module.api.function")(*args, **kwargs)
```

## Bench Environment

```
frappe-bench/                          ← Bench root
├── apps/                              ← Installed apps
│   ├── frappe/                        ← Framework core
│   ├── erpnext/                       ← ERP modules
│   ├── hrms/                          ← HR modules
│   └── novatech_erp/                  ← This app
├── sites/                             ← Site data
│   ├── common_site_config.json
│   ├── novatech.localhost/            ← Dev site
│   └── development.localhost/
├── env/                               ← Python virtualenv
├── logs/                              ← Log files
└── config/                            ← Procfile, scheduler
```

## Dependencies

| Dependency | Purpose |
|-----------|---------|
| `frappe` | Core framework, ORM, UI, REST API |
| `erpnext` | Accounting, Stock, Buying, Selling, CRM, Projects |
| `hrms` | Employee, Attendance, Leave, Payroll, Recruitment |

> **Rule**: Never modify files in `frappe/`, `erpnext/`, or `hrms/`. Use hooks, custom fields, and overrides instead.
