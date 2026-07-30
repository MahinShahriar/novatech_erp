# Development Workflow

## Prerequisites

- Frappe Bench environment set up
- MariaDB running
- Site created (`novatech.localhost`)
- `bench start` running (for development)

## Common Bench Commands

### Site Management

```bash
# Drop and recreate site
bench drop-site novatech.localhost
bench new-site novatech.localhost

# Migrate after DocType changes
bench --site novatech.localhost migrate

# Clear cache
bench --site novatech.localhost clear-cache

# Set site as default
bench use novatech.localhost
```

### Development

```bash
# Start all services (web, worker, scheduler, socketio)
bench start

# Build assets
bench build --app novatech_erp

# Console (Python REPL with Frappe context)
bench --site novatech.localhost console

# Run specific Python
bench --site novatech.localhost execute novatech_erp.api.my_function
```

### DocType Management

```bash
# After editing DocType JSON, migrate
bench --site novatech.localhost migrate

# Export DocType to JSON (from bench console)
bench --site novatech.localhost export-fixtures

# Add custom field via bench
bench --site novatech.localhost add-to-json ...
```

### Testing

```bash
# Run all app tests
bench --site novatech.localhost run-tests --app novatech_erp

# Run specific DocType tests
bench --site novatech.localhost run-tests --doctype "Project Milestone"
```

### Git Workflow

```bash
# Feature branch
git checkout -b feat/milestone-tracking

# Commit with conventional commits
git commit -m "feat(project): add milestone tracking doctype"

# Push and create PR
git push origin feat/milestone-tracking
```

## Development Flow

```
1. Read requirement     → docs/Business Requirements/
2. Check standard func  → ERPNext/HRMS DocType search
3. Plan implementation  → Choose pattern (extend vs custom)
4. Create DocType       → JSON + Python + JS
5. Add hooks/config     → hooks.py
6. Write tests          → test_<name>.py
7. Run tests            → bench run-tests
8. Migrate              → bench migrate
9. Update user docs     → docs/user-guide/
10. Update AGENT docs   → AGENT/CUSTOMIZATIONS.md (if customization)
```

## File Change Triggers

| Change Type | Required Actions |
|-------------|-----------------|
| New DocType JSON | `bench migrate` |
| Field changes | `bench migrate` |
| Permission changes | `bench migrate` |
| hooks.py changes | `bench restart` |
| JS changes | `bench build --app novatech_erp` |
| Python controller | No rebuild needed (hot reload) |
| Custom fields JSON | `bench migrate` |

## Environment Variables

| Variable | Purpose |
|----------|---------|
| ` sites/` | Site configuration |
| `FRAPPE_SITE` | Default site for CLI |
| `DB_HOST` | Database host |
| `DB_PORT` | Database port |

## Useful Console Commands

```python
# bench console

# Check DocType meta
meta = frappe.get_meta("Employee")
for f in meta.fields:
    if f.fieldname:
        print(f.fieldname, f.fieldtype, f.options)

# List all custom fields
frappe.get_all("Custom Field", filters={"dt": "Employee"}, fields=["fieldname", "fieldtype"])

# Test a function
from novatech_erp.api import get_project_summary
get_project_summary("PRJ-001")

# Check permissions
frappe.permissions.get_doctypes_with_read()
```

## Logging

```bash
# View error logs
tail -f sites/novatech.localhost/logs/frappe.log

# View scheduler logs
tail -f sites/novatech.localhost/logs/frappe.log | grep "scheduler"

# Database query log
tail -f sites/novatech.localhost/logs/database.log
```
