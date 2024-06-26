# School Management System  📚

<img src="https://github.com/pgnikolov/student-management-system/assets/151896883/66beb7d5-78c3-46a2-a1c7-e4e2b797c43c" width="720" height="420"/>

Command-line application for managing student records efficiently. It allows users to perform various operations such as adding, updating, deleting, and searching for student information.
The system is designed to streamline administrative tasks related to student management.

## Features  🛠️

- Enhanced User Interaction: Improve user experience with customizable Excel file creation.
- Expanded Functionality: Include advanced search options, sorting capabilities, and report generation directly from Excel data.

## Current Status 👷‍♂️

The project is actively undergoing development to enhance user interaction and expand functionality.

### Future Enhancements ✨

* **Visualization of Student Performance** 👀 (In Progress) 

  Actively working on adding functionalities to generate visual plots for student performance analysis. These plots will provide teachers with valuable insights into student development and achievement. Some potential benefits include:
  
    - **Overall Class Performance** 🎭: Visualizations can help identify trends and patterns in class performance across different subjects. This can be used to assess the effectiveness of teaching methods and identify areas for improvement.
  
    - **Individual Student Performance** 🦸: Visualizations can help track individual student progress over time and identify students who may be excelling in specific subjects or require additional support.
    
    - **Identifying Strengths and Weaknesses** 💪: Visualizations can reveal student strengths and weaknesses in different subjects. This can help teachers tailor their instruction to meet the individual needs of their students.

    - **Early Intervention** 🚑: By identifying students whose performance is declining, visualization tools can help teachers intervene early and provide targeted support.

* **Potential Visualizations** 🪄

  - Bar charts 📊 and histograms ⚖️: These can show the distribution of grades for a particular class or subject, highlighting the overall performance and potential gaps.

  - Line charts 📈: These can track individual student performance over time, allowing teachers to monitor progress and identify trends.
    
  - Scatter plots ↔️ : These can reveal relationships between different variables, such as grades in different subjects or attendance and performance.

* **Missing Student Monitoring** 🙈: Features to identify and report missing students are also planned for future development.


## Getting Started  ⏯️

### Prerequisites 📚

- Python 3.x
- Pandas library

You can install the required library using pip:
```bash
pip install pandas
pip install matplotlib
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
2. Delete Student: Remove a student record.
3. Search Student: Search for a student record by name.
4. List All Students: List all student records.
5. List term 1 final grades for choosen group and subject.
6. List term 2 final grades for choosen group and subject.
7. List yearly grades for choosen group and subject.
8. Distribution of Subject Yearly Grades by Groups.
9. Exit: Exit the program.

##### Add Student 👨‍🎓
Adds a new student record to the DataFrame.

<details>
    <summary>More...</summary>
        
    - Parameters:
        - new_students (list): List containing the information of the new student.
        - df_students (pd.DataFrame): DataFrame containing existing student records.

    - Returns:
        - None
        
</details>

##### Delete Student ✖️
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


##### Search Student 🔍
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


##### List All Students by Group 📝
Prints all students who are in the same group (class).

<details>
    <summary>More...</summary>

    - Parameters:
        - df_students (pd.DataFrame): DataFrame containing existing student records.
        - class_students (str): The group (class) of students to filter.

    - Returns:
        - result (pd.DataFrame): DataFrame containing students filtered by the provided group.
    
</details>

### New Functionality: Student Grade Retrieval and Reporting

This section details the newly implemented functions for retrieving and reporting student grades:

**Retrieving Grades** : Term 1, Term 2 and Yearly

* `get_grade_term1(df_students, class_students, subject)`: This function retrieves and prints the Term 1 grades for a specific subject and class from a provided student DataFrame.
  
* `get_grade_term2(df_students, class_students, subject)`: This function retrieves and prints the Term 2 grades for a specific subject and class from a provided student DataFrame.

* `get_grade_yearly(df_students, class_students, subject)`: This function retrieves and prints the yearly grades for a specific subject and class from a provided student DataFrame.

**Function Arguments** :

* `df_students (pd.DataFrame)`: The DataFrame containing student information (including columns like "group", "first_name", "last_name", and subject grades).

* `class_students (str)`: The name of the class (group) to filter students from (e.g., "group_a").

* `subject (str)`: The subject for which to retrieve grades (e.g., "math").

**Output Example**:

```python
first_name last_name  english_t1_end
 Sebastian      Bell               6
      Levi    Rogers               6
     Aiden    Parker               5
      Aria    Murphy               5
  Victoria   Griffin               5
      Nora      Ward               5
   Natalie    Torres               5
   Matthew   Stewart               5
   Madison   Bennett               5
      Zoey      Gray               5
   Eleanor    Howard               5
    Daniel      Cook               5
     Chloe   Russell               5
    Carter     Adams               5
    Aurora     James               5
      Jack    Nelson               4
   Grayson       Lee               4
      Lily   Ramirez               4
     David      Ward               4
      Owen    Cooper               4
  Scarlett    Hughes               4
     Caleb       Cox               4
     Wyatt    Brooks               4
     Layla     Price               4
    Hannah  Peterson               3
   Jackson      Reed               3

