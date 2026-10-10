
import pandas as pd
import numpy as np
from contextlib import redirect_stdout
# Read student data
df = pd.read_csv("students.csv")

subjects = ["Python", "SQL", "Maths"]

# Calculate total and average using NumPy
df["Total"] = np.sum(df[subjects].to_numpy(), axis=1)
df["Average"] = np.mean(df[subjects].to_numpy(), axis=1).round(2)

# Grade calculation function
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "E"

# Pass/Fail calculation function
def calculate_result(row):
    if any(row[subject] < 40 for subject in subjects):
        return "Fail"
    return "Pass"

df["Grade"] = df["Average"].apply(calculate_grade)
df["Result"] = df.apply(calculate_result, axis=1)

# Display student report
print("\nSTUDENT PERFORMANCE REPORT")
print(df[["Name", "Total", "Average", "Grade", "Result"]].to_string(index=False))

# Overall analysis
print("\nOVERALL ANALYSIS")
print("Number of Students:", len(df))
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Total:", df["Total"].max())
print("Lowest Total:", df["Total"].min())
print("Pass Count:", (df["Result"] == "Pass").sum())
print("Fail Count:", (df["Result"] == "Fail").sum())

# Subject-wise analysis
print("\nSUBJECT-WISE AVERAGE")
for subject in subjects:
    print(subject, ":", round(df[subject].mean(), 2))

# Top 3 students
print("\nTOP 3 STUDENTS")
top_students = df.nlargest(3, "Total")
print(top_students[["Name", "Total", "Average"]].to_string(index=False))
