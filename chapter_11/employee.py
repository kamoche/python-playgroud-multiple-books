class Employee:
    """Represent employee details"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annaul_salary = annual_salary

    def get_raise(self, salary_raise=5000):
        self.annaul_salary += salary_raise
