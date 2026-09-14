"""
Student Score Tracker

Description:
This program processes student exam records and generates a
summary report containing student and subject-level statistics.

Report Includes:
- Student averages
- Top-scoring student
- Lowest-scoring student
- Subject averages
- Hardest subject
- Easiest subject
- Passed students
- Failed students
"""


# ===============================================
# Step 1: Student Record Data
# ===============================================

records = [
    ("Ravi",  "Math",    80),
    ("Ravi",  "Science", 85),
    ("Ravi",  "English", 90),
    ("Priya", "Math",    25),
    ("Priya", "Science", 30),
    ("Priya", "English", 20),
    ("Kumar", "Math",    10),
    ("Kumar", "Science", 15),
    ("Kumar", "English", 12),
]

PASS_MARKS = 40


# ===============================================
# Step 2: Convert Records into Dictionaries
# ===============================================

keys = ("name", "subject", "marks")

student_records = []

for record in records:
    student_records.append(dict(zip(keys, record)))


# ===============================================
# Step 3: Find Unique Students and Subjects
# ===============================================

student_names = []
subjects = []

for record in student_records:

    if record["name"] not in student_names:
        student_names.append(record["name"])

    if record["subject"] not in subjects:
        subjects.append(record["subject"])


# ===============================================
# Utility Functions
# ===============================================

def print_averages(averages):
    """Display name/subject averages."""
    for average in averages:
        print(f"{average[0]:<8}: {average[1]:.2f}")


def print_high_and_low_rates(
    highest_value,
    highest_name,
    lowest_value,
    lowest_name
):
    """Display the highest and lowest result."""
    print(
        f"\n{highest_name}: "
        f"{highest_value[0]} ({highest_value[1]:.2f})"
    )
    print(
        f"{lowest_name}: "
        f"{lowest_value[0]} ({lowest_value[1]:.2f})"
    )


def descending_sort(data, index):
    """Sort records by the selected index in descending order."""
    return sorted(data, key=lambda item: item[index], reverse=True)


def display_students_category(category_name, students, compare_type):
    """Display passed or failed students."""
    print(
        f"\n--- {category_name} Students "
        f"(Average {compare_type} {PASS_MARKS}) ---"
    )

    if not students:
        print("None")
    else:
        for student in students:
            print(f"{student[0]:<8}: {student[1]:.2f}")


def calculate_average(records, key, value):
    """Calculate the average marks for a given student or subject."""
    total_marks = 0
    count = 0

    for record in records:

        if record[key] == value:
            total_marks += record["marks"]
            count += 1

    return round(total_marks / count, 2) if count > 0 else 0


# ===============================================
# Step 4: Calculate Student Averages
# ===============================================

student_averages = []

for name in student_names:
    average = calculate_average(
        student_records,
        "name",
        name
    )

    student_averages.append([name, average])

student_averages = descending_sort(student_averages, 1)


# ===============================================
# Step 5: Display Student Results
# ===============================================

print(
    "\n========== SUMMARY REPORT OF STUDENT "
    "and SUBJECT MARKS ==========\n"
)

print("--- Student Averages ---")
print_averages(student_averages)

top_student = student_averages[0]
lowest_student = student_averages[-1]

print_high_and_low_rates(
    top_student,
    "Top Student",
    lowest_student,
    "Lowest Student"
)


# ===============================================
# Step 6: Calculate Subject Averages
# ===============================================

subject_averages = []

for subject in subjects:
    average = calculate_average(
        student_records,
        "subject",
        subject
    )

    subject_averages.append([subject, average])

subject_averages = descending_sort(subject_averages, 1)


# ===============================================
# Step 7: Display Subject Results
# ===============================================

print("\n--- Subject Averages ---")
print_averages(subject_averages)

easiest_subject = subject_averages[0]
hardest_subject = subject_averages[-1]

print_high_and_low_rates(
    easiest_subject,
    "Easiest Subject",
    hardest_subject,
    "Hardest Subject"
)


# ===============================================
# Step 8: Separate Passed and Failed Students
# ===============================================

passed_students = []
failed_students = []

for student in student_averages:

    if student[1] >= PASS_MARKS:
        passed_students.append(student)
    else:
        failed_students.append(student)


# ===============================================
# Step 9: Display Passed Students
# ===============================================

display_students_category(
    "Passed",
    passed_students,
    ">="
)


# ===============================================
# Step 10: Display Failed Students
# ===============================================

display_students_category(
    "Failed",
    failed_students,
    "<"
)

print()
