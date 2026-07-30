# HR Module — User Guide

## Employee Management

### What It Does
Store and manage all employee information — personal details, job details, documents, and approver assignments.

### Who Uses It
- **HR Manager**: Full access to create, edit, and delete employee records.
- **HR User**: Can create and edit employees.
- **Employee**: Can view own profile only.

### Prerequisites
- Company must be set up in the system.
- Departments, Designations, and Grades must exist.

### How to Use

1. Go to **HR → Employee → New**.
2. Fill in required fields: Employee Name, Company, Department, Designation, Date of Birth, Date of Joining.
3. Fill in **Novatech-specific fields**:
   - **National ID**: Enter the employee's national identification number.
   - **Workstation**: Enter physical location (e.g., "Floor 2, Desk 2B").
4. Assign approvers:
   - **Leave Approver**: Employee who approves leave requests.
   - **Expense Approver**: Employee who approves expense claims.
   - **Shift Request Approver**: Employee who approves shift changes.
5. Click **Save**.

### Related DocTypes
- Employee, Department, Designation, Grade, Employment Type, Branch

---

## Attendance

### What It Does
Track daily attendance for employees using multiple methods.

### Who Uses It
- **HR Manager / HR User**: Can mark and manage attendance for all employees.
- **Employee**: Can mark own attendance (Web/Manual methods).

### Attendance Methods

| Method | How It Works |
|--------|-------------|
| **Biometric** | Auto-captured from biometric device via Employee Checkin |
| **Mobile GPS** | Captured from mobile app with location |
| **Web** | Employee marks attendance via web portal |
| **Manual** | HR staff manually enters attendance |
| **Work From Home** | Employee working remotely |

### How to Use

1. Go to **HR → Attendance → New**.
2. Select **Employee** — branch auto-fills.
3. Choose **Attendance Method** from the dropdown.
4. Set **Status**: Present, Absent, Half Day, or On Leave.
5. Add **Remarks** if correcting a previous attendance.
6. Click **Save**.

### Key Fields

| Field | Description |
|-------|------------|
| **Branch** | Auto-filled from employee record (read-only) |
| **Attendance Method** | How attendance was captured |
| **Remarks** | Required when amending attendance |

---

## Leave Management

### What It Does
Manage employee leave requests, approvals, and balances. Employees can apply for leave, managers can review and approve, and HR can configure leave types and allocations.

### Business Problem
Manual leave tracking leads to confusion, duplicate records, and inaccurate balance calculations. This system provides a structured workflow where employees apply online, managers approve digitally, and leave balances update automatically.

### Who Can Use It

| Role | Capabilities |
|------|-------------|
| **Employee** | Apply for leave, view own leave balance and history, cancel own open requests |
| **Department Manager** | Review and approve/reject leave for team members |
| **HR Manager** | Full access — create/edit leave types, allocate leave, approve/reject, cancel, view all records |
| **HR User** | Create and edit leave applications, view all records |
| **Leave Approver** | Approve/reject leaves assigned to them |

### Prerequisites

Before using leave management:
1. **Leave Types** must be created (Casual, Sick, Earned, Unpaid, Special)
2. **Leave Allocation** must be assigned to each employee (with leave period)
3. **Holiday List** must be configured with weekly offs and public holidays
4. **Leave Approver** must be set on each employee record
5. **HR Settings** must be configured (e.g., leave notification, backdated leave rules)

### Leave Types

The system supports five leave types by default:

| Leave Type | Code | Description | Default Max per Year | Carry Forward |
|-----------|------|-------------|---------------------|---------------|
| Casual Leave | CL | Short-term personal leave (urgent matters, family events) | 10 | No |
| Sick Leave | SL | Medical/health-related leave (with or without medical certificate) | 14 | No |
| Earned Leave | EL | Accumulated annual leave earned over time | As per policy | Yes (limited) |
| Unpaid Leave | LWP | Leave without pay — taken when no other leave balance remains | No limit | N/A |
| Special Leave | — | Leave for special circumstances requiring management approval | As approved | N/A |

Each leave type can be configured in **HR → Leave Type** with:
- Maximum leaves allowed per period
- Minimum calendar days since joining before eligible
- Maximum consecutive days allowed
- Whether holidays are counted as leave days
- Whether negative balance is allowed
- Carry forward settings
- Encashment settings
- Earned leave accrual frequency

