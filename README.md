# Student Management System :school:	

<img src="https://github.com/pgnikolov/student-management-system/assets/151896883/f86c16d7-3e41-490b-9141-c7e927b731fc" width="700" height="400"/>

A simple command-line student management system written in Python. This project allows users to manage 
student records by adding, updating, deleting, searching, and listing student information.

## Features 🧰
- Add Student: Add new student records.
- Update Student: Update existing student records.
- Delete Student: Remove student records.
- Search Student: Search for student records by name.
- List All Students: List all student records.

## Current Status 🚧

The project is currently in active development 🚀, with significant changes underway to enhance its functionality and improve the main concept.
Transitioning from storing records in a `JSON` file to using `Excel` files for better 📊 data management and manipulation directly from the code.

## Roadmap  🗺️

* **Transition to Excel-Based Data Management** 🌱

    Currently implementing functionality 🔧 to create, load, and save student records 💾 using Excel files directly within the code. 
    This change will provide users with more robust data management capabilities and easier manipulation of student information 📊.

* **Enhanced User Interaction** 💬

    The plan is to improve the user interaction experience by adding features such as customizable Excel file creation, 
    allowing users to define the structure of their student records directly from the application 📝.

* **Expanded Functionality** 🚀

    Future updates will focus on expanding the functionality of the application, including advanced search options, 
    sorting capabilities, and the ability to generate reports directly from the Excel data📊✨.



## Getting Started

### Prerequisites 📚
- Python 3.x
- `students.json` file in the project directory (initially an empty list: `[]`)

### Installation ⚙️

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
1. Run the main script to start the student management system:
  ```bash
  python main.py
  ```
2. Follow the on-screen menu to perform various student management operations.

### Functions 🎚️
Student Operations

`add_student()`
<details>
  <summary>More info</summary>

  Adds a new student to the students.json file.
  1. Prompts:
     * First name
     * Last name
     * Age
     * Sex
     * Email
     * Subjects and grades
  2. Updates: `students.json` with the new student information.

</details>

`update_student(name)`

<details>
  <summary>More info</summary>

  Updates the information of an existing student in the `students.json` file.
  - Parameters:
    - `name` (str): The full name of the student to be updated.
  - Prompts: Field to update (first name, last name, age, sex, email, subjects).
  - Updates: `students.json` with the updated student information.
</details>


`delete_student(name)`

<details>
  <summary>More info</summary>
  
  Deletes a student's information from the `students.json` file.
  - Parameters:
    - `name` (str): The full name of the student to be deleted.
  - Prompts: Confirmation to delete the student.
  - Updates: `students.json` with the student removed.
</details>

`search_student(name)`
<details>
  <summary>More info</summary>

  Searches for a student in the `students.json` file by name.
  - Parameters:
    - `name` (str): The full name of the student to search for.
  - Displays: The student information if found.
</details>

`list_all_students()`
<details>
  <summary>More info</summary>

  - Reads all student information from the `students.json` file.
  - Prints it in a user-friendly format.
  - Displays: All student records.
</details>

### Menu
The main menu provides the following options:

1. Add Student: Add a new student record.
2. Update Student: Update an existing student record.
3. Delete Student: Remove a student record.
4. Search Student: Search for a student record by name.
5. List All Students: List all student records.
6. Exit: Exit the program.

### Running the Program ⏯️
To start the student management system, run the following command:
```bash
python main.py
```
Follow the on-screen prompts to manage student records.

### Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.

### License 📝
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
