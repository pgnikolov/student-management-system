class InputValidation:
    @staticmethod
    def subject_validation():
        valid_subjects = ['math', 'physics', 'chemistry', 'biology', 'english', 'history', 'geography', 'literature',
                          'sport', 'it']
        print(valid_subjects)
        while True:
            subject = input("Enter name of the subject you want to select: ").lower()
            if subject in valid_subjects:
                break
            else:
                print("Invalid input. Please try again!")
        return subject

    @staticmethod
    def yearly_grade_validation():
        valid_years = [1, 2, 3, 4]
        while True:
            year = input("Enter grade's year (1, 2, 3, or 4): ")
            if year.isdigit() and int(year) in valid_years:
                break
            else:
                print("Invalid year. Please enter '1', '2', '3', or '4'.")
        return int(year)

    @staticmethod
    def year_validation():
        valid_years = [0, 1, 2, 3]
        while True:
            year = input("Enter student's year (0, 1, 2, or 3): ")
            if year.isdigit() and int(year) in valid_years:
                break
            else:
                print("Invalid year. Please enter '0', '1', '2', or '3'.")
        return int(year)
