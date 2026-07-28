# HR Department Requirements

We need a simple HR module for managing employee records and day-to-day HR work without too much data entry.

The goal is to keep the system clean, practical, and easy for HR staff, managers, and employees to use.

---

## 1. Main HR Scope

The HR module should cover only the essentials:

* Employee master record
* Department and designation setup
* Attendance
* Leave management
* Holiday calendar
* Employee onboarding and exit
* Basic document storage
* Simple HR reports
* HR dashboard

The system should stay simple and should not require repeated manual entry for the same information.

---

## 2. User Roles

The system should support these basic roles:

* HR Manager
* HR Officer
* Department Manager
* Employee
* Management

Permissions should be role-based.

* HR can create and update HR records
* Managers can approve leave and attendance corrections for their teams
* Employees can view their own profile, attendance, leave balance, and requests
* Management can view summaries and reports

---

## 3. Employee Record

Each employee should have one profile with the most important information only.

### Required Fields

* Employee ID
* Full Name
* Department
* Designation
* Reporting Manager
* Joining Date
* Employment Status
* Phone Number
* Email Address
* Present Address
* Emergency Contact Name
* Emergency Contact Phone
* Photo

### Optional Fields

* Date of Birth
* Gender
* National ID / Passport Number
* Blood Group
* Marital Status
* Employee Type
* Work Location
* Shift
* Basic Salary

The system should allow file attachments for important documents.

---

## 4. Common HR Workflow

The normal HR flow should be simple.

1. HR creates the employee profile
2. HR collects basic documents
3. HR assigns department, designation, and manager
4. Employee starts attendance tracking
5. Employee submits leave requests when needed
6. Manager reviews and approves requests
7. HR updates employee changes such as transfer, promotion, or resignation
8. HR keeps records for future reference

The system should keep the history of major changes in the employee profile.

---

## 5. Attendance

Attendance should support the common cases only.

### Attendance Methods

* Manual attendance entry
* Biometric import
* Web or mobile check-in if available
* Work from home attendance

### Attendance Fields

* Employee
* Date
* Check-in Time
* Check-out Time
* Working Hours
* Late Minutes
* Overtime Hours
* Status
* Remarks

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
* Attachment
* Approval Status
* Approved By

### Leave Workflow

1. Employee submits leave request
2. Manager reviews request
3. HR checks leave balance if needed
4. Request is approved or rejected
5. Leave balance updates automatically

Employees should be able to see their leave balance and leave history.

---

## 7. Holiday Calendar

The HR team should maintain a holiday list.

### Holiday Fields

* Holiday Name
* Date
* Holiday Type
* Remarks

The system should also support weekly off days.

---

## 8. Onboarding And Exit

The system should support a simple employee start and exit process.

### Onboarding

* Create employee profile
* Upload basic documents
* Assign department and designation
* Assign reporting manager
* Mark employee as active

### Exit

* Record resignation or termination
* Capture last working date
* Record reason for exit
* Mark employee as inactive

The employee record should remain in the system after exit.

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
* Late Attendance Report
* Absent Report
* Leave Balance Report
* Leave Summary Report
* Pending Leave Approval Report
* Holiday Report
* Document List Report
* Exit Report

Reports should support filtering by date range, department, designation, employee, and status.

---

## 11. Custom Reports

The system should allow simple custom reports without coding when possible.

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
* New Joinees This Month
* Pending Leave Requests
* Absent Today
* Late Arrivals Today
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

The dashboard should update automatically and support basic filters such as date range and department.

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