### Leave Request Fields

| Field | Description | Required |
|-------|-------------|----------|
| **Employee** | The employee requesting leave | Yes |
| **Employee Name** | Auto-filled from employee record | Auto |
| **Leave Type** | Type of leave being requested | Yes |
| **Company** | Auto-filled from employee record | Auto |
| **Department** | Auto-filled from employee record | Auto |
| **From Date** | First day of leave | Yes |
| **To Date** | Last day of leave | Yes |
| **Half Day** | Check if taking half-day leave | No |
| **Half Day Date** | Date of half-day (if applicable) | Conditional |
| **Total Leave Days** | Calculated automatically (excludes off-days) | Auto, Read-only |
| **Reason** | Why the leave is needed | No |
| **Attachment** | Upload supporting documents (medical cert, approval letter, etc.) | No |
| **Leave Approver** | Person who will review the request | Yes |
| **Status** | Open / Approved / Rejected / Cancelled | Auto |
| **Leave Balance** | Current balance before application | Auto, Read-only |

### How to Apply for Leave

**As an Employee (Self-Service):**

1. Go to **HR → Leave Application → New**.
2. Your employee record is automatically selected (if linked to your user account).
3. Select **Leave Type** (e.g., Casual Leave, Sick Leave).
4. Set **From Date** and **To Date**.
   - The system automatically calculates **Total Leave Days**, excluding off-days (weekly offs and holidays).
5. Enter **Reason** for the leave.
6. Attach any supporting documents (e.g., medical certificate for sick leave).
   - **Note**: Special Leave requires an attachment.
7. The **Leave Approver** is auto-selected from your employee record.
8. Click **Save**, then **Submit**.
   - Your leave approver receives a notification.
   - The leave status changes to **Open** (pending approval).

**As HR (On Behalf of Employee):**

1. Go to **HR → Leave Application → New**.
2. Select the **Employee**.
3. Follow steps 3–8 above.
4. You can also set status to **Approved** directly if pre-approved.

### How to Approve or Reject Leave

**As a Leave Approver or HR Manager:**

1. Go to **HR → Leave Application**.
2. Filter by **Status = Open** or use the **Pending Leave Approval** report.
3. Open a leave application to review.
4. Review the details:
   - Leave balance
   - Reason
   - Attachments
   - Date range
5. Click one of:
   - **Approve** — changes status to "Approved" (requires submitting the document).
   - **Reject** — changes status to "Rejected" (enter reason if needed).
6. The employee receives a notification about the decision.

### How to Cancel a Leave

- **Employee**: Can cancel own leave requests while status is **Open**.
- **HR Manager**: Can cancel **Approved** leaves if needed (e.g., employee returned early).

To cancel:
1. Open the Leave Application.
2. Click **Cancel** (Amend → Cancel).
3. The leave balance is automatically restored.

### How to Allocate Leave to Employees

1. Go to **HR → Leave Allocation → New**.
2. Select **Employee**.
3. Select **Leave Type**.
4. Set **From Date** and **To Date** (the leave period this allocation covers).
5. Enter **New Leaves Allocated** (e.g., 10 for Casual Leave).
6. Enable **Add unused leaves from previous allocations** if carry forward is applicable.
7. Click **Save**, then **Submit**.

### Business Workflow

```
Employee Submits Leave Request
        │
        ▼
Leave Status = "Open"
        │
        ▼
Manager Reviews Request
        │
    ┌───┴───┐
    ▼       ▼
Approved   Rejected
    │       │
    ▼       ▼
Leave balance   Leave balance
decrements      unchanged
    │       │
    ▼       ▼
Attendance     Employee
marked as      notified
"On Leave"
```

### System Behavior

| Event | System Action |
|-------|--------------|
| **Leave Application Created** | Dashboard shows updated allocated leaves; approver notified |
| **Leave Application Approved** | Leave balance decremented via Leave Ledger Entry; attendance marked as "On Leave" for each day in range; off-days (holidays/weekly offs) are skipped; employee notified |
| **Leave Application Rejected** | No balance change; employee notified |
| **Leave Application Cancelled** | Leave balance restored via reverse ledger entry; attendance records cancelled |
| **Leave Period Ends** | Unused leaves may expire or carry forward based on Leave Type configuration |

### Validations

