import pandas as pd
import random
import math

file_path = "your_file.csv"
# if you want to save generated grade to other file
file_save = 'file-to-save.csv'

df = pd.read_csv(file_path)


def calculate_end_grade(row, subject):
    t1_grades = [row[f"{subject}_t1_{i}"] for i in range(1, 4) if not pd.isna(row[f"{subject}_t1_{i}"])]
    t2_grades = [row[f"{subject}_t2_{i}"] for i in range(1, 4) if not pd.isna(row[f"{subject}_t2_{i}"])]
    if not t1_grades or not t2_grades:
        return math.nan, math.nan
    t1_avg = sum(t1_grades) / len(t1_grades)
    t2_avg = sum(t2_grades) / len(t2_grades)
    return math.ceil(t1_avg), math.ceil(t2_avg)


def fill_missing_grades(row, subject):
    for i in range(1, 4):
        if pd.isnull(row[f"{subject}_t1_{i}"]):
            row[f"{subject}_t1_{i}"] = random.randint(3, 6)
        if pd.isnull(row[f"{subject}_t2_{i}"]):
            row[f"{subject}_t2_{i}"] = random.randint(3, 6)
    return row


subjects = ['math', 'physics', 'chemistry', 'biology', 'english', 'history', 'geography', 'literature', 'sport', 'it']
for subject in subjects:
    df = df.apply(lambda row: fill_missing_grades(row, subject), axis=1)
    df[[f"{subject}_t1_end", f"{subject}_t2_end"]] = df.apply(lambda row: pd.Series(calculate_end_grade(row, subject)),
                                                              axis=1)

# Save the updated DataFrame to a new CSV file
df.to_csv("file_save.csv", index=False)

df_fill_year = pd.read_csv("students23.csv")

# Calculate the average of t1_end and t2_end for each subject
for subject in ["math", "physics", "chemistry", "biology", "english", "history", "geography", "literature", "sport",
                "it"]:
    t1_end_col = f"{subject}_t1_end"
    t2_end_col = f"{subject}_t2_end"
    year_col = f"{subject}_year"

    # Calculate the average for each row
    df_fill_year[year_col] = (df_fill_year[t1_end_col] + df_fill_year[t2_end_col]) / 2

df_fill_year.to_csv("file_save.csv", index=False)
