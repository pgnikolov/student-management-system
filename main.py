import pandas as pd
import matplotlib.pyplot as plt
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
    new_rows = pd.DataFrame(new_students, columns=df_students.columns)
    try:
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
    valid_groups = ["A", "B", "C", "D"]

    while True:
        group = input("Enter student's group (A, B, C, or D): ").upper()
        if group in valid_groups:
            break
        else:
            print("Invalid group. Please enter 'A', 'B', 'C', or 'D'.")

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


def yearly_grade_validation() -> int:
    """
    Prompts the user to enter a year fo grade, until a valid year is provided.
    Valid years are: 1, 2, 3, and 4.
    Returns:
        int: The validated student year entered by the user.
    """
    valid_years = [1, 2, 3, 4]
    while True:
        year = input("Enter grade's year (1, 2, 3, or 4): ")
        if year.isdigit() and int(year) in valid_years:
            break
        else:
            print("Invalid year. Please enter '1', '2', '3', or '4'.")

    return int(year)


def year_validation() -> int:
    """
    Prompts the user to enter a student's year in school until a valid year is provided.
    Valid years are: 0, 1, 2, and 3.
    Returns:
        int: The validated student year entered by the user.
    """
    valid_years = [0, 1, 2, 3]
    while True:
        year = input("Enter student's year (0, 1, 2, or 3): ")
        if year.isdigit() and int(year) in valid_years:
            break
        else:
            print("Invalid year. Please enter '0', '1', '2', or '3'.")

    return int(year)


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


def get_grade_term1(df_students: pd.DataFrame, class_students: str, subject: str, grade_year: int, sch_year: int):
    """
        This function retrieves and prints the grades for a subject in Term 1 for a given class.
     Args:
      df_students (pd.DataFrame): The DataFrame with student information.
      class_students (str): The name of the class (group) to filter students from.
      subject (str): The subject which grades we want.
      grade_year (int): Year of grade
      sch_year (int): Year student in school
  Returns:
      None: Directly prints the results.
    """
    subject_to_sort = f'{subject}_year{grade_year}_t1_end'
    a = df_students[(df_students['group'] == class_students) & (df_students['year_in_school'] == sch_year)]
    a.reset_index(drop=True, inplace=True)
    results = (a[['student_first_name', 'student_last_name', subject_to_sort]].sort_values(by=subject_to_sort,
                                                                                           ascending=False))
    print(results.to_string(index=False))


def get_grade_term2(df_students: pd.DataFrame, class_students: str, subject: str, grade_year: int, sch_year: int):
    """
        This function retrieves and prints the grades for a subject in Term 2 for a given class.
     Args:
      df_students (pd.DataFrame): The DataFrame with student information.
      class_students (str): The name of the class (group) to filter students from.
      subject (str): The subject which grades we want.
      grade_year (int): Year of grade
      sch_year (int): Year student in school
  Returns:
      None: Directly prints the results.
    """
    subject_to_sort = f'{subject}_year{grade_year}_t2_end'
    a = df_students[(df_students['group'] == class_students) & (df_students['year_in_school'] == sch_year)]
    a.reset_index(drop=True, inplace=True)
    results = (a[['student_first_name', 'student_last_name', subject_to_sort]].sort_values(by=subject_to_sort,
                                                                                           ascending=False))
    print(results.to_string(index=False))


def get_grade_yearly(df_students: pd.DataFrame, class_students: str, subject: str, grade_year: int, sch_year: int):
    """
        This function retrieves and prints the yearly grades for a subject and given class.
    Args:
      df_students (pd.DataFrame): The DataFrame with student information.
      class_students (str): The name of the class (group) to filter students from.
      subject (str): The subject which grades we want.
      grade_year (int): Year of grade
      sch_year (int): Year student in school
    Returns:
      None: Directly prints the results.
  """
    subject_to_sort = f'{subject}_year{grade_year}'
    a = df_students[(df_students['group'] == class_students) & (df_students['year_in_school'] == sch_year)]
    a.reset_index(drop=True, inplace=True)
    results = (a[['student_first_name', 'student_last_name', subject_to_sort]].sort_values(by=subject_to_sort,
                                                                                           ascending=False))
    print(results.to_string(index=False))


def get_year_data(df: pd.DataFrame, year_in_school: int) -> pd.DataFrame:
    """
    Args:
        df: pd.DataFrame
        year_in_school: int
    Return:
        df: pd.DataFrame
    """
    df_year = df[df['year_in_school'] == year_in_school]
    return df_year


def get_group_data(df: pd.DataFrame, year_in_school: int, group: str) -> pd.DataFrame:
    """
        Args:
        df: pd.DataFrame
        year_in_school: int
    Return:
        df: pd.DataFrame
    """

    df_year = get_year_data(df, year_in_school)
    df_group = df_year[df_year['group'] == group]
    return df_group


def grade_name(grade):
    if grade < 3.50:
        return 'Average'
    elif 3.50 <= grade < 4.50:
        return 'Good'
    elif 4.50 <= grade < 5.50:
        return 'Very good'
    else:
        return 'Excellent'


