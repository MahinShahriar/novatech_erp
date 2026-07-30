# Hooks, APIs, and Scheduled Tasks

## hooks.py Overview

`hooks.py` is the central configuration for app integration with Frappe framework. Currently mostly commented out — will be activated as features are built.

## Document Events

Trigger Python functions on DocType lifecycle:

```python
doc_events = {
    # Single DocType
    "Employee": {
        "validate": "novatech_erp.hr.employee_hooks.validate",
        "on_update": "novatech_erp.hr.employee_hooks.on_update",
    },
    # All DocTypes
    "*": {
        "after_insert": "novatech_erp.common.on_after_insert",
    }
}
```

### Available Events

| Event | When |
|-------|------|
| `before_insert` | Before first save of new doc |
| `validate` | Before every save |
| `before_save` | After validate, before DB write |
| `after_insert` | After first insert |
| `on_update` | After every save |
| `on_change` | After any change (including workflow) |
| `after_save` | Final hook after save |
| `before_submit` | Before submit (submittable docs) |
| `on_submit` | After submit |
| `on_cancel` | After cancel |
| `on_trash` | Before delete |
| `after_delete` | After delete |

## Scheduler Events

```python
scheduler_events = {
    "all":     ["module.function"],       # Every minute
    "hourly":  ["module.function"],       # Every hour
    "daily":   ["module.function"],       # Once daily (00:00)
    "weekly":  ["module.function"],       # Weekly (Sunday)
    "monthly": ["module.function"],       # Monthly (1st)
    "cron": {
        "0 9 * * *": ["module.function"],  # Custom cron
    },
}
```

## Overrides

Override framework or dependency methods:

```python
override_doctype_class = {
    "Sales Invoice": "novatech_erp.overrides.SalesInvoice",
}
```

```python
# overrides.py
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice

class SalesInvoice(SalesInvoice):
    def on_submit(self):
        super().on_submit()
        self.trigger_project_creation()
```

## Client Script Includes

Auto-load JS on specific DocTypes:

```python
app_include_js = [
    "/assets/novatech_erp/js/project_custom.js",
]
# OR per-doctype
doctype_js = {
    "Project": "public/js/project_hooks.js",
}
```

## Fixtures

Export custom configurations between sites:

```python
fixtures = [
    "Custom Field",
    "Property Setter",
    "Workflow",
    "Workflow State",
    "Workflow Action",
]
```

## Jinja Methods

Add custom Jinja template functions:

```python
jinja = {
    "methods": [
        "novatech_erp.utils.jinja_methods",
    ]
}
```

## Website Route Rules

```python
website_route_rules = [
    {
        "from_route": "/portal/projects/<name>",
        "to_route": "project",
        "defaults": {"doctype": "Project"},
    }
]
```

## whitelisted API Conventions

```python
# In any .py file (usually api.py or module-level)
@frappe.whitelisted()
def get_data():
    """Callable via frappe.call or REST API."""
    pass

@frappe.whitelist(allow_guest=True)
def public_endpoint():
    """Callable without login."""
    pass

@frappe.whitelist(methods=["POST"])
def create_something():
    """POST only."""
    pass
```

## API URL Pattern

```
POST /api/method/novatech_erp.module.function_name
GET  /api/method/novatech_erp.module.function_name?arg=value
```

## Current State

| Hook Type | Status |
|-----------|--------|
| `doc_events` | Not configured |
| `scheduler_events` | Not configured |
| `override_doctype_class` | Not configured |
| `app_include_js` | Not configured |
| `fixtures` | Not configured |
| `required_apps` | ✅ `['frappe', 'erpnext', 'hrms']` |
