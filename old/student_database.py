import pandas as pd
import matplotlib.pyplot as plt


class StudentDatabase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df_students = self.load_data()

    def load_data(self):
        try:
            return pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Error: '{self.file_path}' file not found. Please create it or provide the correct file path.")
            return pd.DataFrame(columns=[
                'first_name', 'last_name', 'gender', 'birth_date', 'parent_name', 'city', 'address',
                'student_email', 'parent_email', 'group'
            ])

    def save_data(self):
        self.df_students.to_csv(self.file_path, index=False)

    def add_student(self, student):
        new_row = pd.DataFrame([student.to_dict()])
        self.df_students = pd.concat([self.df_students, new_row], ignore_index=True)
        self.save_data()

    def delete_student(self, first_name, last_name):
        self.df_students = self.df_students[
            (self.df_students['first_name'] != first_name) | (self.df_students['last_name'] != last_name)
            ]
        self.save_data()

    def search_student(self, first_name, last_name):
        result = self.df_students[
            (self.df_students['first_name'] == first_name) & (self.df_students['last_name'] == last_name)
            ]
        if result.empty:
            raise ValueError(f"No student with names '{first_name} {last_name}' found.")
        return result

    def list_students_by_group(self, group):
        return self.df_students[self.df_students['group'] == group]

    def get_grade_term(self, class_students, subject, grade_year, sch_year, term):
        subject_to_sort = f'{subject}_year{grade_year}_t{term}_end'
        students = self.df_students[
            (self.df_students['group'] == class_students) & (self.df_students['year_in_school'] == sch_year)
            ]
        students.reset_index(drop=True, inplace=True)
        results = students[['first_name', 'last_name', subject_to_sort]].sort_values(by=subject_to_sort,
                                                                                     ascending=False)
        print(results.to_string(index=False))

    def get_yearly_grade(self, class_students, subject, grade_year, sch_year):
        subject_to_sort = f'{subject}_year{grade_year}'
        students = self.df_students[
            (self.df_students['group'] == class_students) & (self.df_students['year_in_school'] == sch_year)
            ]
        students.reset_index(drop=True, inplace=True)
        results = students[['first_name', 'last_name', subject_to_sort]].sort_values(by=subject_to_sort,
                                                                                     ascending=False)
        print(results.to_string(index=False))

    def yearly_grade_distribution(self, year_in_school, grade_year, subject):
        df_year = self.df_students[self.df_students['year_in_school'] == year_in_school].dropna(axis=1)

        for col in df_year.columns:
            if col.endswith(f'_year{grade_year}'):
                df_year[col + '_gn'] = df_year[col].apply(StudentDatabase.grade_name)

        group_arg = f'{subject}_year{grade_year}_gn'
        df_year_groups = df_year.groupby(['group', group_arg])
        groups_count = df_year_groups.size()

        plt.figure(figsize=(8, 8))
        plt.suptitle(f"Distribution of {subject.capitalize()} Yearly Grades", fontsize=22)
        groups = ['A', 'B', 'C', 'D']
        for i, group in enumerate(groups, 1):
            plt.subplot(2, 2, i)
            plt.title(f'"{group}" {subject} Year {grade_year} Grades')
            if group in groups_count:
                plt.pie(groups_count[group], labels=groups_count[group].index, autopct='%1.1f%%')

        plt.show()

    @staticmethod
    def grade_name(grade):
        if grade < 3.50:
            return 'Average'
        elif 3.50 <= grade < 4.50:
            return 'Good'
        elif 4.50 <= grade < 5.50:
            return 'Very good'
        else:
            return 'Excellent'
