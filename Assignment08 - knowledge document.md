# CREATING APPLICATIONS

## Introduction
This week we were introduced to the concept of modules and Testing. Adding on to the concept of Separation of concerns we learned to create different modules for our classes based on their purpose. We then learned how to import those modules to our main Python Script. We them moved on the various methods of testing our code by pro-actively to ensure that the functions operate as intended.

## Modules
Code modules (or just modules) are Python code files used by other code files. Within a code module file, you can create a set of functions and classes, then link the module to another code file to use those functions and classes. 

## Testing
Rigorous testing and quality assurance processes are essential, including unit testing, integration testing, and user acceptance testing.

**Unit testing** involves subjecting each individual unit of code, such as functions or methods, to a battery of tests to ensure that they function correctly in isolation. This proactive approach not only aids in detecting errors early but also contributes to more robust and maintainable software, as issues are addressed promptly, reducing the risk of accumulating complex and hard-to-debug problems over time.

We create unit tests by **defining functions that "exercise" the properties and methods of our code**. Typically, these testing functions are **in a separate module file**, often referred to as a **"test harness."**

Python has a unittest module with several functions that we can use to test our code. The most common ones that I would be using for this assignment are assertEquals and assertRaises

## Creating Python Script
For the purpose of this assignment, I have used the Assignment 08 starter code as my reference point. The assignment requires us to create an application that reads data from a Json file, presents the data to the user, gather more data from the user, save the new data, present the new data to the user and provide exit choice.

## Separation of Concerns
I will be assorting the functions in my program into three data classes: data classes, presentation classes and processing classes.

## Data Classes
I will start by creating my first module” Data classes”

```python

from datetime import date


class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - Rabiys Wasiq, 12.1.2023: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f"{self.first_name},{self.last_name}"


```
**_Figure 1 – Data Classes_**

in (Figure 1) I have defined my first data class Person that has 2 attributes, first_name and last_name. I have defined the attributes using the __init__ constructor. I have then added data validation rules using the property functions (getter and setter). Lastly I have defined the string for the Person class using the __str__ magic method.

```python
class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    - Rabiya Wasiq, 12.1.2023: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):

        super().__init__(first_name=first_name,last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: str):
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = int(value)
        else:
            raise ValueError("Please choose only values 1 through 5")


    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"

if __name__ == "__main__":
    print("Please refer to main.py")
```
**_Figure 2 – Data Class Employee(Person_**)

In (Figure 2) I have defined my class Employee which is a sub class of my Person class, using the overload method. Employee will inherit the attributes from Person class and will have two additional attribitutes.
Employee class has two other attributes review_date and review_rating. For review_date I have called a function from the datetime module, which I have imported at the start of the data_classes modeule as you can see in Figure 1.

```python
if __name__ == "__main__":
    print("Please refer to main.py")
```
The above code at the end of my data_class module tells Python to prompt a message to the user to not to run this module as a script and refer to the main.py which would contain the main program for the application.

## Processing Classes

It is important to note that at the start of every module we need to import classes from other modules that we would be calling. Its very similar to when we impot Json at the start of our program when we need to read and write data to a Json File. 

My processing classes will also be calling the Employee class from data_classes module, hence I start the module by importing those classes (Figure 3)

```python

import json
from data_classes import Person, Employee
from datetime import date


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Rabiya Wasiq,12.1.2023,Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        Rabiya Wasiq,11.4.2023,Created function

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_object: an instance of the Employee class
        :return: list
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data
```
**_Figure 3 – Processing Classes – Read data from file._**

The function Read_data_from_file reads data from Json file and loads it into a local variable List_of_dictionary_data.  I then create an instance of the Employe class. Using a for loop I iterate over each dictionary and assign values to the attributes of my employee_object (instance of Employee class). I then append each employee_object to a list of objects (Employee).

```python
@staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Rabiya Wasiq,12.1.2023,Created function

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")

if __name__ == "__main__":
    print("Please refer to main.py")
```
**_Figure 4 – Processing classes write_data_to_file_**

