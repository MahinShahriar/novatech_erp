# HR Department Requirements

We need a simple HR module for managing employee records and day-to-day HR work without too much data entry.

The goal is to keep the system clean, practical, and easy for HR staff, managers, and employees to use.

---

## 1. Main HR Scope

The HR module should cover only the essentials:

* Employee master record
* Department and designation setup
* Branch / office setup
* Attendance
* Leave management
* Holiday calendar (per branch)
* Employee onboarding and exit
* Inter-branch transfer
* Basic document storage
* Simple HR reports
* HR dashboard

The system should stay simple and should not require repeated manual entry for the same information.

---

## 2. User Roles

The system should support these basic roles:

* HR Manager
* HR User (can be branch-specific — HR users at one branch see only that branch)
* Department Manager
* Employee
* Management

Permissions should be role-based.

* HR can create and update HR records (optionally scoped to a specific branch)
* Managers can approve leave and attendance corrections only for their teams
* Employees can view their own profile, attendance, leave balance, and requests
* Management can view summaries and reports across all branches

---

## 3. Employee Record

Each employee should have one profile with the most important information only.

### Required Fields

* Employee ID
* Full Name
* Department
* Designation
* Joining Date
* Email Address



### Optional Fields
* Reporting Manager
* Present Address
* Phone Number
* Emergency Contact Name
* Emergency Contact Phone
* Photo
* Date of Birth
* Gender
* National ID / Passport Number
* Blood Group
* Marital Status
* Employee Type
* Shift
* Basic Salary
* Work Station / Desk Location (if on-site)

The system should allow file attachments for important documents.

---

## 4. Common HR Workflow

The normal HR flow should be simple.

1. HR creates the employee profile
2. HR collects basic documents
3. HR assigns department, designation, office/branch, and manager
4. Employee starts attendance tracking
5. Employee submits leave requests when needed, even create application after taking leave
6. Manager reviews and approves requests, and HR submits, cancel
7. HR updates employee changes such as transfer, promotion, inter-branch move, or resignation
8. HR keeps records for future reference

The system should support inter-branch and inter-office transfers without losing employee history.

The system should keep the history of major changes in the employee profile.

---

## 5. Attendance

Attendance should support the common cases only.

### Attendance Methods

* Manual attendance entry
* Biometric import (per branch office)
* Web or mobile check-in with GPS location capture
* Work from home attendance
* IP-based check-in verification for office networks


### Attendance Fields

* Employee
* Date
* Check-in Time
* Check-out Time
* Working Hours
* Actual Working Hours
* Attendance Method (Biometric, Mobile GPS, Web, Manual, WFH)
* Status
* Remarks (must need in attendance correction)

### Attendance Actions

* Mark present, absent, late, leave, work from home, and holiday
* Allow attendance correction request
* Allow manager approval for corrections

---

## 6. Leave Management

Leave should be easy to apply and easy to approve.

### Leave Types

* Casual Leave
* Sick Leave
* Earned Leave
* Unpaid Leave
* Special Leave

### Leave Request Fields

* Employee
* Leave Type
* From Date
* To Date
* Total Days
* Reason
* Approval Status
* Approved By

### Leave Workflow

1. Employee submits leave request
2. Manager reviews request
3. HR checks leave balance if needed
4. Request is approved or rejected
5. Leave balance updates automatically

Employees should be able to see their leave balance and leave history.
employee cant create duplicate leave application for any single day , and leave application is date range than off-days shouldn't count .  

---

## 7. Holiday Calendar

The HR team should maintain a holiday list.

### Holiday Fields

* Holiday Name
* Date
* Holiday Type
* Applicable Branch / Office (all branches or specific branch)
* Remarks

The system should also support weekly off days. (default, fri, sat) 


---

## 8. Onboarding And Exit

The system should support a simple employee start and exit process.

### Onboarding

* Create employee profile
* Upload basic documents
* Assign department, designation, and branch/office
* Assign reporting manager
* Issue office assets (laptop, ID card, access card, etc.) if applicable
* Mark employee as active

