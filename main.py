import pandas as pd
from datetime import datetime

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


def add_student(new_students: list, df_students: pd.DataFrame):
    """
    Add a new student record to woorkbook.

    Args:
        df_students (pd.DataFrame): Student records.
        new_students (list): Student info
    Return:
        None
    """
    new_rows = pd.DataFrame(new_students, columns=df_students.columns[:10])
    num_cols_student = len(new_students[0])
    num_cols_df = len(df_students.columns)

    try:
        if num_cols_student != num_cols_df[:10]:
            raise ValueError
        # all other cols fill with NaN
        for col in df_students.columns[10:]:
            new_rows[col] = pd.NA

        df_students = pd.concat([df_students, new_rows], ignore_index=True)
        return df_students

    except ValueError:
        "The number of the columns in the new student doesn't match"


def delete_student(first_name_del: str, last_name_del: str, df_students: pd.DataFrame):
    """
    Delete student record from dataframe.
    Args:
        first_name_del (str): Student's first name.
        last_name_del (str): Student's last name.
        df_students (pd.DataFrame): Student records.
    Return:
        df (pd.DataFrame): Students info without deleted record.
    Raises:
        ValueError: If no student with the given names is found.
    """
    try:
        df = df_students[(df_students['first_name'] != first_name_del) | (df_students['last_name'] != last_name_del)]
    except KeyError:
        raise ValueError(f"No student with names '{first_name_del} {last_name_del}' found.")

    return df


def search_student(first_name_search: str, last_name_search: str, df_students: pd.DataFrame):
    """
        This function searches for a student in the students Excel file by name.
    Args:
        first_name_search (str): Student's first name.
        last_name_search (str): Student's last name.
        df_students (pd.DataFrame): Student records.
    Return:
        result (pd.DataFrame): Students filtered by user criteria.
    Raises:
        ValueError: If there is no student with the given names.
    """
    result = df_students[
        (df_students['first_name'] == first_name_search) & (df_students['last_name'] == last_name_search)]
    if result.empty:
        raise ValueError(f"No student with names '{first_name_search} {last_name_search}' found.")

    return result


def list_all_students_by_group(df_students: pd.DataFrame, class_students: str):
    """
        Print all students who are in same group (class).
    Args:
        df_students (pd.DataFrame): Student records.
        class_students (str): The group(class) students we want.
    Return:
        result (pd.DataFrame): Students filtered by user criteria.
    """
    result = df_students[df_students['group'] == class_students]

    return result


def group_validation() -> str:
    """
        This function prompts the user to enter a student's group until a valid group is provided.
        Valid groups are: "group_a", "group_b", "group_c", and "group_d".
  Returns:
      str: The validated student group entered by the user.
    """
    valid_groups = ["group_a", "group_b", "group_c", "group_d"]

    while True:
        group = input("Enter student's group(group_a, group_b, group_c or group_d: ").lower()
        if group in valid_groups:
            break
        else:
            print("Invalid group. Please enter 'group_a', 'group_b', 'group_c', or 'group_d'.")

    return group


def subject_validation() -> str:
    """
        This function prompts the user to enter a subject name until a valid subject is provided.
        Valid subjects are: 'math', 'physics', 'chemistry', 'biology', 'english', 'history', 'geography', 'literature',
        'sport', and 'it'.
  Returns:
      str: The validated subject name entered by the user.
    """
    valid_subjects = ['math', 'physics', 'chemistry', 'biology', 'english', 'history', 'geography', 'literature',
                      'sport', 'it']
    print(valid_subjects)
    while True:
        subject = input("Enter name of the subject you want to select: ")
        if subject in valid_subjects:
            break
        else:
            print("Invalid input. Please try again!")

    return subject


def get_student_information():
    """
        Prompts the user for student information and performs basic validation.
    Returns:
      list: A list containing the student's information.
    """
    valid_genders = ["Male", "Female"]

    while True:
        first_name = input("First name: ").capitalize()
        last_name = input("Last name: ").capitalize()

        while True:
            gender = input("Gender (Male/Female): ").capitalize()
            if gender in valid_genders:
                break
            else:
                print("Invalid gender. Please enter 'Male' or 'Female'.")

        while True:
            birth_date = input("Date of birth(YYYY-MM-DD): ")
            if validate_date(birth_date):
                break
            else:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")

        parent_name = input("Parent First and Last name together: ").capitalize()
        city = input("Enter student's city: ").capitalize()
        address = input("Enter student's addres(street and number: ").capitalize()

        while True:
            student_email = input("Enter student's email: ").lower()
            if validate_email(student_email):
                break
            else:
                print("Invalid email format")

        while True:
            parent_email = input("Enter parent's email: ").lower()
            if validate_email(parent_email):
                break
            else:
                print("Invalid email format.")

        group = group_validation()

        return [first_name, last_name, gender, birth_date, parent_name, city, address, student_email, parent_email,
                group]


