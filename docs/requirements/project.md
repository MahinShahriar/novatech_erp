# Project Management Requirements

Project management is the core of our business operations. The system should allow us to manage the entire project lifecycle — from project creation after a sales order to final delivery — with full visibility into progress, budget, resources, and deadlines.

---

## 1. Main Scope

The project management module should cover:

* Project workspace creation
* Client information management
* Project team and role assignment
* Milestone planning
* Task breakdown and assignment
* Time tracking against tasks
* Progress tracking
* Budget and cost tracking
* Document and repository management
* Meeting notes
* Notifications for overdue tasks and deadlines
* Project dashboards and reports

Every project should be linked to a client (customer) and a sales order where applicable.

---

## 2. User Roles

The system should support these roles within the project management module:

* Project Manager
* Team Member (Software Engineer, UI/UX Designer, QA Engineer, DevOps Engineer)
* Management
* Client (read-only portal access)

Each role should see only what is relevant to them.

* Project Managers can create projects, assign tasks, manage milestones, track budgets, and view all project data
* Team Members can view assigned tasks, update task progress, log time, and add comments
* Management can view all projects, dashboards, and high-level reports
* Clients can view project progress, milestones, and deliverables through the client portal

---

## 3. Project Workspace

Once a sales order is confirmed, the system should automatically create a project workspace.

### 3.1 Project Fields

* Project Name
* Project ID (auto-generated)
* Client / Customer
* Sales Order Reference
* Project Manager
* Status (Planning, In Progress, On Hold, Completed, Cancelled)
* Priority (Low, Medium, High, Critical)
* Start Date
* Expected Completion Date
* Actual Completion Date
* Budget (in BDT/USD)
* Currency
* Description
* Source Code Repository URL
* Billing Type (Fixed Price, Hourly, Retainer, Non-Billable)

### 3.2 Project Team

Each project should have a defined team.

* Project Manager (one primary manager)
* Team Members (multiple employees from different departments)
* Role within Project (Tech Lead, Developer, Designer, QA, etc.)
* Allocation Percentage
* Start Date in Project
* End Date in Project

The system should allow adding and removing team members throughout the project lifecycle.

### 3.3 Project Documents

* Upload project-related documents
* Link to Google Drive or shared folders
* Version tracking for documents
* Document categories (Contracts, SOW, Technical Docs, Design Files, etc.)

---

## 4. Milestones

Projects should be divided into milestones for better tracking.

### Milestone Fields

* Milestone Title
* Description
* Start Date
* Due Date
* Status (Not Started, In Progress, Completed, Delayed)
* Project
* Linked Sales Order (if milestone-based billing)

Milestones represent major phases or deliverables of the project.

---

## 5. Task Management

Each milestone should contain one or more tasks. Tasks are the smallest unit of work.

### 5.1 Task Fields

* Task Title
* Description
* Project
* Milestone (optional)
* Assigned Employee
* Priority (Low, Medium, High, Urgent)
* Status (Open, In Progress, In Review, Rework, Completed, Cancelled)
* Estimated Hours
* Actual Hours
* Start Date
* Due Date
* Completed Date
* Dependencies (link to other tasks)
* Task Category (Development, Design, Testing, Deployment, Documentation, Meeting, Other)

### 5.2 Checklist

Each task should support a checklist for breaking down sub-steps.

* Checklist Item Text
* Checked / Unchecked
* Order / Sequence

### 5.3 Task Attachments

* File uploads
* Screenshots
* Reference links

### 5.4 Task Comments

Employees should be able to add comments to tasks.

* Comment Text
* Attachments
* Timestamp
* Comment Author
* Mentions (notify specific users)

### 5.5 Task Workflow

1. Project Manager or lead creates tasks and assigns them to team members
2. Assigned employee updates status as work progresses
3. Employee marks task as In Progress when starting work
4. Employee moves task to In Review when ready for review
5. Reviewer can move it back to Rework with comments
6. Employee marks task as Completed when finished
7. Project Manager is notified if a task becomes overdue

### 5.6 Task Progress

* Each task should have a progress percentage (0-100%)
* Progress can be updated manually or auto-calculated based on checklist completion
* The system should track time between status changes for analytics