### Exit

* Record resignation or termination
* Capture last working date
* Record reason for exit
* Collect office assets before final settlement
* Mark employee as inactive

The employee record should remain in the system after exit.

### Inter-Branch Transfer

* Record transfer from one branch/office to another
* Capture transfer date and reason
* Update reporting manager if changed
* Update shift, work location, and branch-specific settings
* Keep full history of previous assignments
* Notify relevant HR teams at both branches

---

## 9. Documents

HR should be able to store common employee documents.

### Common Document Types

* NID or Passport
* CV
* Offer Letter
* Appointment Letter
* Contract
* Educational Certificate
* Resignation Letter
* Clearance Form

The system should allow document search by employee and document type.

---

## 10. Common Reports

The system should provide the reports HR uses most often.

### Required Reports

* Employee List
* Active Employee List
* Department-wise Employee Report
* Designation-wise Employee Report
* Joining Report
* Attendance Summary Report
* Monthly Attendance Register (day-by-day attendance per employee for a given month)
* Late Attendance Report
* Absent Report
* Leave Balance Report
* Leave Summary Report
* Pending Leave Approval Report
* Holiday Report
* Document List Report
* Expiring Document Report (contracts, visas, and other documents nearing expiry)
* Exit Report
* Employee Turnover Report (joinings vs exits over a period)
* Payroll Register / Salary Register (monthly payroll summary for all employees)

Reports should support filtering by date range, department, designation, employee, branch/office, and status.

---

## 11. Custom Reports

The system should allow simple custom reports without coding when possible.

---

## 12. Payroll

Payroll should be generated monthly based on employee attendance, leave, and salary structure.

### Payroll Components

The system should calculate:

* Basic Salary
* Allowances
* Overtime
* Bonuses
* Deductions
* Taxes
* Provident Fund
* Net Salary

### Payroll Process

1. HR sets up salary structures for each employee (may vary by branch/location)
2. System pulls attendance, leave, and overtime data for the month
3. System calculates earnings and deductions automatically
4. HR reviews and adjusts if needed
5. Payroll is finalized and salary slips are generated
6. Finance processes the payment

The system should support branch-wise payroll processing — each branch can have separate payroll runs if needed.

### Salary Slip

Each salary slip should include:

* Employee Name and ID
* Department and Designation
* Pay Period
* Earnings (Basic, Allowances, Overtime, Bonuses)
* Deductions (Tax, Provident Fund, Other Deductions)
* Net Pay
* Leave Summary for the month

Salary slips should be downloadable as PDF and accessible to employees through self-service.

### Custom Report Needs

* Choose columns
* Apply filters
* Group by department or status
* Sort by date or name
* Export to Excel or PDF

### Example Custom Reports

* Employees with no attendance in the last 30 days
* Employees with pending leave requests
* Employees on probation if probation is used
* Documents expiring soon
* Employees with repeated late arrival

---

## 12. HR Dashboard

The HR dashboard should show the most important data at a glance.

### Overview Cards

* Total Employees
* Active Employees
* Pending Leave Requests
* Absent Today
* Upcoming Holidays
* Documents Expiring Soon

### Required Charts

* Employee count by department
* Employee count by designation
* Monthly joining trend
* Monthly leave trend
* Monthly attendance status trend
* Exit trend

### Dashboard Tables

* Pending leave approvals
* Recent joins
* Recent exits
* Attendance exceptions
* Documents expiring soon

The dashboard should update automatically and support basic filters such as date range, branch/office, and department.

---

## 13. Simple Rules

The HR system should follow these rules:

* Keep forms short
* Avoid duplicate data entry
* Use clear statuses such as Draft, Pending, Approved, Rejected, Active, and Inactive
* Keep an audit trail for important changes
* Support file upload
* Support Excel and PDF export

The main goal is to manage HR work simply, with minimum typing and maximum clarity.
