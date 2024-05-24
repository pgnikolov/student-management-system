import json


def add_student():
    with open('students.json', 'r') as f:
        students = json.load(f)

    first_name = input("Enter the first name of the student: ").capitalize()
    last_name = input("Enter the last name of the student: ").capitalize()
    age = int(input("Enter the age of the student: "))
    sex = input("Enter the sex of the student (Male/Female): ").capitalize()
    email = input("Enter the email of the student: ").lower()

    key = f"{first_name} {last_name}"
    students[key] = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "sex": sex,
        "email": email
    }

    print("Student added successfully!")

    # Save the updated students to the JSON file
    with open('students.json', 'w') as f:
        json.dump(students, f)


def update_student():
    """
    Updates the information of an existing student in the students.json file.
    update specific fields (first name, last name, age, sex, email)

    """

    with open('students.json', 'r') as f:
        students = json.load(f)

    first_name = input("Enter the first name of the student to update: ").capitalize()
    last_name = input("Enter the last name of the student to update: ").capitalize()
    key = f"{first_name} {last_name}"  # Use full name as the key

    if key not in students:
        print(f"Student with name '{key}' not found.")

    updated_fields = {}  # Dictionary to store updated information

    while True:
        field_to_update = input(
            "Enter the field to update (first_name, last_name, age, sex, email, or 'q' to quit): ").lower()

        if field_to_update == 'q':
            break

        if field_to_update not in students[key]:
            print(f"Invalid field: '{field_to_update}'. Valid fields are: first_name, last_name, age, sex, email.")
            continue

        if field_to_update == 'age':
            new_value = int(input(f"Enter the new value for {field_to_update}: "))
            if new_value < 0:
                print("Age cannot be negative.")
                print(f"Invalid input for '{field_to_update}'. Please enter a valid value.")

        new_value = input(f"Enter the new value for {field_to_update}: ")
        updated_fields[field_to_update] = new_value

        continue

    # Update the student's information with the collected data
    students[key].update(updated_fields)

    # Save the updated students data to the JSON filea
    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)

    print(f"Student information for '{key}' updated successfully!")


def delete_student():
    """
    Deletes a student's information from the students.json file.

    """

    with open('students.json', 'r') as f:
        students = json.load(f)
    first_name = input("Enter the first name of the student to delete: ").capitalize()
    last_name = input("Enter the last name of the student to delete: ").capitalize()
    full_name = f"{first_name} {last_name}"  # Use full name as the key for simplicity

    key = f"{full_name}"  # Use full name as the key

    if key not in students:
        print(f"Student with name '{full_name}' not found.")
        return  # Exit the function if student not found

    confirmation = input(f"Are you sure you want to delete student '{full_name}' (y/n): ").lower()

    if confirmation == 'y':
        del students[key]  # Remove student data using del
        print(f"Student '{full_name}' deleted successfully!")

        # Save the updated students data to the JSON file
        with open('students.json', 'w') as f:
            json.dump(students, f, indent=4)

    else:
        print("Deletion cancelled.")


def search_student():
    with open('students.json', 'r') as f:
        students = json.load(f)

    first_name = input("Enter the first name of the student: ").capitalize()
    last_name = input("Enter the last name of the student: ").capitalize()
    full_name = f"{first_name} {last_name}"
    key = f"{full_name}"  # Use full name as the key for simplicity
    if key in students:
        student_info = students[key]
        # Print student information
        print("Student Information:")
        for field, value in student_info.items():
            print(f"{field}: {value}")
    else:
        print(f"Student with name '{full_name}' not found.")


def list_all_students():
    """
    Reads all student information from the students.json file and prints it in a user-friendly format.

    """

    with open('students.json', 'r') as f:
        students = json.load(f)

    if not students:
        print("No students found in the file.")
        return  # Exit the function if there are no students

    # Print student information
    print("Students:")
    for name, info in students.items():
        print(f"{name}:")
        for field, value in info.items():
            print(f"- {field}: {value}")
        print()  # Print an empty line between students
