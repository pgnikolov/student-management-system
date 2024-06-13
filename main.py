import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


def add_student(new_students: list, df):
    """
    Add a new student record to woorkbook.

    Args:
        df (pd.DataFrame): Student records.
        new_students (list): Student info
    Return:
        None
    """
    new_rows = pd.DataFrame(new_students, columns=df.columns[:10])

    # Fill missing columns with NaN
    for col in df.columns[10:]:
        new_rows[col] = pd.NA

    df = pd.concat([df, new_rows], ignore_index=True)

    return df


def delete_student(first_name_del: str, last_name_del: str, df):
    """
    Delete student record from dataframe.
    Args:
        first_name_del (str): Student's first name.
        last_name_del (str): Student's last name.
        df (pd.DataFrame): Student records.
    Return:
        df (pd.DataFrame): Students info without deleted record.
    """
    df = df[(df['first_name'] != first_name_del) | (df['last_name'] != last_name_del)]
    return df


def search_student(first_name_search: str, last_name_search: str, df):
    """
        This function searches for a student in the students Excel file by name.
    Args:
        first_name_search (str): Student's first name.
        last_name_search (str): Student's last name.
        df (pd.DataFrame): Student records.
    Return:
        result (pd.DataFrame): Students filtered by user criteria.
    """
    result = df[(df['first_name'] == first_name_search) & (df['last_name'] == last_name_search)]

    return result


def list_all_students_by_group(df, class_students: str):
    """
        Print all students who are in same group (class).
    Args:
        df (pd.DataFrame): Student records.
        class_students (str): The group(class) students we want.
    Return:
        result (pd.DataFrame): Students filtered by user criteria.
    """
    result = df[df['group'] == class_students]

    return result


def main():
    """
    Main function to provide user interaction.
    """
    df_students = pd.read_csv('students2023.csv')
    new_students = []
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. List All Students in same Group")
        print("5. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            new_student = [input("First name: ").capitalize(), input("Last name: ").capitalize(),
                           input("Gender (Male/Female): ").capitalize(), input("Date of birth(YYYY-MM-DD): "),
                           input("Parent First and Last name together: ").capitalize(),
                           input("Enter student's city: ").capitalize(),
                           input("Enter student's addres(street and number: ").capitalize(),
                           input("Enter student's email: ").lower(), input("Enter parent's email: ").lower(),
                           input("Enter student's group(group_a, group_b, group_c or group_d: ").lower()]

            new_students.append(new_student)
            df = add_student(new_students, df_students)
            df.to_csv('students2023.csv', index=False)
        elif choice == '2':
            first_name = input("Enter the student's first name to delete: ").capitalize()
            last_name = input("Enter the student's last name to delete: ").capitalize()
            df = delete_student(first_name, last_name, df_students)
            df.to_csv('students2023.csv', index=False)
        elif choice == '3':
            first_name = input("Enter the first name of the student: ").capitalize()
            last_name = input("Enter the last name of the student: ").capitalize()
            result = search_student(first_name, last_name, df_students)
            type_of_info = input(
                "What type of information do you want ('main ' or 'grades')?: ").lower()
            if type_of_info == 'main':
                print(result[['first_name', 'last_name', 'student_email', 'birth_date', 'city', 'address', 'parent', 'parent_email']])
            elif type_of_info == 'grades':
                print("Subjects: math, physics, chemistry, biology,english, history, geography, literature, sport, it")
                subjet = input("Enter the name of the subjesct: ").lower()
                subjet_cols = [col for col in result.columns if subjet in col]
                print(result[subjet_cols])
        elif choice == '4':
            group_name = input("Enter the name of the group('group_a', group_b, 'group_c, 'group_d: ").lower()
            result = list_all_students_by_group(df_students, group_name)
            type_of_info = input("Choose type if info: 'main' or 'grades': ").lower()
            if type_of_info == 'main':
                print(result[['first_name', 'last_name', 'student_email', 'birth_date', 'city', 'address', 'parent',
                              'parent_email']])
            elif type_of_info == 'grades':
                grade_type = input("Which grades do you need? Enter 't1' first term or t2 for second term: ").lower()
                print("Subjects: math, physics, chemistry, biology,english, history, geography, literature, sport, it")
                subjet = input("Enter the name of the subjesct: ").lower()
                filter_param = subjet + "_" + grade_type
                subjet_cols = [col for col in result.columns if filter_param in col]
                all_cols = ['first_name', 'last_name'] + subjet_cols
                print(result[all_cols])
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