```
```python
first_name last_name  chemistry_year
     Henry    Harris             5.5
  Benjamin   Jackson             5.5
      Ella    Garcia             5.5
   Michael  Thompson             5.5
     Lucas     White             5.5
   Abigail  Thompson             5.0
  Victoria   Johnson             5.0
    Sophia  Anderson             5.0
    Oliver     Brown             5.0
       Mia   Jackson             5.0
     James    Thomas             5.0
  Isabella    Thomas             5.0
    Harper    Harris             5.0
     Ethan    Garcia             5.0
      Emma    Wilson             5.0
       Ava    Taylor             5.0
    Amelia     White             5.0
 Alexander    Martin             4.5
     Jacob  Martinez             4.5
     Grace  Martinez             4.5
      Liam   Johnson             4.5
      Noah     Smith             4.5
    Elijah    Taylor             4.5
    Olivia     Moore             4.5
   William  Anderson             4.5
    Evelyn    Martin             4.0

```

### DataFrame Functions 🖼️

`get_year_data(df: pd.DataFrame, year_in_school: int) -> pd.DataFrame` - This function filters a DataFrame to return data for a specific year in school.

`get_group_data(df: pd.DataFrame, year_in_school: int, group: str) -> pd.DataFrame` - This function further filters data by both year in school and student group.

`grade_name(grade) -> str` - This function assigns a grade name based on a given numeric grade.

### Data Visualisation Functions 📊

`yearly_grade_dist_subject(df: pd.DataFrame, year_in_school: int, grade_year: int, subject: str) -> None` - This function generates pie charts showing the distribution of yearly grades for a specified subject and grade year. It filters data, calculates grade names, groups the data, and plots pie charts for each student group.

<img src="https://github.com/pgnikolov/student-management-system/assets/151896883/13e53418-646e-4a6c-bb03-de1a32b8be6f"  width="420" height="420"/>



**Important Notes** :

* These functions directly print the results to the console, displaying students' first name, last name, and the requested grades (Term 1, Term 2, or Yearly) in descending order (highest to lowest).

* The index column (row numbers) is excluded from the output.


### Data Validation ☑️

- Get Student Information 📩: Prompts the user for student information and performs basic validation.

- Validate Email 📧:  Checks if the email format is valid.

- Validate Date 📅: Checks if the date format is in valid format (YYYY-MM-DD).

- Group Validation 🔡: Prompts the user to enter a student's group until a valid group is provided.

- Subject Validation ✅: Prompts the user to enter a subject name until a valid subject is provided.

- Grade Year Validation 👌: Prompts the user to enter a year fo grade, until a valid year is provided.

- Year Validation 🗓️: Prompts the user to enter a student's year in school until a valid year is provided.


## Contributing 🤝
Contributions are welcome! Please fork the repository and submit a pull request.

## License 📝
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact 📫
For any questions or feedback, please contact [![Gmail](https://img.shields.io/badge/-Gmail-c14438?style=flat&logo=Gmail&logoColor=white)](mailto:pgnikolov@gmail.com)
