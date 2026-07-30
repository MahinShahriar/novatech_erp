# Agent Instructions

> **Every AI agent must read and follow these rules before writing any code.**

## Core Principles

1. **Analyze before implementing.** Read requirements, check if standard Frappe/ERPNext/HRMS already provides the feature.
2. **Configuration over customization.** Use DocType settings, property setters, and custom fields before writing controllers.
3. **Reuse before creating.** Check if an existing DocType, function, or pattern solves the problem.
4. **Never modify core.** Do not edit files inside `frappe/`, `erpnext/`, or `hrms/` app directories.

## Pre-Implementation Checklist

Before writing code for any task:

- [ ] Read the relevant business requirement in `docs/Business Requirements/`
- [ ] Check if the feature exists in standard ERPNext/HRMS
- [ ] Review `CUSTOMIZATIONS.md` for existing overrides
- [ ] Review `PATTERNS.md` for established patterns
- [ ] Plan the DocType/API structure before coding
- [ ] Identify which roles/permissions are needed

## Documentation Policy

> **Documentation is a deliverable, not an afterthought.**

After completing every implementation, **immediately update user documentation** before considering the task finished.

### Where to document

Maintain documentation under `apps/novatech_erp/docs/user-guide/`. Organize by business department or module:

```
docs/user-guide/
├── README.md        ← Overview & index
├── hr.md            ← HR module features
├── projects.md      ← Project management features
├── crm.md           ← CRM features
├── finance.md       ← Finance features
└── ...              ← One file per module
```

If the appropriate document does not exist, **create it** using the module name.

### What to document

Update **only the relevant document**. Keep documentation cumulative — it always reflects current system behavior.

For every feature, document:

- **Feature name** and purpose
- **Business problem** it solves
- **Who can use it** (roles/departments)
- **Prerequisites** or required setup
- **Step-by-step usage** from a user's perspective
- **Business workflow** end-to-end
- **Inputs, validations, calculations, outputs**
- **System behavior**: automation, notifications, scheduled jobs, integrations
- **Related DocTypes**, reports, dashboards, menu paths
- **Configuration options** and permissions
- **Limitations**, assumptions, notes
- **Screens/forms/reports** affected
- **Links** to related features

### Writing style

- Write from the perspective of an **end user, ERP consultant, or client** — not a developer
- Explain **what** the feature does and **how** to use it
- Do **not** document implementation details unless they affect system behavior
- Keep it **simple, clear, and concise** — not lengthy articles
- Use bullet points, numbered steps, and tables

### Verification

After each implementation, verify the corresponding documentation has been updated. **Documentation is an essential deliverable.**

## Naming Conventions

| Item | Convention | Example |
|------|-----------|---------|
| DocType | Title Case, spaces OK | `Project Milestone` |
| DocType name (Python) | snake_case, no spaces | `project_milestone` |
| Python class | PascalCase | `ProjectMilestone` |
| JS filename | snake_case | `project_milestone.js` |
| Python filename | snake_case | `project_milestone.py` |
| Custom field name | snake_case | `national_id` |
| JSON export | snake_case | `project_milestone.json` |
| Module folder | snake_case | `novatech_erp` |
| Role | Title Case + spaces | `HR Manager` |

## Code Style

- **Line length**: 110 characters max
- **Python**: Ruff formatter, target Python 3.14
- **JS**: Prettier + ESLint (Frappe defaults)
- **Imports**: Use absolute imports within the app
- **Docstrings**: Google-style for all public methods

## Error Handling

- Use `frappe.throw()` for user-facing errors
- Use `frappe.msgprint()` for informational messages
- Log errors with `frappe.log_error()` for background jobs
- Always validate input in `validate()` method, not in API endpoints

## Permissions

- Define permissions in the DocType JSON, not in code
- Use existing Frappe roles when possible
- Create custom roles only when no existing role fits
- Test with the least-privileged role first
