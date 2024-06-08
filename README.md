# Student Management System :school:	

<img src="https://github.com/pgnikolov/student-management-system/assets/151896883/f86c16d7-3e41-490b-9141-c7e927b731fc" width="828" height="464"/>

A simple command-line student management system written in Python. This project allows users to manage 
student records by adding, updating, deleting, searching, and listing student information.

## Features
- Add Student: Add new student records.
- Update Student: Update existing student records.
- Delete Student: Remove student records.
- Search Student: Search for student records by name.
- List All Students: List all student records.

## Getting Started

### Prerequisites
- Python 3.x
- `students.json` file in the project directory (initially an empty list: `[]`)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```
2. Create a `students.json` file in the project directory with an initial empty list:
```json
[]
```

### Usage
Run the main script to start the student management system:
```bash
python main.py
```
Follow the on-screen menu to perform various student management operations.

### Functions
Student Operations
`add_student()`
Adds a new student to the students.json file.
- Prompts:
    - First name
    - Last name
    - Age
    - Sex
    - Email
    - Subjects and grades
- Updates: `students.json` with the new student information.

`update_student(name)`
Updates the information of an existing student in the `students.json` file.
- Parameters:
    - `name` (str): The full name of the student to be updated.
- Prompts: Field to update (first name, last name, age, sex, email, subjects).
- Updates: `students.json` with the updated student information.

`delete_student(name)`
Deletes a student's information from the `students.json` file.
- Parameters:
    - `name` (str): The full name of the student to be deleted.
- Prompts: Confirmation to delete the student.
- Updates: `students.json` with the student removed.

`search_student(name)`
Searches for a student in the `students.json` file by name.
- Parameters:
    - `name` (str): The full name of the student to search for.
- Displays: The student information if found.

`list_all_students()`
Reads all student information from the `students.json` file and prints it in a user-friendly format.
- Displays: All student records.

### Menu
The main menu provides the following options:

1. Add Student: Add a new student record.
2. Update Student: Update an existing student record.
3. Delete Student: Remove a student record.
4. Search Student: Search for a student record by name.
5. List All Students: List all student records.
6. Exit: Exit the program.

### Running the Program
To start the student management system, run the following command:
```bash
python main_code.py
```
Follow the on-screen prompts to manage student records.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