The function write_data_to_file converts the list of objects (Employees) to a list of dictionaries using a for loop and then adds it to a Json File. In both the functions I have made provisions for Errors by raising and catching exceptions.
Similar to the Data_classes I end the module __name__ system variable.

## Presentation Classes


This modules has a collection of Input and Output functions. I start the module by importing Employee class from my data_classes module.
```python

from data_classes import Employee

class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Rabiya Wasiq,12.1.2023,Created Class
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        Rabiya Wasiq,12.3.2023,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Rabiya Wasiq,12.1.2023,Created function

        :return: None
        """
        print()
        print(menu)
        print()
```
**_Figure 5 – Presenting Classes._**

The function output_error_message presents the output message to the user, it is important to note that this function has a default value None for the exception with an if condition. If the passed in Exception is not none it will present the user with the error message.
```python
@staticmethod
def input_menu_choice():
    """ This function gets a menu choice from the user

    ChangeLog: (Who, When, What)
    Rabiya Wasiq,12.1.2023,Created function

    :return: string with the users choice
    """
    choice = ''
    try:
        choice = input("Enter your menu choice number: ")
        if choice not in ("1", "2", "3", "4"): # Note these are strings
            return choice == ''
            raise Exception("Please, choose only 1, 2, 3, or 4")
    except Exception as e:
        IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

    return choice
```
**_Figure 6 – Presenting Classes – input_menu_choice_**

The function input_menu_choice prompts the user to enter a menu choice and returns the value entered by the user. The if condition raises an Exception if the user enters an invalid choice.
```python
@staticmethod
def output_employee_data(employee_data: list):
    """ This function displays employee data to the user

    ChangeLog: (Who, When, What)
    Rabiya Wasiq,12.1.2023,Created function

    :param employee_data: list of employee object data to be displayed

    :return: None
    """
    message:str = ''
    print()
    print("-" * 50)
    for employee in employee_data:
        if employee.review_rating == 5:
            message = " {} {} is rated as 5 (Leading)"
        elif employee.review_rating == 4:
            message = " {} {} is rated as 4 (Strong)"
        elif employee.review_rating == 3:
            message = " {} {} is rated as 3 (Solid)"
        elif employee.review_rating == 2:
            message = " {} {} is rated as 2 (Building)"
        elif employee.review_rating == 1:
            message = " {} {} is rated as 1 (Not Meeting Expectations"

        print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))
    print("-" * 50)
    print()
```
**Figure 7 – Presenting classes – output_employee_data**

The function output_employee_data presents the data to the user using the if condition and .format method to present a custom message based on the employee rating.
```python

@staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        Rabiya Wasiq,12.1.2023,Created function

        :param employee_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # Input the data
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data


if __name__ == "__main__":
    print("Please refer to main.py")
```
**Figure 8 – Presenting Classes- input_employee_data**

The function input_employee_data, creates an instance of the Employee class, gathers input from the user and adds them as attributes to the Employee_object . Since we have already added data validation rules to the Employee() using property function we don’t need to add them here. Here, we are only catching the exception that may be raised if the user enters invalid data.

## Testing Data Classes

To test my Data_classes module I start by importing the Pycharm built in unittest module. Figure 9

```python

import unittest
from data_classes import Person, Employee
Figure 9 – Testing Data Classes
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
```
**Figure 9 – Testing Data Classes – test_person_init**

I start by testing the _init_ constructor for my Person class. I start by creating an instance of the Person class and passing in attributes.
The self.asserEqual function compares the actual and expected values of those attributes.

```python

def test_person_str(self):  # Tests the __str__() magic method
    person = Person("John", "Doe")
    self.assertEqual(str(person), "John,Doe")
```
**Figure 10 – Testing Data Classes – test_person_string**

In Figure 10 I am testing the __str__ method of the person class using the same self.assertEqual function.
```python


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Alice", "Smith", "2023-12-10",3)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, "2023-12-10")
        self.assertEqual(employee.review_rating, 3)
```
**Figure 11 – test_employee_init**

