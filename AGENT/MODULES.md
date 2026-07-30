# Module Organization

## Declared Module

The app declares a single module in `modules.txt`:

```
Novatech Erp
```

All custom DocTypes and customizations live under this module.

## Planned Module Structure

Based on business requirements, the following sub-modules will be organized under `Novatech Erp`:

| Module | DocTypes (Planned) | Status |
|--------|-------------------|--------|
| **Novatech HR** | Extended Employee fields, Attendance customizations | ✅ Custom fields only |
| **CRM** | Meeting, Follow-up, Proposal (extend standard Lead/Opportunity) | ❌ Not started |
| **Projects** | Project Milestone, Time Log, Project Report | ❌ Not started |
| **Finance** | AMC Contract, recurring invoicing | ❌ Not started |
| **Helpdesk** | Ticket extensions, SLA tracking | ❌ Not started |
| **Client Portal** | Portal pages, API endpoints | ❌ Not started |

## DocType Directory Convention

Each DocType lives in its own folder under the module:

```
novatech_erp/novatech_erp/
├── doctype/
│   ├── project_milestone/
│   │   ├── project_milestone.json       ← Schema definition
│   │   ├── project_milestone.py         ← Python controller
│   │   ├── project_milestone.js         ← Client script
│   │   └── test_project_milestone.py    ← Tests
│   └── time_log/
│       ├── time_log.json
│       ├── time_log.py
│       ├── time_log.js
│       └── test_time_log.py
├── report/
│   ├── project_progress/
│   │   ├── project_progress.json
│   │   ├── project_progress.py
│   │   └── project_progress.js
├── page/
│   └── project_dashboard/
│       ├── project_dashboard.json
│       └── project_dashboard.js
└── dashboard/
    └── project_dashboard/
        └── project_dashboard.json
```

## Customization JSON Convention

Field customizations on standard DocTypes are stored in:

```
novatech_erp/novatech_erp/custom/
├── employee.json          ← Custom fields on Employee
├── attendance.json        ← Custom fields on Attendance
├── employee_checkin.json  ← Custom fields on Employee Checkin
└── shift_type.json        ← Permission changes on Shift Type
```

## DocType Naming Rules

| Rule | Example | Wrong |
|------|---------|-------|
| Spaces in DocType name | `Project Milestone` | `ProjectMilestone` |
| snake_case for filenames | `project_milestone.py` | `ProjectMilestone.py` |
| PascalCase for Python class | `ProjectMilestone` | `project_milestone` |
| Module prefix optional | `Time Log` (in Novatech module) | `Novatech Time Log` |
| Use existing ERPNext names | Extend `Project`, `Task` | Create `Nova Project` |

## DocType JSON Structure

```json
{
  "name": "Project Milestone",
  "module": "Novatech Erp",
  "doctype": "DocType",
  "fields": [...],
  "permissions": [...],
  "autoname": "field:project + '-' + field:milestone_name",
  "is_submittable": 0,
  "is_tree": 0,
  "is_calendar_and_gantt": 0
}
```

## Field Type Reference

| Type | Use Case |
|------|----------|
| `Data` | Short text, single line |
| `Small Text` | Multi-line text |
| `Text` | Long text (no formatting) |
| `Text Editor` | Rich text with formatting |
| `Select` | Dropdown with fixed options |
| `Check` | Checkbox (0/1) |
| `Int` | Integer |
| `Float` | Decimal number |
| `Currency` | Money with currency symbol |
| `Percent` | Percentage |
| `Date` | Date only |
| `Datetime` | Date + time |
| `Time` | Time only |
| `Link` | Foreign key to another DocType |
| `Table` | Child table (rows) |
| `Table MultiSelect` | Many-to-many via child table |
| `Attach` | File upload |
| `Attach Image` | Image upload with preview |
| `Code` | Code editor with syntax highlighting |
| `Color` | Color picker |
| `Geolocation` | Map coordinates |
| `Rating` | Star rating |
| `Read Only` | Computed/display only |
| `Password` | Encrypted field |

## Relationship Patterns

### One-to-Many (Parent → Child)
Use `Table` field type pointing to a child DocType marked as `istable: 1`.

### Many-to-Many
Use `Table MultiSelect` — creates an implicit link table.

### Link (Foreign Key)
Use `Link` field type. Add `options: "Target DocType"` in JSON.

### Dynamic Link
Use `Dynamic Link` when the target DocType depends on another field value.
