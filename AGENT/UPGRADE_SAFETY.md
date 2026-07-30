# Upgrade-Safe Development

> **Critical Rule**: The app must survive Frappe/ERPNext/HRMS version upgrades without breaking.

## Golden Rules

1. **Never modify core files** in `frappe/`, `erpnext/`, or `hrms/`
2. **Use hooks for all overrides** — they survive upgrades
3. **Use custom fields, not core field edits** — standard fields can change
4. **Use Property Setters for UI tweaks** — safe across versions
5. **Avoid monkey-patching** — prefer subclassing via `override_doctype_class`

## Safe vs Unsafe Approaches

### ✅ Safe (Upgrade-Proof)

| Approach | Use Case |
|----------|----------|
| Custom fields via JSON | Add fields to standard DocTypes |
| hooks.py `doc_events` | Trigger logic on standard DocType events |
| hooks.py `override_doctype_class` | Extend standard DocType methods |
| Custom DocTypes | New entities in your module |
| whitelisted API functions | Custom endpoints |
| Client scripts via `app_include_js` | JS behavior additions |
| Property Setters | Label/description/permission tweaks |
| Fixtures | Exportable configuration |

### ❌ Unsafe (Breaks on Upgrade)

| Approach | Why It Breaks |
|----------|--------------|
| Editing ERPNext Python files | Overwritten on update |
| Editing ERPNext JS files | Overwritten on update |
| Editing Frappe core | Overwritten on update |
| Hardcoding DocType field IDs | Internal IDs may change |
| Assuming field order/position | May be reorganized upstream |
| Using private/internal APIs | May be removed without notice |
| Direct table manipulation | Schema may change |

## Custom Field Best Practices

### Use `is_system_generated: 0`

This marks fields as user-created, preventing conflicts with system fields.

### Avoid Name Collisions

Check existing field names before adding:
```python
meta = frappe.get_meta("Employee")
existing = [f.fieldname for f in meta.fields]
if "national_id" in existing:
    frappe.throw("Field already exists")
```

### Use Module Isolation

Set `module: "Novatech Erp"` on all custom fields so they're scoped to your app.

### Use `insert_after` / `insert_before`

Position fields relative to existing ones rather than assuming positions:
```json
{
    "fieldname": "national_id",
    "insert_after": "passport_number"
}
```

## Override Doctype Class Safely

```python
# hooks.py
override_doctype_class = {
    "Sales Invoice": "novatech_erp.overrides.SalesInvoiceOverride",
}
```

```python
# overrides.py
from erpnext.accounts.doctype.sales_invoice.sales_invoice import (
    SalesInvoice as OriginalSalesInvoice,
)

class SalesInvoiceOverride(OriginalSalesInvoice):
    """Override only what's needed, call super() for the rest."""

    def on_submit(self):
        super().on_submit()  # Always call parent first
        self.create_project_from_invoice()
```

## Version Compatibility Checklist

Before any implementation:

- [ ] Does standard ERPNext/HRMS already do this?
- [ ] Am I using hooks instead of core edits?
- [ ] Will this work if Frappe field IDs change?
- [ ] Am I using public APIs only?
- [ ] Have I called `super()` in overrides?
- [ ] Is my custom field properly isolated?
- [ ] Have I documented the dependency?

## Bench Upgrade Process

```bash
# 1. Pull updates
bench update --pull

# 2. Run migrations
bench --site novatech.localhost migrate

# 3. Build assets
bench build

# 4. Restart
bench restart

# 5. Run tests
bench --site novatech.localhost run-tests --app novatech_erp
```

## Testing After Upgrade

1. Verify all custom fields still exist
2. Check custom DocType functionality
3. Run full test suite
4. Test all API endpoints
5. Verify UI behavior
6. Check scheduler tasks

## Common Upgrade Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Missing custom field | Field name conflict | Rename field, re-export |
| Broken override | Parent method signature changed | Update `super()` call |
| JS error | Framework API changed | Check Frappe changelog |
| Permission error | Role changes upstream | Update permission config |
| Migration error | Schema mismatch | Check `patches.txt` |
