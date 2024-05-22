import requests


def get_studensts_data():
    """
    Get the students recordet data from Google Sheets with sheety.co API
    Args:
        No args
    """
    url = 'https://api.sheety.co/283e4374599ecb7c462c0903b64b4b25/students/students'
    response = requests.get(url)
    data = response.json()
    students_data = data["students"]

    return students_data


def add_student(new_student: dict):
    """
    Add a new student record.
    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.
    """
    students_data = get_studensts_data()

    # Check for existing student with the same name (assuming name is unique)
    for student in students_data:
        if student['name'] == new_student['name']:
            print(f"Student {student['name']} already exists")
            return  # Exit function if duplicate found
    # Find the next free row id show number of the row in response
    next_id = 1
    if students_data:
        next_id = max(student['id'] for student in students_data) + 1

    # Create a new dictionary with the next ID
    data_to_send = {"student": new_student}

    url = 'https://api.sheety.co/283e4374599ecb7c462c0903b64b4b25/students/students'
    response = requests.post(url, json=data_to_send)

    # Check for successful addition
    if response.status_code == 200:
        print("Student added successfully!")
    else:
        print(f"Error adding student: {response.text}")


def update_student(name):
    """
    Update an existing student record.
    Args:
    - name (str): The name of the student whose record is to be updated.
    """
    # Check if the student exists
    # Prompt the user to update fields and keep current values if fields are empty
    # Code to update the student's record


def delete_student(name):
    """
    Delete a student record based on the student's name.
    Args:
    - name (str): The name of the student to delete.
    """
    # Check if the student exists
    # Code to delete the student's record


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
