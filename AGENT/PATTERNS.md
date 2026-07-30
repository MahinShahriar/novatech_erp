# Implementation Patterns

## Pattern 1: Extend Standard DocType (Preferred)

**When**: Standard ERPNext/HRMS DocType covers 80%+ of the need.

**How**:
1. Add custom fields via `custom/<doctype>.json`
2. Add server logic via `hooks.py` document events
3. Add client logic via `public/js/<doctype>_custom.js`

```python
# hooks.py
doc_events = {
    "Employee": {
        "validate": "novatech_erp.hr.employee_custom.validate_employee",
    }
}
```

```python
# novatech_erp/hr/employee_custom.py
def validate_employee(doc, method):
    if doc.national_id and len(doc.national_id) < 10:
        frappe.throw(_("National ID must be at least 10 characters"))
```

## Pattern 2: Custom DocType (When Extension Isn't Enough)

**When**: Business entity doesn't map to any standard DocType.

**Structure**:
```
doctype/
└── project_milestone/
    ├── project_milestone.json
    ├── project_milestone.py
    ├── project_milestone.js
    └── test_project_milestone.py
```

**Controller skeleton**:
```python
class ProjectMilestone(Document):
    def validate(self):
        self.validate_dates()
        self.calculate_progress()

    def before_save(self):
        self.update_parent_progress()

    def validate_dates(self):
        if self.end_date and self.end_date < self.start_date:
            frappe.throw(_("Invalid date range"))

    def calculate_progress(self):
        if self.total_tasks:
            self.progress = (self.completed_tasks / self.total_tasks) * 100

    def update_parent_progress(self):
        if self.project:
            project = frappe.get_doc("Project", self.project)
            project.save()
```

## Pattern 3: Whitelisted API (Client → Server)

**When**: Need custom logic callable from JS or external integrations.

```python
# api.py
@frappe.whitelisted()
def get_project_summary(project):
    """Return project summary for dashboard."""
    if not frappe.has_permission("Project", "read"):
        frappe.throw(_("Not permitted"))

    milestones = frappe.get_all(
        "Project Milestone",
        filters={"project": project},
        fields=["milestone_name", "progress", "status"],
    )
    return {"milestones": milestones}
```

```javascript
// Client side
frappe.call({
    method: "novatech_erp.api.get_project_summary",
    args: { project: frm.doc.name },
    callback: (r) => {
        // handle r.message
    },
});
```

## Pattern 4: Child Table (Parent → Detail Rows)

**When**: One parent has many detail rows (e.g., Time Log entries).

**Child DocType JSON** must have:
```json
{ "istable": 1, "is_submittable": 0 }
```

**Parent controller**:
```python
class Project(Document):
    def validate(self):
        self.total_hours = sum(row.hours for row in self.time_logs or [])
```

## Pattern 5: Auto-Naming

**Common patterns**:
```json
{ "autoname": "naming_series:" }
// Uses Naming Series field

{ "autoname": "field:project + '-' + field:milestone_name" }
// Combines fields

{ "autoname": "format:NT-{YYYY}-{MM}-{####}" }
// Custom format
```

## Pattern 6: Workflow States

Instead of hardcoded statuses, use Frappe workflow or field options:

```json
{
    "fieldname": "status",
    "fieldtype": "Select",
    "options": "\nDraft\nOpen\nIn Progress\nCompleted\nCancelled",
    "default": "Draft"
}
```

## Pattern 7: Link + Fetch

Auto-populate fields from linked DocType:

```json
{
    "fieldname": "employee",
    "fieldtype": "Link",
    "options": "Employee"
},
{
    "fieldname": "employee_name",
    "fieldtype": "Data",
    "fetch_from": "employee.employee_name",
    "read_only": 1
}
```

## Pattern 8: Permission Rules

Define in DocType JSON:
```json
{
    "permissions": [
        {
            "role": "HR Manager",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1
        },
        {
            "role": "HR User",
            "read": 1,
            "write": 1,
            "create": 1
        }
    ]
}
```

Programmatic check:
```python
if not frappe.has_permission("DocType Name", "write"):
    frappe.throw(_("Insufficient permissions"))
```

## Pattern 9: Scheduled Tasks

```python
# hooks.py
scheduler_events = {
    "daily": [
        "novatech_erp.tasks.daily_reminders"
    ],
    "hourly": [
        "novatech_erp.tasks.check_sla_breaches"
    ],
}
```

## Pattern 10: Fixtures (Exportable Config)

For settings that should be migrateable between sites:
```python
# hooks.py
fixtures = ["Custom Field", "Property Setter"]
```

## Reusable Utilities

| Utility | Location | Purpose |
|---------|----------|---------|
| `frappe.utils.data` | Built-in | Date/time/string helpers |
| `frappe.utils.file_manager` | Built-in | File handling |
| `erpnext.accounts.utils` | ERPNext | Accounting helpers |
| `hrms.hr.utils` | HRMS | HR calculation helpers |
| Custom utils | `novatech_erp/utils.py` | Project-specific helpers |

## Anti-Patterns to Avoid

| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| Modify ERPNext/HRMS core files | Use hooks, custom fields |
| Hardcode site URLs | Use `frappe.utils.get_url()` |
| Raw SQL for simple queries | Use `frappe.get_list()`, `frappe.get_all()` |
| `print()` for debugging | Use `frappe.log_error()` or `frappe.msgprint()` |
| Direct DB writes outside DocType | Use `frappe.get_doc().insert()` / `.save()` |
| Skip validation for speed | Always validate, use flags sparingly |
| Store config in code | Use `frappe.conf` or Custom DocType |
| Create duplicate DocTypes | Extend existing ones with custom fields |
