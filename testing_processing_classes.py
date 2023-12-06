# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of unit tests for processing classes
# ChangeLog: (Who, When, What)
# Rabiya Wasiq,12/1/2023,Created Script
# ------------------------------------------------------------------------------------------------- #


import tempfile
import unittest
import json
from processing_classes import FileProcessor
from data_classes import Employee

class TestFileprocessor(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name

    def tearDown(self):
        self.temp_file.close()


    def test_read_data_from_file(self):
        sample_data = [
            {"FirstName": "Vic", "LastName": "Vu", "ReviewDate": "2023-12-01","ReviewRating":  3},
            {"FirstName": "Sue", "LastName": "Salius", "ReviewDate": "2023-12-01", "ReviewRating": 3}
            ]

        with open(self.temp_file_name, 'w') as file:
            json.dump(sample_data,file)

        employees = []
        employees = FileProcessor.read_employee_data_from_file(file_name=self.temp_file_name,
                                                               employee_data=employees,employee_type=Employee) # Note this is the class name (ignore the warning)
        self.assertEqual(len(sample_data),len(employees))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i]["FirstName"],employees[i].first_name)
            self.assertEqual(sample_data[i]["LastName"], employees[i].last_name)
            self.assertEqual(sample_data[i]["ReviewDate"], employees[i].review_date)
            self.assertEqual(sample_data[i]["ReviewRating"], employees[i].review_rating)



    def test_write_data_to_file(self):
        sample_data = [
            Employee("Eve", "Brown", "2023-12-10",4),
            Employee("Eve", "Brown", "2023-12-10",4)
            ]

        FileProcessor.write_employee_data_to_file(self.temp_file_name,sample_data)

        with open(self.temp_file_name, 'r') as file:
            file_data = json.load(file)

        self.assertEqual(len(sample_data), len(file_data))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i].first_name,file_data[i]["FirstName"])
            self.assertEqual(sample_data[i].last_name,file_data[i]["LastName"])
            self.assertEqual(sample_data[i].review_date, file_data[i]["ReviewDate"])
            self.assertEqual(sample_data[i].review_rating, file_data[i]["ReviewRating"])

    def test_read_data_from_file_not_found(self):
        employees = []
        with self.assertRaises(FileNotFoundError):
            employees = FileProcessor.read_employee_data_from_file(file_name="invalid.json",
                                                                   employee_data=employees,employee_type=Employee)




if __name__ == '__main__':
    unittest.main()