def yearly_grade_dist_subject(df: pd.DataFrame, year_in_school: int, grade_year: int, subject: str):
    """
        Generates a pie chart showing the distribution of yearly grades for a specified subject and grade year.

        This function processes the provided DataFrame to filter data for the specified year in school,
        calculates grade names for the specified subject and grade year, groups the data by grade names and
        student groups, and then plots pie charts representing the distribution of grades for each student group.
    Args:
        df (pd.DataFrame): The DataFrame containing student grades and other information.
        year_in_school (int): The year in school (0, 1, 2, 3)
        grade_year (int): The specific grade year within the subject (1, 2, 3, 4).
        subject (str): The subject for which to analyze and plot the grade distribution (e.g., 'math').
    Returns:
        None: The function generates and displays pie charts but does not return any value.
    """
    dfyear = get_year_data(df, year_in_school)
    dfyear = dfyear.dropna(axis=1)

    for col in dfyear.columns:
        if col.endswith(f'_year{grade_year}'):
            dfyear[col + '_gn'] = df[col].apply(grade_name)

    group_arg = f'{subject}_year{grade_year}_gn'
    dfyear_groups = dfyear.groupby(['group', group_arg])
    groups_count = dfyear_groups.size()

    plt.figure(figsize=(8, 8))
    plt.suptitle(f"Distribution of {subject.capitalize()} Yearly Grades", fontsize=22)
    plt.subplot(2, 2, 1)
    plt.title(f'"A" {subject} Year {grade_year} Grades')
    plt.pie(groups_count['A'], labels=groups_count['A'].index, autopct='%1.1f%%')
    plt.subplot(2, 2, 2)
    plt.title(f'"B" {subject} Year {grade_year} Grades')
    plt.pie(groups_count['B'], labels=groups_count['B'].index, autopct='%1.1f%%')
    plt.subplot(2, 2, 3)
    plt.title(f'"C" {subject} Year {grade_year} Grades')
    plt.pie(groups_count['C'], labels=groups_count['C'].index, autopct='%1.1f%%')
    plt.subplot(2, 2, 4)
    plt.title(f'"D" {subject} Year {grade_year} Grades')
    plt.pie(groups_count['D'], labels=groups_count['D'].index, autopct='%1.1f%%')

    plt.show()


def main():
    try:
        df_students = pd.read_csv('school_database.csv')
    except FileNotFoundError:
        "Error: 'school_database.csv' File not found. Please create it or provide the correct file path."

    new_students = []

    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. List All Students in same Group")
        print("5. List term 1 final grades for chosen group, subject, and year")
        print("6. List term 2 final grades for chosen group, subject, and year")
        print("7. List yearly grades for chosen group, subject, and year")
        print("8. Distribution of Subject Yearly Grades by Groups")
        print("9. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            new_student_info = get_student_information()
            new_students.append(new_student_info)
            try:
                new_students.append(new_student_info)
                df = add_student(new_students, df_students)
                df.to_csv('school_database.csv', index=False)
            except ValueError:
                "Error adding student"
        elif choice == '2':
            first_name = input("Enter the student's first name to delete: ").capitalize()
            last_name = input("Enter the student's last name to delete: ").capitalize()
            try:
                df = delete_student(first_name, last_name, df_students)
                df.to_csv('school_database.csv', index=False)
            except ValueError:
                "Error deleting student"
        elif choice == '3':
            first_name = input("Enter the first name of the student: ").capitalize()
            last_name = input("Enter the last name of the student: ").capitalize()
            try:
                result = search_student(first_name, last_name, df_students)
                print(result[
                          ['student_first_name', 'student_last_name', 'student_email', 'birth_date', 'city', 'address',
                           'parent',
                           'parent_email']])
            except ValueError:
                "Please enter a valid student name."

        elif choice == '4':
            group_name = input("Enter the name of the group (A, B, C, or D): ").upper()
            result = list_all_students_by_group(df_students, group_name)
            type_of_info = input("Choose type if info: 'main' or 'grades': ").lower()
            if type_of_info == 'main':
                print(result[
                          ['student_first_name', 'student_last_name', 'student_email', 'birth_date', 'city', 'address',
                           'parent',
                           'parent_email']])
        elif choice == '5':
            year_in_school = year_validation()
            grade_year = yearly_grade_validation()
            group_grades = group_validation()
            subject_grades = subject_validation()
            get_grade_term1(df_students, group_grades, subject_grades, grade_year, year_in_school)
        elif choice == '6':
            year_in_school = year_validation()
            grade_year = yearly_grade_validation()
            group_grades = group_validation()
            subject_grades = subject_validation()
            get_grade_term2(df_students, group_grades, subject_grades, grade_year, year_in_school)
        elif choice == '7':
            year_in_school = year_validation()
            grade_year = yearly_grade_validation()
            group_grades = group_validation()
            subject_grades = subject_validation()
            get_grade_yearly(df_students, group_grades, subject_grades, grade_year, year_in_school)
        elif choice == "8":
            year_in_shool = year_validation()
            grade_year = yearly_grade_validation()
            subject = subject_validation()
            yearly_grade_dist_subject(df_students, year_in_shool, grade_year, subject)
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
