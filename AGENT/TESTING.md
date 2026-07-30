# Testing Strategy

## Framework

Frappe uses Python's `unittest` framework with custom test helpers.

## Test File Location

```
doctype/<name>/test_<name>.py
```

## Test Structure

```python
import frappe
from frappe.tests import IntegrationTestCase
from frappe.utils import today

class TestProjectMilestone(IntegrationTestCase):
    """Tests for Project Milestone DocType."""

    def test_milestone_requires_project(self):
        """Milestone must have a project linked."""
        milestone = frappe.get_doc({
            "doctype": "Project Milestone",
            "milestone_name": "Test Milestone",
        })
        self.assertRaises(frappe.exceptions.MandatoryError, milestone.insert)

    def test_progress_calculation(self):
        """Progress updates based on completed tasks."""
        project = create_test_project()
        milestone = create_test_milestone(project.name)
        milestone.completed_tasks = 5
        milestone.total_tasks = 10
        milestone.save()
        self.assertEqual(milestone.progress, 50)

    def test_date_validation(self):
        """End date cannot be before start date."""
        milestone = frappe.get_doc({
            "doctype": "Project Milestone",
            "milestone_name": "Date Test",
            "project": create_test_project().name,
            "start_date": "2026-12-31",
            "end_date": "2026-01-01",
        })
        self.assertRaises(frappe.ValidationError, milestone.insert)
```

## Running Tests

```bash
# Run all tests for an app
bench --site novatech.localhost run-tests --app novatech_erp

# Run tests for a specific DocType
bench --site novatech.localhost run-tests --doctype "Project Milestone"

# Run a single test file
bench --site novatech.localhost run-tests --module novatech_erp.doctype.project_milestone.test_project_milestone

# Verbose output
bench --site novatech.localhost run-tests --app novatech_erp -v
```

## Test Best Practices

| Rule | Why |
|------|-----|
| Use `IntegrationTestCase` | Sets up test site, cleans up after |
| Create test data in `setUp` | Consistent state per test |
| Clean up in `tearDown` | No test pollution |
| Use `self.assert*` methods | Clear failure messages |
| Test one thing per method | Isolated, diagnosable failures |
| Name tests descriptively | `test_leave_approval_sends_email` not `test1` |

## Test Data Helpers

```python
from frappe.tests import IntegrationTestCase
from frappe.utils import today, add_days

def create_test_project():
    """Create a minimal test project."""
    return frappe.get_doc({
        "doctype": "Project",
        "project_name": "Test Project",
        "company": "_Test Company",
        "expected_start_date": today(),
    }).insert(ignore_permissions=True)
```

## CI Integration

Tests run automatically via `.github/workflows/ci.yml`:
- **MariaDB 11.8**
- **Python 3.14**
- **Node 24**
- Runs `bench run-tests` for the app

## Coverage Goal

- Aim for tests on all DocType controllers
- Test mandatory field validation
- Test business rule enforcement
- Test API endpoint access control
- Test edge cases and error paths
