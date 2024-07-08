import pandas as pd
from input_validation import InputValidation
from student import Student
from student_database import StudentDatabase

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


class StudentManagementSystem:
    def __init__(self, db_path):
        self.db = StudentDatabase(db_path)

    def run(self):
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. Delete Student")
            print("3. Search Student")
            print("4. List Students by Group")
            print("5. Get Grade Term")
            print("6. Get Yearly Grade")
            print("7. Yearly Grade Distribution")
            print("8. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                student = Student.from_input()
                self.db.add_student(student)
            elif choice == '2':
                first_name = input("Enter first name of the student to delete: ").capitalize()
                last_name = input("Enter last name of the student to delete: ").capitalize()
                self.db.delete_student(first_name, last_name)
            elif choice == '3':
                first_name = input("Enter first name of the student to search: ").capitalize()
                last_name = input("Enter last name of the student to search: ").capitalize()
                try:
                    student_info = self.db.search_student(first_name, last_name)
                    print(student_info)
                except ValueError as e:
                    print(e)
            elif choice == '4':
                group = input("Enter group to list students: ").upper()
                print(self.db.list_students_by_group(group))
            elif choice == '5':
                class_students = input("Enter the class group: ").upper()
                subject = InputValidation.subject_validation()
                grade_year = InputValidation.yearly_grade_validation()
                sch_year = InputValidation.year_validation()
                term = input("Enter the term: ")
                self.db.get_grade_term(class_students, subject, grade_year, sch_year, term)
            elif choice == '6':
                class_students = input("Enter the class group: ").upper()
                subject = InputValidation.subject_validation()
                grade_year = InputValidation.yearly_grade_validation()
                sch_year = InputValidation.year_validation()
                self.db.get_yearly_grade(class_students, subject, grade_year, sch_year)
            elif choice == '7':
                year_in_school = InputValidation.year_validation()
                grade_year = InputValidation.yearly_grade_validation()
                subject = InputValidation.subject_validation()
                self.db.yearly_grade_distribution(year_in_school, grade_year, subject)
            elif choice == '8':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    sms = StudentManagementSystem('school_database.csv')
    sms.run()