def validate_email(email):
    """
        Checks if the email format is valid.
    Args:
        email (str): The email address to validate.
    Returns:
        bool: True if the email format is likely valid, False otherwise.
    """

    if '@' not in email or '.' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    username_part, domain_part = parts
    if not username_part or not domain_part:
        return False
    if '.' not in domain_part:
        return False
    return True


def validate_date(date_str):
    """
        Checks if the date format is valid (YYYY-MM-DD).
    Args:
        date_str (str): The date string to validate.
    Returns:
        bool: True if the date format is valid, False otherwise.
    """

    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def get_grade_term1(df_students: pd.DataFrame, class_students: str, subject: str):
    """
        This function retrieves and prints the grades for a subject in Term 1 for a given class.
     Args:
      df_students (pd.DataFrame): The DataFrame with student information.
      class_students (str): The name of the class (group) to filter students from.
      subject (str): The subject which grades we want.
  Returns:
      None: Directly prints the results.
    """
    subject_to_sort = subject + '_t1_end'
    a = df_students[df_students['group'] == class_students]
    a.reset_index(drop=True, inplace=True)
    results = (a[['first_name', 'last_name', subject_to_sort]].sort_values(by=subject_to_sort, ascending=False))
    print(results.to_string(index=False))


def get_grade_term2(df_students: pd.DataFrame, class_students: str, subject: str):
    """
        This function retrieves and prints the grades for a subject in Term 2 for a given class.
     Args:
      df_students (pd.DataFrame): The DataFrame with student information.
      class_students (str): The name of the class (group) to filter students from.
      subject (str): The subject which grades we want.
  Returns:
      None: Directly prints the results.
    """
    subject_to_sort = subject + '_t2_end'
    a = df_students[df_students['group'] == class_students]
    a.reset_index(drop=True, inplace=True)
    results = (a[['first_name', 'last_name', subject_to_sort]].sort_values(by=subject_to_sort, ascending=False))
    print(results.to_string(index=False))


def get_grade_yearly(df_students: pd.DataFrame, class_students: str, subject: str):
    """
        This function retrieves and prints the yearly grades for a subject and given class.
     Args:
      df_students (pd.DataFrame): The DataFrame with student information.
      class_students (str): The name of the class (group) to filter students from.
      subject (str): The subject which grades we want.
  Returns:
      None: Directly prints the results.
  """
    subject_to_sort = subject + '_year'
    a = df_students[df_students['group'] == class_students]
    a.reset_index(drop=True, inplace=True)
    results = (a[['first_name', 'last_name', subject_to_sort]].sort_values(by=subject_to_sort, ascending=False))
    print(results.to_string(index=False))


def main():
    """
    Main function to provide user interaction.
    """
    try:
        df_students = pd.read_csv('students23.csv')
    except FileNotFoundError:
        "Error: 'students2023.csv' File not found. Please create it or provide the correct file path."

    new_students = []

    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. List All Students in same Group")
        print("5. List term 1 final grades for choosen group and subject")
        print("6. List term 2 final grades for choosen group and subject")
        print("7. List yearly grades for choosen group and subject")
        print("8. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            new_student_info = get_student_information()
            new_students.append(new_student_info)
            try:
                new_students.append(new_student_info)
                df = add_student(new_students, df_students)
                df.to_csv('students2023.csv', index=False)
            except ValueError:
                "Error adding student"
        elif choice == '2':
            first_name = input("Enter the student's first name to delete: ").capitalize()
            last_name = input("Enter the student's last name to delete: ").capitalize()
            try:
                df = delete_student(first_name, last_name, df_students)
                df.to_csv('students2023.csv', index=False)
            except ValueError:
                "Error deleting student"
        elif choice == '3':
            first_name = input("Enter the first name of the student: ").capitalize()
            last_name = input("Enter the last name of the student: ").capitalize()
            try:
                result = search_student(first_name, last_name, df_students)
                print(result[['first_name', 'last_name', 'student_email', 'birth_date', 'city', 'address', 'parent',
                              'parent_email']])
            except ValueError:
                "Please enter a valid student name."

        elif choice == '4':
            group_name = input("Enter the name of the group('group_a', group_b, 'group_c, 'group_d: ").lower()
            result = list_all_students_by_group(df_students, group_name)
            type_of_info = input("Choose type if info: 'main' or 'grades': ").lower()
            if type_of_info == 'main':
                print(result[['first_name', 'last_name', 'student_email', 'birth_date', 'city', 'address', 'parent',
                              'parent_email']])
        elif choice == '5':
            group_grades = group_validation()
            subjet_grades = subject_validation()
            get_grade_term1(df_students, group_grades, subjet_grades)
        elif choice == '6':
            group_grades = group_validation()
            subjet_grades = subject_validation()
            get_grade_term2(df_students, group_grades, subjet_grades)
        elif choice == '7':
            group_grades = group_validation()
            subjet_grades = subject_validation()
            get_grade_yearly(df_students, group_grades, subjet_grades)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
