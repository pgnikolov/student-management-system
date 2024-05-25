# Students Management System :school:	

![pic](https://github.com/pgnikolov/student-management-system/assets/151896883/75dc6683-e5bb-4e34-ab8e-013146059d72)

### SoftUni lecturer's task  

This Python script provides a basic command-line interface for managing student data in an educational institution.

### Features:

* Add new students
* Update existing student information
* Delete student records
* Search for students by full name
* List all students

```add_student:```

* This function allows adding a new student to the students.json file.
* It prompts the user for various details like name, age, sex, email, and subjects with grades (optional).
* An empty dictionary is created to store subjects and their grades.
* The script iterates until the user chooses not to add more subjects.
* Finally, a dictionary containing all student information is created and added to the main students dictionary (keyed by full name).
* The updated students dictionary is then written back to the JSON file.

```update_student:```

* This function updates an existing student's information.
* It takes the student's full name as input to identify the record.
* It checks if the student exists in the JSON data.
* If found, it allows the user to update specific fields (like first name, age, etc.) or subjects (add, update grade).
* An updated_fields dictionary is used to store changes.
* After user confirmation, the updated information is written back to the students dictionary and subsequently saved to the JSON file.

```delete_student:```

* This function deletes a student's information based on their full name.
* It checks if the student exists in the JSON data.
* If found, it prompts the user for confirmation before deleting the record.
* Upon confirmation, the student's data is removed using ```del```.
* The updated ```students``` dictionary is then saved to the JSON file.

```search_student:```

* This function allows searching for a student by their full name.
* It checks if the student exists in the JSON data.
* If found, it iterates through the student's information dictionary and prints each field (name, age, etc.) and its corresponding value.

```list_all_students:```

* This function displays a list of all students and their information stored in the ```students.json``` file.
* It checks if there are any students in the file.
* If students exist, it iterates through each student's information dictionary and prints their name, followed by details (age, subjects, etc.) on separate lines.

### Future Development:

* Academic Records: Keeps track of grades and academic progress.
* Attendance & Scheduling: Tracks student attendance and manages class schedules.
* Implement data storage using files or a database to persist student information.
* Add features like displaying student details, searching by partial names, and storing additional student information.
* Develop a more user-friendly interface (e.g., using a graphical user interface library).