---

## 6. Time Tracking

Every employee should log the time they spend on each task.

### 6.1 Time Log Fields

* Project
* Task
* Employee
* Date
* Start Time
* End Time
* Total Hours (auto-calculated)
* Break Time (optional)
* Billable Hours
* Description of Work Done
* Overtime (auto-detected if applicable)

### 6.2 Time Log Methods

* Manual entry (employee enters start/end time)
* Timer mode (employee clicks start/stop)
* Weekly timesheet view for bulk entry

### 6.3 Timesheet Approval

* Employees submit timesheets weekly or bi-weekly
* Project Manager reviews and approves timesheets
* Finance uses approved hours for billing and payroll
* Rejected timesheets should include a reason and allow resubmission

### 6.4 Estimated vs Actual

The system should provide a comparison of estimated hours vs actual hours:

* Per task
* Per milestone
* Per project
* Per employee

Variance should be highlighted when actual hours exceed estimated hours by more than a configurable threshold.

---

## 7. Budget & Cost Tracking

The system should track project financials.

### Budget Fields

* Total Project Budget
* Budget by Category (Development, Design, Testing, Infrastructure, Misc)
* Currency

### Cost Tracking

* Employee Cost (based on logged hours × hourly rate)
* Expense Cost (linked from expense management)
* Total Cost Incurred
* Remaining Budget
* Budget Utilization Percentage

### Billing

* Billing Method (Fixed Price, Hourly, Non-Billable)
* For hourly projects, billable amount = billable hours × billing rate
* Track invoiced amount against project
* Track pending billing

---

## 8. Progress Tracking

The system should provide real-time visibility into project progress.

### Project Level

* Overall project completion percentage
* Completed vs pending milestones
* Budget consumed
* Remaining budget
* Days elapsed vs total days
* Delayed milestones and tasks

### Milestone Level

* Milestone completion percentage
* Tasks completed vs total
* Days remaining

### Task Level

* Task status
* Hours logged vs estimated
* Days overdue

---

## 9. Meeting Notes

Project meetings should be recorded in the system.

### Meeting Fields

* Project
* Meeting Title
* Date & Time
* Meeting Link / Location
* Attendees
* Agenda
* Minutes / Notes
* Action Items
* Next Meeting Date

Action items from meetings should be convertible to tasks.

---

## 10. Project Closure

When a project is completed, the system should support a closure process.

### Closure Checklist

* All milestones completed
* All tasks closed
* Timesheets approved
* Final invoice generated
* All deliverables handed over
* Client sign-off received
* Project documentation archived
* Team released from project

### Post-Closure

* Project status set to Completed
* Actual completion date recorded
* Final budget vs actual report generated
* Project moved to read-only state
* Client portal access maintained for historical view

---

## 11. Notifications

The system should send notifications for the following project events:

* New project assigned
* Task assigned
* Task status changed
* Task overdue
* Milestone approaching deadline
* Milestone overdue
* Comment added on assigned task
* Timesheet submitted for approval
* Timesheet approved or rejected
* Project budget exceeded threshold
* Project completion

Notifications should be sent as in-app alerts and email where configured.

---

## 12. Reports & Dashboards

### Project Dashboard (per project)

* Project progress bar
* Milestone Gantt-style view
* Task breakdown by status
* Hours logged vs estimated
* Budget consumed vs remaining
* Recent activity feed
* Overdue tasks list

### Management Dashboard (all projects)

* Active projects count
* Project status distribution
* Delayed projects
* Overall budget utilization
* Resource allocation across projects
* Revenue per project
* Profitability per project

### Individual Dashboard (per employee)

* My assigned tasks
* Tasks due this week
* Overdue tasks
* Hours logged today / this week
* Pending timesheet submission

---

## 13. Additional Requirements

* Tasks should be searchable and filterable by project, assignee, status, priority, and date range
* Bulk assign tasks to team members
* Reorder tasks within milestones via drag and drop
* Export project reports to PDF and Excel
* Google Calendar sync for task due dates and milestones
* Gantt chart view for project timeline
* Kanban board view for task management
* REST API for project and task CRUD operations
* Print project summary as PDF
* Role-based visibility — clients should only see their own projects with limited information
