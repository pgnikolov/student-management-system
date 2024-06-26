from datetime import datetime


class Student:
    def __init__(self, first_name, last_name, gender, birth_date, parent_name, city, address, student_email, parent_email, group):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_date = birth_date
        self.parent_name = parent_name
        self.city = city
        self.address = address
        self.student_email = student_email
        self.parent_email = parent_email
        self.group = group

    @staticmethod
    def from_input():
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
                if Student.validate_date(birth_date):
                    break
                else:
                    print("Invalid date format. Please enter in YYYY-MM-DD format.")

            parent_name = input("Parent First and Last name together: ").capitalize()
            city = input("Enter student's city: ").capitalize()
            address = input("Enter student's address (street and number): ").capitalize()

            while True:
                student_email = input("Enter student's email: ").lower()
                if Student.validate_email(student_email):
                    break
                else:
                    print("Invalid email format")

            while True:
                parent_email = input("Enter parent's email: ").lower()
                if Student.validate_email(parent_email):
                    break
                else:
                    print("Invalid email format.")

            group = Student.group_validation()

            return Student(first_name, last_name, gender, birth_date, parent_name, city, address, student_email, parent_email, group)

    @staticmethod
    def validate_email(email):
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

    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def group_validation():
        valid_groups = ["A", "B", "C", "D"]

        while True:
            group = input("Enter student's group (A, B, C, or D): ").upper()
            if group in valid_groups:
                break
            else:
                print("Invalid group. Please enter 'A', 'B', 'C', or 'D'.")

        return group

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'birth_date': self.birth_date,
            'parent_name': self.parent_name,
            'city': self.city,
            'address': self.address,
            'student_email': self.student_email,
            'parent_email': self.parent_email,
            'group': self.group
        }

