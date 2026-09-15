# Problem 11 — Student Score Tracker

## Problem Statement

A school stores exam records for multiple students across multiple subjects. Each record is represented as:

```text
(student, subject, score)
```

Build a program that processes the records and generates a student-wise and subject-wise summary.

## Input Data

```python
records = [
    ("Ravi",   "Math",    78),
    ("Anjali", "Math",    92),
    ("Ravi",   "Science", 65),
    ("Priya",  "Math",    55),
    ("Anjali", "Science", 88),
    ("Priya",  "Science", 40),
    ("Ravi",   "English", 50),
    ("Anjali", "English", 95),
    ("Priya",  "English", 33),
]
```

## Required Output

Calculate and report:

1. The average score for every student.
2. The top-scoring student and their average.
3. The average score for every subject.
4. The hardest subject, meaning the subject with the lowest average.
5. Students whose average score is strictly below 40.

## Expected Output

```text
--- Student Averages ---
Anjali  : 91.67
Ravi    : 64.33
Priya   : 42.67

Top Scorer: Anjali (91.67)

--- Subject Averages ---
Math    : 75.0
Science : 64.33
English : 59.33

Hardest Subject: English (59.33)

--- Failed Students (Average < 40) ---
None
```

## Constraints

- A student fails only when their average is strictly less than 40.
- Round averages to 2 decimal places for calculations/output where decimal formatting is shown.
- Students must be sorted by average from highest to lowest.
- Subjects must be sorted by average from highest to lowest.
- For equal averages, any consistent tie order is acceptable.

## Test Cases

Every test case below reports all required results using the same section names as the main expected output.

### Test Case 1 — Normal case

**Input**
```python
records = [
    ("Ravi",   "Math",    78),
    ("Anjali", "Math",    92),
    ("Ravi",   "Science", 65),
    ("Priya",  "Math",    55),
    ("Anjali", "Science", 88),
    ("Priya",  "Science", 40),
    ("Ravi",   "English", 50),
    ("Anjali", "English", 95),
    ("Priya",  "English", 33),
]
```

**Expected Output**
```text
--- Student Averages ---
Anjali  : 91.67
Ravi    : 64.33
Priya   : 42.67

Top Scorer: Anjali (91.67)

--- Subject Averages ---
Math    : 75.0
Science : 64.33
English : 59.33

Hardest Subject: English (59.33)

--- Failed Students (Average < 40) ---
None
```

### Test Case 2 — One student fails

**Input**
```python
records = [
    ("Ravi",   "Math",    78),
    ("Anjali", "Math",    92),
    ("Kumar",  "Math",    20),
    ("Ravi",   "Science", 65),
    ("Anjali", "Science", 88),
    ("Kumar",  "Science", 15),
    ("Ravi",   "English", 50),
    ("Anjali", "English", 95),
    ("Kumar",  "English", 10),
]
```

**Expected Output**
```text
--- Student Averages ---
Anjali : 91.67
Ravi   : 64.33
Kumar  : 15.00

Top Scorer: Anjali (91.67)

--- Subject Averages ---
Math    : 63.33
Science : 56.0
English : 51.67

Hardest Subject: English (51.67)

--- Failed Students (Average < 40) ---
Kumar : 15.00
```

### Test Case 3 — Equal student averages

**Input**
```python
records = [
    ("A", "Math", 70),
    ("B", "Math", 70),
    ("C", "Math", 70),
]
```

**Expected Output**
```text
--- Student Averages ---
A : 70.00
B : 70.00
C : 70.00

Top Scorer: A (70.00)

--- Subject Averages ---
Math : 70.00

Hardest Subject: Math (70.00)

--- Failed Students (Average < 40) ---
None
```

Any consistent order among the equal-average students is acceptable.

### Test Case 4 — Boundary: average exactly 40 does not fail

**Input**
```python
records = [
    ("Ravi", "Math", 40),
    ("Ravi", "Science", 40),
    ("Anjali", "Math", 80),
    ("Anjali", "Science", 80),
]
```

**Expected Output**
```text
--- Student Averages ---
Anjali : 80.00
Ravi   : 40.00

Top Scorer: Anjali (80.00)

--- Subject Averages ---
Math    : 60.00
Science : 60.00

Hardest Subject: Math (60.00)

--- Failed Students (Average < 40) ---
None
```

Math and Science have equal averages, so either subject may be reported as the hardest subject if the tie is handled consistently.

### Test Case 5 — Multiple failing students

**Input**
```python
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
```

**Expected Output**
```text
--- Student Averages ---
Ravi  : 85.00
Priya : 25.00
Kumar : 12.33

Top Scorer: Ravi (85.00)

--- Subject Averages ---
Science : 43.33
English : 40.67
Math    : 38.33

Hardest Subject: Math (38.33)

--- Failed Students (Average < 40) ---
Priya : 25.00
Kumar : 12.33
```
