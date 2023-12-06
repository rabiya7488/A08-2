# ------------------------------------------------------------------------------------------------- #
# Title: Data Classes
# # Description: A collection of unit tests for data classes
# ChangeLog: (Who, When, What)
# Rabiya Wasiq,12/1/2023,Created Script
# ------------------------------------------------------------------------------------------------- #


import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")
    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")


        def test_person_str(self):  # Tests the __str__() magic method
            person = Person("John", "Doe")
            self.assertEqual(str(person), "John,Doe")

class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Alice", "Smith", "2023-12-10",3)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, "2023-12-10")
        self.assertEqual(employee.review_rating, 3)

    def test_employee_review_date_type(self):  # Test the gpa validation
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "invalid_date",3)

    def test_employee_review_rating_within_range(self):  # Test the gpa validation
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "invalid_date",8)

    def test_employee_review_rating_type_int(self):  # Test the gpa validation
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "invalid_date", 4.0)

    def test_employee_str(self):
        employee = Employee("Eve", "Brown", "2023-12-10",4)  # Tests the __str__() magic method
        self.assertEqual(str(employee), "Eve,Brown,2023-12-10,4")



if __name__ == '__main__':
    unittest.main()
