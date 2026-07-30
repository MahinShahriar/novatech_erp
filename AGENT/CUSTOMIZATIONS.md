# Current Customizations

> Track all customizations on standard DocTypes here. Update this file whenever a new customization is added.

## Employee (`employee.json`)

**17 custom fields** — mostly reorganized from HRMS defaults plus 2 Novatech-specific fields.

### Novatech-Specific Fields

| Field | Type | Module | Purpose |
|-------|------|--------|---------|
| `national_id` | Data | Novatech HR | National ID number (after passport_number) |
| `workstation` | Data | Novatech HR | Physical workstation location (e.g. "Floor 2, Desk 2B") |

### Reorganized Fields (Moved to Custom Section)

These fields exist in standard Employee but are reorganized into a Novatech section:

| Field | Type | Purpose |
|-------|------|---------|
| `approvers_section` | Section Break | Approvers grouping |
| `default_shift` | Link → Shift Type | Default shift assignment |
| `employee_advance_account` | Link → Account | Advance account |
| `employment_type` | Link → Employment Type | Employment classification |
| `expense_approver` | Link → Employee | Expense approval chain |
| `grade` | Link → Employee Grade | Pay grade |
| `health_insurance_no` | Data | Insurance policy number |
| `health_insurance_provider` | Data | Insurance company name |
| `job_applicant` | Link → Job Applicant | Source applicant |
| `leave_approver` | Link → Employee | Leave approval chain |
| `payroll_cost_center` | Link → Cost Center | Payroll cost allocation |
| `shift_request_approver` | Link → Employee | Shift request approval |

---

## Attendance (`attendance.json`)

**3 custom fields**

| Field | Type | Options/Details |
|-------|------|----------------|
| `branch` | Link → Branch | `fetch_from: employee.branch`, read_only, in_list_view, standard_filter |
| `attendance_method` | Select | `Biometric\nMobile GPS\nWeb\nManual\nWork From Home` |
| `remarks` | Small Text | Required when attendance is amended |

---

## Employee Checkin (`employee_checkin.json`)

**1 custom field**

| Field | Type | Details |
|-------|------|---------|
| `ip_address` | Data | read_only — auto-captured from request |

---

## Shift Type (`shift_type.json`)

**Permission changes only** (no custom fields)

| Role | Read | Write | Create | Delete | Other |
|------|------|-------|--------|--------|-------|
| HR Manager | ✅ | ✅ | ✅ | ✅ | Full access |
| HR User | ✅ | ✅ | ✅ | ❌ | export, email, print, report, share |
| Employee | ✅ | ❌ | ❌ | ❌ | select only |
| Employee Self Service | ❌ | ❌ | ❌ | ❌ | select only |
| System Manager | ✅ | ✅ | ❌ | ❌ | email, print, report, share |

---

---

## Leave Application (`leave_application.json`)

**1 custom field**

| Field | Type | Details |
|-------|------|---------|
| `attachment` | Attach | Dedicated file upload field, placed after Reason (description). Supports document uploads (medical certificates, approval letters, etc.) |

### Validation Hooks

Defined in `novatech_erp/novatech_erp/hr/leave_validations.py`:

| Validation | Description |
|-----------|-------------|
| `validate_off_days_excluded` | Warns if Leave Type has `include_holiday=1`, which would cause off-days to be counted as leave days |
| `validate_attachment_for_special_leave` | Requires attachment for Special Leave applications |

Registered via `hooks.py`:
```python
doc_events = {
	"Leave Application": {
		"validate": "novatech_erp.novatech_erp.hr.leave_validations.validate",
	},
}
```

---

## Adding New Customizations

When adding a new customization:

1. Create/update the JSON file in `novatech_erp/novatech_erp/custom/`
2. Update this document with the new field details
3. Run `bench migrate` to apply
4. Verify with `bench console`:
   ```python
   frappe.get_meta("DocType Name").get_field("field_name")
   ```
