# Copyright (c) 2026, NovaTech Solutions Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import getdate, date_diff, flt

from hrms.hr.doctype.leave_application.leave_application import (
	get_number_of_leave_days,
	get_leave_balance_on,
	is_lwp,
)


def validate(doc, method):
	"""NovaTech-specific validations for Leave Application.

	Runs after standard HRMS Leave Application validation.
	Extends the standard with additional business rules.
	"""
	validate_off_days_excluded(doc)
	validate_attachment_for_special_leave(doc)


def validate_off_days_excluded(doc):
	"""Ensure off-days (holidays/weekly offs) are not counted as leave days.

	The standard HRMS Leave Application already excludes holidays from
	total_leave_days when the Leave Type has 'Include holidays within leaves
	as leaves' unchecked (include_holiday=0). This validation serves as a
	safety net to ensure off-days are never counted, regardless of Leave
	Type configuration.

	If a Leave Type has include_holiday=1, the system will show a warning so
	the administrator can correct the configuration.
	"""
	if not doc.leave_type or not doc.from_date or not doc.to_date:
		return

	include_holiday = frappe.db.get_value(
		"Leave Type", doc.leave_type, "include_holiday"
	)

	if flt(include_holiday):
		frappe.msgprint(
			_(
				"Off-days (holidays/weekly offs) within the leave period will be"
				" counted as leave days for {0}. To exclude off-days, disable"
				" 'Include holidays within leaves as leaves' in the Leave Type."
			).format(frappe.bold(doc.leave_type)),
			title=_("Off-Day Counting"),
			indicator="orange",
		)


def validate_attachment_for_special_leave(doc):
	"""Require attachment for Special Leave applications."""
	if doc.leave_type != "Special Leave":
		return

	if not doc.attachment:
		frappe.throw(
			_("Attachment is required for Special Leave applications."),
			title=_("Missing Attachment"),
		)
