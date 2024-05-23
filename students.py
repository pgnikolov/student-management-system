import requests


def get_students_data():
    """
    Get the students recordet data from Google Sheets with sheety.co API
    Args:
        No args
    """
    url = 'https://api.sheety.co/283e4374599ecb7c462c0903b64b4b25/students/students'
    response = requests.get(url)
    r = response.json()
    data = r["students"]

    return data


def add_student(new_student: dict):
    """
    Add a new student record.
    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.
    """
    data = get_students_data()

    # Check for existing student with the same name
    for student in data:
        if student['name'] == new_student['name']:
            print(f"Student {student['name']} already exists")
            return  # Exit function if duplicate found
    # Find the next free row id show number of the row in response
    next_id = 1
    if data:
        next_id = max(student['id'] for student in data) + 1

    # Create a new dictionary with the next ID(row)
    data_to_send = {"student": new_student}

    url = 'https://api.sheety.co/283e4374599ecb7c462c0903b64b4b25/students/students'
    response = requests.post(url, json=data_to_send)

    # Check for successful addition
    if response.status_code == 200:
        print("Student added successfully!")
    else:
        print(f"Error adding student: {response.text}")


def update_subjects(data):
    """
    Updates the subjects field for a student.

    Args:
        data (dict): A dictionary containing student data, including the "subjects" field.

    Returns:
        None
    """

    # Get the current subjects
    current_subjects = data.get("subjects", [])

    # Prompt user for updated subjects
    while True:
        new_subjects_str = input(f"Update subjects (current: {' ,'.join(current_subjects)}): ")
        new_subjects = [subject.strip().upper() for subject in new_subjects_str.split(",") if subject.strip()]

        # Check for changes (avoid unnecessary updates)
        if new_subjects != current_subjects:
            data["subjects"] = new_subjects
            print("Subjects updated successfully.")
            return
        else:
            print("No changes made to subjects.")


def update_student(name):
    """
    Updates an existing student record.

    Args:
        name (str): The name of the student whose record is to be updated.

    Returns:
        bool: True if the student was updated successfully, False otherwise.
    """

    data = get_students_data()
    student_to_update = None

    # Find the student with the matching name
    for student in data:
        if student["name"] == name:
            student_to_update = student
            break

    # Check if student exists
    if not student_to_update:
        print(f"Student with name '{name}' not found.")
        return False

    # Prompt user for updates (assuming basic input functions)
    updated_fields = {}
    for field in student_to_update.keys():
        if field not in ("id", "name"):
            current_value = student_to_update[field]
            new_value = None

            if field == "grade":
                new_value = input(f"Update grade (current: {current_value}): ")

            else:
                new_value = input(f"Update {field} (current: {current_value}): ")
                if new_value:
                    new_value = new_value.strip().upper()  # Remove whitespaces, convert to uppercase (optional)
                    updated_fields[field] = new_value.split(",")  # Split the validated input into a list

            if new_value:
                updated_fields[field] = new_value
    # Update student data (assuming you have logic to update data in Sheety)
    if updated_fields:
        url = 'https://api.sheety.co/283e4374599ecb7c462c0903b64b4b25/students/students'
        data = {"student": {**student_to_update, **updated_fields}}  # Update existing data with changes

        response = requests.put(url + "/" + str(student_to_update["id"]), json=data)
        if response.status_code == 200:
            print("Student record updated successfully!")
            return True
        else:
            print(f"Error updating student: {response.text}")
            return False
    else:
        print("No changes made to student record.")
        return True


def delete_student(name: str):
    """
    Delete a student record based on the student's name.
    Args:
    - name (str): The name of the student to delete.
    """
    data = get_students_data()

    # Check if the student exists
    for student in data:
        if student['name'] == name:
            url = f'https://api.sheety.co/283e4374599ecb7c462c0903b64b4b25/students/students/{student["id"]}'
            response = requests.delete(url)
            if response.status_code == 204:
                print(f"Student '{name}' deleted successfully!")
            else:
                print(f"Error deleting student '{name}': {response.text}")
            return
    print(f"Student '{name}' not found.")


def search_student(name):
    """
    Search for a student by name and return their record.
    Args:
    - name (str): The name of the student to search for.
    """
    # Check if the student exists
    # Code to return the student's record


def list_all_students():
    """
    List all student records.
    """
    # Check if there are any student records
    # Code to list all students
