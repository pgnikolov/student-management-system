import json

def add_student(first_name, last_name, age, sex, email, subjects):
    """
    Add a new student record.
    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - sex (str): Stundent's sex
    - email (str): The grade of the student.
    - subjects (dict) with subjects (str) and grade (float): The subjects the student is enrolled in.
    """
    with open('students.json', 'r') as f:
        students = json.load(f)

    # Create the student information dictionary
    student_info = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "sex": sex,
        "email": email,
        "subjects": subjects
    }

    # Add the student information to the main students dictionary
    students[f"{first_name} {last_name}"] = student_info
    print("Student added successfully!")

    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)


def update_student(name):
    """
    Updates the information of an existing student in the students.json file.
    update specific fields (first name, last name, age, sex, email, subject)
    Args:
        name (str): first_name + last_name

    """

    with open('students.json', 'r') as f:
        students = json.load(f)

    student_info = students[name]

    if name not in students:
        print(f"Student with name '{name}' not found.")

    updated_fields = {}  # Dictionary to store updated information

    while True:
        update_field = input(
            "Enter the field to update (age, subjects, or 'q' to quit): ").lower()

        if update_field == 'q':
            break
        elif update_field == "age":
            age = int(input())
            student_info[update_field] = age
        elif update_field == 'subjects':
            update_subject = input("Enter the subject to update(Mathematics, Literature, IT, History, "
                                   "Geography, Philosophy, Biology, Physics, Chemistry, Sport, Art): ").capitalize()
            grade = float(input(f"Enter grade for {update_subject}: "))
            student_info['subjects'][update_subject] = grade

            if update_subject not in student_info['subjects']:
                print(f"Subject '{update_subject}' not found.")
                continue

    # Update the student information in the main dictionary
    students[name] = student_info

    # Save the updated students data to the JSON filea
    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)

    print(f"Student information for '{name}' updated successfully!")


def delete_student(name):
    """
    Deletes a student's information from the students.json file.
        Args:
        name (str): first_name + last_name

    """

    with open('students.json', 'r') as f:
        students = json.load(f)

    if name not in students:
        print(f"Student with name '{name}' not found.")
        return  # Exit the function if a student not found

    confirmation = input(f"Are you sure you want to delete student '{name}' (y/n): ").lower()

    if confirmation == 'y':
        students.pop(name)  # Remove student data using del
        print(f"Student '{name}' deleted successfully!")

        with open('students.json', 'w') as f:
            json.dump(students, f, indent=4)

    else:
        print("Deletion cancelled.")


def search_student(name):
    """
    This function searches for a student in the students.json file by name.
    Args:
        name (str): first_name + last_name
    """
    with open('students.json', 'r') as f:
        students = json.load(f)

    if name in students:
        student_info = students[name]
        # Print student information
        print("Student Information:")
        for field, value in student_info.items():
            print(f"{field}: {value}")
    else:
        print(f"Student with name '{name}' not found.")


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


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter the first name of the student: ").capitalize()
            last_name = input("Enter the last name of the student: ").capitalize()
            age = int(input("Enter the age of the student: "))
            sex = input("Enter the sex of the student (Male/Female): ").capitalize()
            email = input("Enter the email of the student: ").lower()
            subjects_lst = ["Mathematics", "Literature", "IT", "History", "Geography", "Philosophy", "Biology",
                            "Physics", "Chemistry", "Sport", "Art"]
            grades = [float(input(f"Enter grade for {subjects_lst[i]}: ")) for i in range(len(subjects_lst))]
            subjects = {subject: grade for subject in subjects_lst for grade in grades}

            add_student(first_name, last_name, age, sex, email, subjects)
        elif choice == '2':
            first_name = input("Enter the first name of the student to update: ").capitalize()
            last_name = input("Enter the last name of the student to update: ").capitalize()
            name = f"{first_name} {last_name}"  # Use full name as the key
            update_student(name)
        elif choice == '3':
            first_name = input("Enter the first name of the student to update: ").capitalize()
            last_name = input("Enter the last name of the student to update: ").capitalize()
            name = f"{first_name} {last_name}"  # Use full name as the key
            delete_student(name)
        elif choice == '4':
            first_name = input("Enter the first name of the student to update: ").capitalize()
            last_name = input("Enter the last name of the student to update: ").capitalize()
            name = f"{first_name} {last_name}"  # Use full name as the key
            search_student(name)
        elif choice == '5':
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