| Rule | Where Enforced | Description |
|------|---------------|-------------|
| **No duplicate dates** | Standard HRMS | Cannot create overlapping leave applications for the same date range |
| **Off-days excluded** | Standard HRMS + NovaTech hook | Off-days (weekly offs, public holidays) are not counted in total leave days |
| **Leave balance check** | Standard HRMS | Cannot apply for more days than available balance (unless negative balance allowed) |
| **Backdated leave** | Standard HRMS | Optional restriction via HR Settings — only certain roles can create backdated leaves |
| **Applicable after days** | Standard HRMS | Leaves can be restricted until a minimum number of calendar days after joining |
| **Block dates** | Standard HRMS | Leaves cannot be applied/approved on blocked dates |
| **Special Leave attachment** | NovaTech hook | Attachment is required when applying for Special Leave |

### Related DocTypes

| DocType | Purpose |
|---------|---------|
| **Leave Type** | Defines leave categories and rules |
| **Leave Application** | Employee leave request record |
| **Leave Allocation** | Allocates leave balance to an employee for a period |
| **Leave Ledger Entry** | Tracks all leave transactions (allocation, application, encashment, expiry) |
| **Leave Period** | Defines a leave calendar period (e.g., Jan–Dec 2026) |
| **Leave Policy** | Groups multiple leave allocations into a policy |
| **Leave Policy Assignment** | Assigns a leave policy to an employee |
| **Holiday List** | Defines holidays and weekly offs used for off-day calculation |

### Configuration

**HR Settings affecting leave:**
- `send_leave_notification` — Enable/disable email notifications
- `restrict_backdated_leave_application` — Prevent backdated applications
- `role_allowed_to_create_backdated_leave_application` — Who can bypass backdate restriction

**Leave Type settings per type:**
- `include_holiday` — When **unchecked** (recommended), off-days are excluded from total leave days
- `allow_negative` — When checked, employees can apply leave exceeding their balance
- `is_lwp` — When checked, marks as Leave Without Pay
- `is_carry_forward` — Unused leaves carry forward to next period
- `applicable_after` — Minimum days after joining before this leave can be used

### Limitations

- Leave applications cannot span across two allocation periods (must be within same allocation)
- Half-day leaves are supported only as single days or as a specific date within a range
- Employee must have a Holiday List assigned for off-day calculation to work correctly

### Menu Path

| Action | Navigation |
|--------|-----------|
| Apply for Leave | HR → Leave Application → New |
| Approve/Reject Leaves | HR → Leave Application → filter by "Open" |
| View Leave Balance | HR → Leave Application → select employee → dashboard |
| Configure Leave Types | HR → Leave Type |
| Allocate Leave | HR → Leave Allocation → New |
| View Leave Reports | HR → Reports → Leave Balance / Leave Summary / Pending Leave Approval |

---

## Holiday Calendar

### What It Does
Define company holidays per branch. Employees on leave are automatically adjusted.

### How to Use

1. Go to **HR → Holiday List → New**.
2. Enter **Holiday List Name** and **Year**.
3. Add holidays with **Date**, **Description**, and **Weekly Off** flag.
4. Link the holiday list to the **Branch** in Settings.

---

## Payroll

### What It Does
Generate monthly salary slips and process payments.

### Who Uses It
- **HR Manager**: Can generate and submit salary slips.
- **HR User**: Can view salary slips.
- **Employee**: Can view own salary slip only.

### How to Generate Payroll

1. Go to **HR → Payroll Entry → New**.
2. Select **Company**, **Payroll Period**.
3. Add employees or select by department/filter.
4. Click **Create** to generate salary slips.
5. Review, then **Submit**.

---

## Document Storage

Employees can have documents attached: National ID copy, CV, offer letter, contract, etc.

### How to Use

1. Open the **Employee** record.
2. Scroll to **Documents** section.
3. Click **Attach** to upload files.
4. Select document type from dropdown.

---

## Reports

| Report | Purpose |
|--------|---------|
| Employee Details | Full employee listing with filters |
| Attendance | Daily/monthly attendance summary |
| Leave Balance | Current leave balances per employee |
| Salary Slip | Monthly salary slip listing |
| Headcount | Employee count by department/branch |
| Late Attendance | Employees who checked in late |
| Expense Claims | Pending and approved expenses |

Navigate to **HR → Reports** to access all reports.
