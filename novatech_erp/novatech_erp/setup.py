# Copyright (c) 2026, NovaTech Solutions Ltd. and contributors
# For license information, please see license.txt

"""Setup utilities for NovaTech ERP.

Run after app installation to create default data like Leave Types.
"""

import frappe
from frappe import _


def after_install():
	"""Run after app installation to set up default data."""
	create_default_leave_types()


def create_default_leave_types():
	"""Create the five default leave types required by the HR module.

	These are the standard leave types defined in the business requirements.
	If a leave type already exists (e.g., from a previous run or manual
	creation), it is skipped.
	"""
	default_leave_types = [
		{
			"leave_type_name": "Casual Leave",
			"max_leaves_allowed": 10,
			"max_continuous_days_allowed": 5,
			"include_holiday": 0,
			"allow_negative": 0,
			"is_carry_forward": 0,
			"is_lwp": 0,
			"is_optional_leave": 0,
			"is_compensatory": 0,
		},
		{
			"leave_type_name": "Sick Leave",
			"max_leaves_allowed": 14,
			"max_continuous_days_allowed": 7,
			"include_holiday": 0,
			"allow_negative": 0,
			"is_carry_forward": 0,
			"is_lwp": 0,
			"is_optional_leave": 0,
			"is_compensatory": 0,
		},
		{
			"leave_type_name": "Earned Leave",
			"max_leaves_allowed": 20,
			"max_continuous_days_allowed": 15,
			"include_holiday": 0,
			"allow_negative": 0,
			"is_carry_forward": 1,
			"maximum_carry_forwarded_leaves": 10,
			"is_lwp": 0,
			"is_optional_leave": 0,
			"is_earned_leave": 1,
			"earned_leave_frequency": "Monthly",
			"rounding": "1.0",
		},
		{
			"leave_type_name": "Unpaid Leave",
			"max_leaves_allowed": 0,
			"max_continuous_days_allowed": 30,
			"include_holiday": 0,
			"allow_negative": 1,
			"is_carry_forward": 0,
			"is_lwp": 1,
			"is_optional_leave": 0,
			"is_compensatory": 0,
		},
		{
			"leave_type_name": "Special Leave",
			"max_leaves_allowed": 0,
			"max_continuous_days_allowed": 30,
			"include_holiday": 0,
			"allow_negative": 1,
			"is_carry_forward": 0,
			"is_lwp": 0,
			"is_optional_leave": 0,
			"is_compensatory": 0,
		},
	]

	for leave_type_data in default_leave_types:
		name = leave_type_data["leave_type_name"]
		if frappe.db.exists("Leave Type", name):
			continue

		doc = frappe.get_doc({"doctype": "Leave Type", **leave_type_data})
		doc.flags.ignore_permissions = 1
		doc.insert()
		frappe.msgprint(_("Leave Type '{0}' created.").format(name))
