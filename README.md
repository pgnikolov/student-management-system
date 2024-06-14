# Student Management System  📚

<img src="https://github.com/pgnikolov/student-management-system/assets/151896883/66beb7d5-78c3-46a2-a1c7-e4e2b797c43c" width="7200" height="420"/>

Command-line application for managing student records efficiently. It allows users to perform various operations such as adding, updating, deleting, and searching for student information.
The system is designed to streamline administrative tasks related to student management.

## Features  🛠️

- Enhanced User Interaction: Improve user experience with customizable Excel file creation.
- Expanded Functionality: Include advanced search options, sorting capabilities, and report generation directly from Excel data.

## Current Status 🚧

The project is actively undergoing development to enhance user interaction and expand functionality.

## Roadmap  🗺️

* **Expanded Functionality** 🚀

    Future updates will focus on expanding the functionality of the application, including advanced search options,
    sorting capabilities, and the ability to generate reports directly from the CSV data.📊✨.

* **School Subjects and Grades Management** 📚

    - Calculating the average grade for the first half of the year, the second half, and the entire year.
    - Providing insights into student performance and progress in various subjects.



## Getting Started  ⏯️

### Prerequisites 📚

- Python 3.x
- Pandas library

You can install the required library using pip:
```bash
pip install pandas
```

### File Structure 📂

`main.py`: The main script containing all functionalities.

`students23.csv`: CSV file containing student records.

### Installation ⚙️ 

1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/student-management-system.git
  cd student-management-system
  ```

### Usage

1. Run the main script to start the student management system:
  ```bash
  python main.py
  ```
2. Follow the on-screen menu to perform various student management operations.

### Functions 🎚️

### Menu
The main menu provides the following options:

1. Add Student: Add a new student record.
2. Delete Student: Remove a student record. (Feature under development)
3. Search Student: Search for a student record by name. (Feature under development)
4. List All Students: List all student records. (Feature under development)
5. Exit: Exit the program.

#### Add Student 👨‍🎓
Adds a new student record to the DataFrame.

<details>
    <summary>More...</summary>
        
    - Parameters:
        - new_students (list): List containing the information of the new student.
        - df_students (pd.DataFrame): DataFrame containing existing student records.

    - Returns:
        - None
        
</details>


#### Delete Student ✖️
Deletes a student record from the DataFrame.

<details>
    <summary>More...</summary>
    
    - Parameters:
        - first_name_del (str): First name of the student to delete.
        - last_name_del (str): Last name of the student to delete.
        - df_students (pd.DataFrame): DataFrame containing existing student records.

    - Returns:
        - df (pd.DataFrame): DataFrame with the deleted record removed.

    - Raises:
        - ValueError: If no student with the given names is found.
    
</details>


#### Search Student 🔍
Searches for a student in the DataFrame by first and last name.

<details>
    <summary>More...</summary>

    - Parameters:
        - first_name_search (str): First name of the student to search.
        - last_name_search (str): Last name of the student to search.
        - df_students (pd.DataFrame): DataFrame containing existing student records.

    - Returns:
        - result (pd.DataFrame): DataFrame containing students matching the search criteria.

    - Raises:
        - ValueError: If no student with the given names is found.
        
</details>


#### List All Students by Group 📝
Prints all students who are in the same group (class).

<details>
    <summary>More...</summary>

    - Parameters:
        - df_students (pd.DataFrame): DataFrame containing existing student records.
        - class_students (str): The group (class) of students to filter.

    - Returns:
        - result (pd.DataFrame): DataFrame containing students filtered by the provided group.
    
</details>

### Data Validation ☑️

#### Get Student Information  ℹ️
Prompts the user for student information and performs basic validation.

- **Returns**:
    - `list`: A list containing the student's information.

#### Validate Email 📧
Checks if the email format is valid.

- **Parameters**:
    - `email` (str): The email address to validate.

- **Returns**:
    - `bool`: True if the email format is likely valid, False otherwise.

#### Validate Date 📅
Checks if the date format is valid (YYYY-MM-DD).

- **Parameters**:
    - `date_str` (str): The date string to validate.

- **Returns**:
    - `bool`: True if the date format is valid, False otherwise.


## Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.

## License 📝
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
