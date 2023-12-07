
## Introduction 
This application reads data from a Json file, presents the data to the user, gather more data from the user, save the new data, present the new data to the user and provide exit choice.

The data validation rules incorporated in the data classes ensure that the correct format of data is received from the user.

The source code of this repository is [here](https://github.com/rabiya7488/A08-2)


## Separation of Concerns
This program is assorted  into three data classes: data classes, presentation classes and processing classes.


# Class Diagram ![Assignment 08 Diagram.drawio.png](Images%2FAssignment%2008%20Diagram.drawio.png))



# Employee Ratings Program

## Classes

### `Person`

A class representing person data.

#### Properties:

- `first_name` (str): The person's first name.
- `last_name` (str): The person's last name.

#### Methods:

- `__init__(self, first_name: str = "", last_name: str = "")`: Constructor to initialize the person instance.
- `__str__(self) -> str`: Returns a formatted string representation of the person.


### `Employee`

A class representing employee data, inheriting from the `Person` class.

#### Properties:

- `first_name` (str): The employee's first name.
- `last_name` (str): The employee's last name.
- `review_date` (date): The data of the employee review.
- `review_rating` (int): The review rating of the employee's performance (1-5).

#### Methods:

- `__init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3)`: Constructor to initialize the employee instance.
- `__str__(self) -> str`: Returns a formatted string representation of the employee.


### `FileProcessor`

A collection of processing layer functions that work with JSON files.

#### Methods:

- `read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee) -> list`: Reads data from a JSON file and loads it into a list of dictionary rows.
- `write_employee_data_to_file(file_name: str, employee_data: list) -> None`: Writes data to a JSON file with data from a list of dictionary rows.


### `IO`

A collection of presentation layer functions that manage user input and output.

#### Methods:

- `output_error_messages(message: str, error: Exception = None) -> None`: Displays a custom error message to the user.
- `output_menu(menu: str) -> None`: Displays the menu of choices to the user.
- `input_menu_choice() -> str`: Gets a menu choice from the user.
- `output_employee_data(employee_data: list) -> None`: Displays employee data to the user.
- `input_employee_data(employee_data: list, employee_type: Employee) -> list`: Gets the first name, last name, review date, and review rating from the user.

#### ChangeLog:

## Program Overview

The program manages employee ratings data and provides the following functionality:

1. Display current employee rating data.
2. Enter new employee rating data.
3. Save data to a file.
4. Exit the program.

## Usage

1. Run the program.
2. Choose from the menu options by entering the corresponding number.
3. Follow the prompts to input or display employee data.
4. Save data to a file or exit the program as needed.

## File Handling

The program reads and writes employee data to a JSON file named `EmployeeRatings.json`. Ensure the file exists before running the script.


Sure, let's create a couple of example use cases for your Employee Ratings program.

### Use Case 1: Display Current Employee Rating Data

**Actor:** User  
**Description:** The user wants to view the current employee rating data stored in the program.

**Steps:**
1. User launches the Employee Ratings program.
2. User selects the option to "Show current employee rating data."
3. The program retrieves and displays the current employee rating data.

**Alternative Flow:**
- If there is no existing data, the program displays a message indicating that there is no data available.

---

### Use Case 2: Enter New Employee Rating Data

**Actor:** User  
**Description:** The user wants to enter new employee rating data into the program.

**Steps:**
1. User launches the Employee Ratings program.
2. User selects the option to "Enter new employee rating data."
3. The program prompts the user to enter the details for a new employee, including first name, last name, review date, and review rating.
4. User provides the required information.
5. The program validates the input and adds the new employee data to the existing data.
6. The program displays the updated employee rating data.

**Alternative Flow:**
- If there is an error in the input (e.g., invalid date format or review rating out of range), the program displays an error message and prompts the user to enter the data again.

---

### Use Case 3: Save Data to a File

**Actor:** User  
**Description:** The user wants to save the current employee rating data to a file.

**Steps:**
1. User launches the Employee Ratings program.
2. User selects the option to "Save data to a file."
3. The program prompts the user to provide a filename for saving the data.
4. User enters the desired filename.
5. The program validates the filename and writes the current employee rating data to the specified file.
6. The program displays a message confirming the successful save operation.

**Alternative Flow:**
- If there is an issue with file access or the filename provided is not valid, the program displays an error message.

---

### Use Case 4: Exit the Program

**Actor:** User  
**Description:** The user wants to exit the Employee Ratings program.

**Steps:**
1. User launches the Employee Ratings program.
2. User selects the option to "Exit the program."
3. The program terminates, and the application closes.

**Alternative Flow:**
- If there are unsaved changes, the program prompts the user to confirm the exit and save data before closing.