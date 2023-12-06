# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of unit tests for presentation classes
# ChangeLog: (Who, When, What)
# Rabiya Wasiq,12/1/2023,Created Script
# -------------------------------------


import builtins
import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

class TestIO(unittest.TestCase):

    def test_input_menu_choice(self):
        with patch('builtins.input',return_value='2'):
            choice=IO.input_menu_choice()
            self.assertEqual('2',choice)

    def test_input_invalid_menu_choice(self):
        with patch('builtins.input', return_value='two'):
            choice=IO.input_menu_choice()
            self.assertEqual(False,choice)


    def test_input_employee_data(self):
        with patch('builtins.input', side_effect=["Eve","Brown","2023-12-10","4"]):
            employees :list[Employee]= []
            employees = IO.input_employee_data(employee_data=employees,employee_type=Employee)
            self.assertEqual(1,len(employees))
            self.assertEqual('Eve',employees[0].first_name)
            self.assertEqual('Brown',employees[0].last_name)
            self.assertEqual('2023-12-10',employees[0].review_date)
            self.assertEqual(4,employees[0].review_rating)

    def test_input_employee_data_invalid_date(self):
        with patch('builtins.input', side_effect=["Eve", "Brown", "Dec 10, 2023", "4"]):
            employees: list[Employee] = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
            self.assertEqual(0, len(employees))


if __name__ == '__main__':
    unittest.main()
