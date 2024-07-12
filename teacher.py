class Teacher:
    def __init__(self, first_name, last_name, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject

    def __repr__(self):
        print(f"{self.first_name} {self.last_name} is teaching {self.subject}.")
