# Copyright (c) 2026, NovaTech Solutions Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.tests import IntegrationTestCase
from frappe.utils import today, add_days, getdate, date_diff


class TestLeaveManagement(IntegrationTestCase):
	"""Tests for Section 6 - Leave Management."""

	def setUp(self):
		"""Set up test data."""
		self.employee = self._create_test_employee()
		self.leave_type = self._create_test_leave_type("Casual Leave")

	def tearDown(self):
		"""Clean up test data."""
		frappe.db.rollback()

	def _create_test_employee(self) -> str:
		"""Create a minimal test employee."""
		employee = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "_Test Leave Employee",
			"company": "_Test Company",
			"date_of_joining": add_days(today(), -365),
			"status": "Active",
		})
		employee.insert(ignore_permissions=True)
		return employee.name

	def _create_test_leave_type(self, name: str) -> str:
		"""Create a test leave type."""
		leave_type = frappe.get_doc({
			"doctype": "Leave Type",
			"leave_type_name": f"_Test {name}",
			"max_leaves_allowed": 10,
			"include_holiday": 0,
		})
		leave_type.insert(ignore_permissions=True)
		return leave_type.name

	def _create_leave_allocation(self, employee: str, leave_type: str, days: float = 10):
		"""Create a leave allocation for the employee."""
		allocation = frappe.get_doc({
			"doctype": "Leave Allocation",
			"employee": employee,
			"leave_type": leave_type,
			"from_date": add_days(today(), -30),
			"to_date": add_days(today(), 300),
			"new_leaves_allocated": days,
		})
		allocation.insert(ignore_permissions=True)
		allocation.submit()
		return allocation

	def _create_leave_application(
		self,
		employee: str,
		leave_type: str,
		from_date: str,
		to_date: str,
		reason: str = "Test leave",
		status: str = "Open",
	) -> dict:
		"""Helper to create a leave application."""
		doc = frappe.get_doc({
			"doctype": "Leave Application",
			"employee": employee,
			"leave_type": leave_type,
			"from_date": from_date,
			"to_date": to_date,
			"description": reason,
			"status": status,
			"company": "_Test Company",
		})
		doc.insert(ignore_permissions=True)
		return doc

	# === Tests ===

	def test_leave_application_can_be_created(self):
		"""Verify a basic leave application can be created with all required fields."""
		self._create_leave_allocation(self.employee, self.leave_type)
		from_date = today()
		to_date = today()

		leave = self._create_leave_application(
			self.employee, self.leave_type, from_date, to_date
		)

		self.assertEqual(leave.employee, self.employee)
		self.assertEqual(leave.leave_type, self.leave_type)
		self.assertEqual(leave.from_date, getdate(from_date))
		self.assertEqual(leave.to_date, getdate(to_date))
		self.assertEqual(leave.description, "Test leave")
		self.assertEqual(leave.status, "Open")
		self.assertIsNotNone(leave.name)

	def test_total_leave_days_excludes_off_days(self):
		"""Verify off-days (holidays/weekly offs) are not counted in total_leave_days.

		When a Leave Type has include_holiday=0, the standard HRMS system
		subtracts all holidays (including weekly offs) from the total leave
		days count.
		"""
		self._create_leave_allocation(self.employee, self.leave_type)

		# Create a Monday-Friday leave application
		# Assuming the holiday list has Saturday-Sunday as weekly offs
		from_date = "2026-08-03"  # Monday
		to_date = "2026-08-09"    # Sunday

		leave = self._create_leave_application(
			self.employee, self.leave_type, from_date, to_date
		)

		# total_leave_days should be less than 7 (the full date range)
		# because off-days (Sat-Sun) are excluded
		total_days = date_diff(getdate(to_date), getdate(from_date)) + 1
		self.assertLess(
			leave.total_leave_days,
			total_days,
			"Off-days should be excluded from total leave days",
		)
		self.assertGreater(
			leave.total_leave_days, 0, "There should be at least 1 working day"
		)

	def test_duplicate_leave_application_is_prevented(self):
		"""Verify an employee cannot create duplicate leave for the same date range.

		This tests the standard HRMS validate_leave_overlap() which checks
		for overlapping leave applications.
		"""
		self._create_leave_allocation(self.employee, self.leave_type)
		from_date = add_days(today(), 7)
		to_date = add_days(today(), 9)

		# Create first leave application
		self._create_leave_application(
			self.employee, self.leave_type, from_date, to_date
		)

		# Attempt to create a second overlapping leave application
		with self.assertRaises(frappe.ValidationError):
			self._create_leave_application(
				self.employee, self.leave_type, from_date, to_date
			)

	def test_leave_balance_updates_on_submit(self):
		"""Verify leave balance updates automatically when leave is submitted.

		This tests the standard Leave Ledger Entry creation on submit.
		"""
		initial_leaves = 10
		self._create_leave_allocation(self.employee, self.leave_type, initial_leaves)

		from_date = add_days(today(), 14)
		to_date = add_days(today(), 14)

		leave = self._create_leave_application(
			self.employee, self.leave_type, from_date, to_date,
			status="Approved",
		)
		leave.submit()

		# Verify a Leave Ledger Entry was created
		ledger_entries = frappe.get_all(
			"Leave Ledger Entry",
			filters={
				"employee": self.employee,
				"leave_type": self.leave_type,
				"transaction_name": leave.name,
			},
		)
		self.assertGreater(len(ledger_entries), 0, "Leave Ledger Entry should be created on submit")

	def test_special_leave_requires_attachment(self):
		"""Verify Special Leave applications require an attachment."""
		special_leave = self._create_test_leave_type("Special Leave")
		self._create_leave_allocation(self.employee, special_leave)

		from_date = add_days(today(), 21)
		to_date = add_days(today(), 21)

		# Creating a Special Leave without attachment should fail
		with self.assertRaises(frappe.ValidationError):
			doc = frappe.get_doc({
				"doctype": "Leave Application",
				"employee": self.employee,
				"leave_type": special_leave,
				"from_date": from_date,
				"to_date": to_date,
				"description": "Special leave without attachment",
				"company": "_Test Company",
			})
			doc.insert(ignore_permissions=True)

	def test_leave_application_has_required_fields(self):
		"""Verify the Leave Application has all fields specified in requirements.

		Required fields per Section 6:
		- Employee
		- Leave Type
		- From Date
		- To Date
		- Total Days
		- Reason
		- Attachment
		- Approval Status
		- Approved By
		"""
		meta = frappe.get_meta("Leave Application")

		required_fieldnames = [
			"employee",       # Employee
			"leave_type",     # Leave Type
			"from_date",      # From Date
			"to_date",        # To Date
			"total_leave_days",  # Total Days
			"description",    # Reason
			"attachment",     # Attachment (custom field)
			"status",         # Approval Status
			"leave_approver",  # Approved By
		]

		for fieldname in required_fieldnames:
			field = meta.get_field(fieldname)
			self.assertIsNotNone(
				field,
				f"Field '{fieldname}' should exist on Leave Application",
			)

	def test_leave_types_exist(self):
		"""Verify the five required leave types are configured.

		Required leave types:
		- Casual Leave
		- Sick Leave
		- Earned Leave
		- Unpaid Leave
		- Special Leave
		"""
		required_types = [
			"Casual Leave",
			"Sick Leave",
			"Earned Leave",
			"Unpaid Leave",
			"Special Leave",
		]

		for leave_type_name in required_types:
			exists = frappe.db.exists("Leave Type", leave_type_name)
			if not exists:
				# Check with _Test prefix (might not have been created yet)
				exists = frappe.db.exists("Leave Type", f"_Test {leave_type_name}")
			if not exists:
				self.fail(f"Leave Type '{leave_type_name}' is not configured")