Similarly I have also tested the _init_ constructor of my Employee class using the function self.asserEqual.
I had also added some data validation rules to my data classes by defining properties (getter and setter functions), To these the properties I will use the self.assertRaises function.

```python

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
```
**Figure 12 – Testing class properties using self.assertRaises function**

For the said purpose we pass in invalid values to our object and use the self.assertRaises function to ensure that the appropriate error was raised.

## Testing Processing Classes
My processing class has functions that read and write data to file. To test this function I will import the module tempfile, as I do not want the unit tests to impact my actual file data.I define the setup function that created a temporary file using the tempfile function and the teardown function closes the file.

```python

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
```
**Figure 13 – Testing Processing Data – Creating temporary file**

To test the read_employee_data_from_file function from my processing class I start by adding sample_data in my temporary file using the json.dump function.
I then call my FileProcessor.read_employee_data_from_file function and pass in the tempfile with the sample data and save the return value as a list, ‘employees”
```python

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
```

**Figure 14 – Testing processing classes – read_employee_data_from_file**

To test the function I use the self.assertEquals function. The length of the sample data should be equal to the length of employees. I use the for loop to iterate over the sample_data and test each attribute of the empoloyee_object.
```python

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
```
**Figure 15 – Testing Processing classes  - write_data_to_file and Filenotfound error**

We follow the same approach for the write_employee_data_to_file function. 
My read_employee_data_to_file function also raises a Filenotfound error when the file name is invalid. To test that I call the function while passing in an invald file name. I then use the self.assertRaises function to check is the error is raised or not.

## Testing Presentation Classes
My presentation classes has functions that obtain input from the user and present output.
To test the functions I need to bypass the built-in input function and enter values myself. For the said purpose I import the builtins module and patch from the unittest module.(Figure 16)

```python

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
```
**Figure 16 – Testing Presentation classes – testing input_menu_choice**

I define the function test_input_menu_choice, using the patch function I am able to enter my own value as user input and then test the actual and expected value using self.assertEquals function.
I also want to if an invalid menu choice would be stored or not, I test that using the test_input_invalid_menu_choice function. I have added an if condition in my input_menu_choice function that should not store any values other than “1”,”2”,”3’ or “4”. I pass an invalid menu_choice and then test it using the self.assertEqual function. Since it’s an invalid value the expected value should be False.
```python

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
    with patch('builtins.input', side_effect=["Eve","Brown","Dec 10, 2023","4"]):
        employees :list[Employee]= []
        employees = IO.input_employee_data(employee_data=employees,employee_type=Employee)
        self.assertEqual(0,len(employees))
```
**Figure 17 – Testing Presentation Classes – test_input_employee_data and test_input_employee_data_invalid_date**

To test the input_employee_data we again use the patch, to pass in multiple values we use the side effect parameter. The input_employee_data function saves the data collected by the user as an object of Employee class and appends it to a list. To test the function we use the self.assertEquals to compare the length of the list and then individually compare expected and actual value of each attribute. 

My Employee class also had data validation rules for the property functions. To test if my input function would accept an invalid value or not I define the test_input_employee_data_invalid_date and pass in invalid date format. The input_employee_data function should raise an exception and the employee object would not be created. For the said purpose we compare the length of the list of employees. Since no employee object was created the length of the list should be 0.

## Summary
I was successfully able to create a code that reads data from a Json file, presents the data to the user, gather more data from the user, save the new data, present the new data to the user and provide exit choice. I was able to create multiple modules for my classes using the concept of Separation of Concern. I was also able to link my classes my importing modules. I then ran tests for each class module. I particularly found testing processing classes very tricky with many un-expected errors. After troubleshooting using the Python debugger I was able to create the tests for that class also. 
I was able to run my program in both PyCharm and Command Prompt.

I was able to exhibit and display all the Python knowledge that I had learned in this course. I am particularly comfortable with if conditions, for loops and while loops. Also defining classes, function and modules. The concept of Testing was the most challenging for me.


