class Student:
    def __init__(self, first_name, last_name, address, parent_name, parent_email, parent_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.parent_name = parent_name
        self.parent_email = parent_email
        self.parent_phone = parent_phone
        self.grades = {subject: {"term1": [], "term2": []} for subject in SUBJECTS}

    def add_grade(self, subject, term, grade):
        if subject in self.grades:
            self.grades[subject][term].append(grade)

    def get_final_grade(self, subject):
        if subject in self.grades:
            term1_avg = sum(self.grades[subject]["term1"]) / len(self.grades[subject]["term1"])
            term2_avg = sum(self.grades[subject]["term2"]) / len(self.grades[subject]["term2"])
            return (term1_avg + term2_avg) / 2


SUBJECTS = ['math', 'physics', 'chemistry', 'biology', 'english', 'history', 'geography', 'literature', 'sport', 'it']
