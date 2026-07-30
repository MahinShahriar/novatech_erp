# Coding Standards

## Python

### Style
- **Formatter**: Ruff
- **Line length**: 110 characters
- **Target**: Python 3.14
- **Quotes**: Double quotes for strings
- **Imports**: Absolute within the app, grouped (stdlib → third-party → frappe → erpnext → hrms → local)

### Example

```python
import frappe
from frappe import _
from frappe.model.document import Document

class ProjectMilestone(Document):
    """Represents a milestone within a project."""

    def validate(self):
        self.validate_dates()
        self.set_status()

    def validate_dates(self):
        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                frappe.throw(_("End date cannot be before start date"))
```

### Rules
- Use `frappe._()` for all user-facing strings (i18n ready)
- Validate in `validate()`, compute in `before_save()`, trigger in `on_update()`
- Never use `frappe.db.sql()` when ORM methods work
- Use `frappe.only_for()` for role checks, not manual queries
- Handle `None` checks explicitly — don't assume fields are populated

## JavaScript

### Style
- **Formatter**: Prettier
- **Linter**: ESLint (Frappe defaults)
- **Module system**: Frappe provided (no ES modules)

### Example

```javascript
frappe.ui.form.on("Project Milestone", {
    refresh(frm) {
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__("Mark Complete"), () => {
                frappe.call({
                    method: "mark_complete",
                    doc: frm.doc,
                    callback: () => frm.reload_doc(),
                });
            });
        }
    },

    project(frm) {
        if (frm.doc.project) {
            frm.set_query("task", () => ({
                filters: { project: frm.doc.project },
            }));
        }
    },
});
```

### Rules
- Always use `frm` (lowercase) for form object in newer Frappe versions
- Use `frappe.call()` for server interaction, never raw AJAX
- Use `frm.set_value()` instead of direct field assignment for proper events
- Use `__()` for translatable strings in JS

## JSON (DocType Definitions)

- Tab indentation (2 spaces for Frappe standard)
- Field names: snake_case
- Field labels: Title Case (human readable)
- Always include `"description"` for complex fields
- Set `"reqd": 1` for mandatory fields, not in validate()

## File Organization

| Content | Location |
|---------|----------|
| Python controllers | `doctype/<name>/<name>.py` |
| Client scripts | `doctype/<name>/<name>.js` |
| JSON schema | `doctype/<name>/<name>.json` |
| Server scripts | `doctype/<name>/<name>.py` (same file) |
| Web templates | `templates/<path>/` |
| Static assets | `public/js/`, `public/css/` |
| Tests | `doctype/<name>/test_<name>.py` |
| Custom fields | `custom/<doctype_name>.json` |

## Commit Messages

Follow conventional commits:
```
feat(project): add milestone tracking
fix(hr): correct attendance calculation
docs: update user guide for leave module
```
