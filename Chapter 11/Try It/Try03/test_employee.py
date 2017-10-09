import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """Test the employee.py functionality"""

    def setUp(self):
        self.salary = 70000
        self.employee = Employee('dom', 'torr', self.salary)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, self.salary + 5000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, self.salary + 10000)


unittest.main()
