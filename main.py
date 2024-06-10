from openpyxl import Workbook, load_workbook
import file_manage as fm


def add_student(student: list, wb_year: Workbook, class_students: str):
    """
    Add a new student record to woorkbook.

    Args:
        student (list): Student info
        wb_year (Workbook): The workbook to add the student.
        class_students (str): The class to which  student will be added

    Return:
        None
    """
    all_students_info = wb_year.worksheets[0]
    group_sheet = wb_year[class_students]

    all_students_info.append(student)
    group_sheet.append(student)

    print("Student added successfully!")


def update_student(name):
    """
    Updates the information of an existing student in the students.json file.
    update specific fields (first name, last name, age, sex, email, subject)
    Args:
        name (str): first_name + last_name

    """



def delete_student(name):
    """
    Deletes a student's information from the students.json file.
        Args:
        name (str): first_name + last_name

    """


def search_student(name):
    """
    This function searches for a student in the students.json file by name.
    Args:
        name (str): first_name + last_name
    """


def list_all_students():
    """
    Reads all student information from the students.json file and prints it in a user-friendly format.

    """


def main():
    """
    Main function to provide user interaction.
    """
    current_workbook = None
    available_sheets = None
    new_student = []

    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Create new custom file")
        print("7. Create new default file")
        print("8. Load existing file")
        print("9. Save changes to an existing file")
        print("10. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            new_student = [input("First name: ").capitalize(), input("Last name: ").capitalize(),
                           input("Gender (Male/Female): ").capitalize(), input("Date of birth(YYYY-MM-DD): "),
                           input("Parent First and Last name together: ").capitalize(), ]
            students_group = input("Please choose a group ('A', 'B', 'C' or 'D'): ")
            new_student.append(new_student)
            path_to_wb = input("Enter the path to a file, where you want to add new student: ")
            wb = fm.load_existing_file(path_to_wb)
            add_student(new_student, wb, students_group)
            # grades = [float(input(f"Enter grade for {subjects_lst[i]}: ")) for i in range(len(subjects_lst))]
            # subjects = {subject: grade for subject in subjects_lst for grade in grades}
        elif choice == '2':
            first_name = input("Enter the first name of the student to update: ").capitalize()
            last_name = input("Enter the last name of the student to update: ").capitalize()

        elif choice == '3':
            first_name = input("Enter the first name of the student to update: ").capitalize()
            last_name = input("Enter the last name of the student to update: ").capitalize()

        elif choice == '4':
            first_name = input("Enter the first name of the student to update: ").capitalize()
            last_name = input("Enter the last name of the student to update: ").capitalize()

        elif choice == '5':

        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()