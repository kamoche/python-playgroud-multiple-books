import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test class for an Employee class"""

    def setUp(self):
        self.employee = Employee('Kamoche', 'Jackson', 1000000)

    def test_give_default_raise(self):
        self.employee.get_raise()
        self.assertEqual(1005000, self.employee.annaul_salary)

    def test_give_custom_raise(self):
        self.employee.get_raise(10000)
        self.assertEqual(1010000,self.employee.annaul_salary)


unittest.main()
