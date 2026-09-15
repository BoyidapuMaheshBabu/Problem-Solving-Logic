# Problem 10 — Department Payroll Breakdown

## Problem Statement

Process payroll grouped by department and generate a department-wise summary report.

Each employee record contains a name, department, hours worked, and hourly rate.

## Salary Rules

- Up to 40 hours: paid at the normal hourly rate.
- Hours beyond 40: paid at 1.5× the normal hourly rate.

## Report Requirements

For each department, calculate and report:

- Individual salary for every employee in that department.
- Total department payroll.
- Highest-paid employee in the department.
- Lowest-paid employee in the department.

## Input/Data

```python
employees = [
    {"name": "Ravi",  "dept": "Engineering", "hours": 45, "rate": 200},
    {"name": "Sita",  "dept": "Engineering", "hours": 38, "rate": 250},
    {"name": "Arjun", "dept": "Marketing",   "hours": 50, "rate": 180},
    {"name": "Divya", "dept": "Marketing",   "hours": 40, "rate": 220},
    {"name": "Kiran", "dept": "HR",          "hours": 35, "rate": 300},
    {"name": "Meena", "dept": "HR",          "hours": 42, "rate": 270},
]
```

## Expected Output

```text
=== Engineering ===
Ravi  : ₹9500.00
Sita  : ₹9500.00
Total : ₹19000.00
Highest paid: Ravi
Lowest paid : Sita

=== Marketing ===
Arjun : ₹9900.00
Divya : ₹8800.00
Total : ₹18700.00
Highest paid: Arjun
Lowest paid : Divya

=== HR ===
Kiran : ₹10500.00
Meena : ₹11610.00
Total : ₹22110.00
Highest paid: Meena
Lowest paid : Kiran
```

## Constraints

- Departments must be discovered dynamically from the data; do not hardcode department names.
- Overtime rate is exactly 1.5× the normal hourly rate.
- Only hours beyond 40 count as overtime.
- If two employees have equal salary, either tied employee may be reported consistently as highest or lowest as appropriate.

## Test Cases

Every test case below uses the same complete department report structure.

### Test Case 1 — Multiple departments with regular and overtime employees

**Input**
```python
employees = [
    {"name": "Ravi",  "dept": "Engineering", "hours": 45, "rate": 200},
    {"name": "Sita",  "dept": "Engineering", "hours": 38, "rate": 250},
    {"name": "Arjun", "dept": "Marketing",   "hours": 50, "rate": 180},
    {"name": "Divya", "dept": "Marketing",   "hours": 40, "rate": 220},
    {"name": "Kiran", "dept": "HR",          "hours": 35, "rate": 300},
    {"name": "Meena", "dept": "HR",          "hours": 42, "rate": 270},
]
```

**Expected Output**
```text
=== Engineering ===
Ravi  : ₹9500.00
Sita  : ₹9500.00
Total : ₹19000.00
Highest paid: Ravi
Lowest paid : Ravi

=== Marketing ===
Arjun : ₹9900.00
Divya : ₹8800.00
Total : ₹18700.00
Highest paid: Arjun
Lowest paid : Divya

=== HR ===
Kiran : ₹10500.00
Meena : ₹11610.00
Total : ₹22110.00
Highest paid: Meena
Lowest paid : Kiran
```

For Engineering, Ravi and Sita are tied, so either tied employee is acceptable for both highest and lowest if handled consistently.

### Test Case 2 — One department, all employees work overtime

**Input**
```python
employees = [
    {"name": "Asha",  "dept": "Tech", "hours": 48, "rate": 200},
    {"name": "Vijay", "dept": "Tech", "hours": 44, "rate": 300},
]
```

**Expected Output**
```text
=== Tech ===
Asha  : ₹10400.00
Vijay : ₹13800.00
Total : ₹24200.00
Highest paid: Vijay
Lowest paid : Asha
```

### Test Case 3 — Single department with one employee

**Input**
```python
employees = [
    {"name": "Raj", "dept": "Finance", "hours": 40, "rate": 500},
]
```

**Expected Output**
```text
=== Finance ===
Raj : ₹20000.00
Total : ₹20000.00
Highest paid: Raj
Lowest paid : Raj
```

### Test Case 4 — Departments must be discovered dynamically

**Input**
```python
employees = [
    {"name": "A", "dept": "Sales", "hours": 40, "rate": 200},
    {"name": "B", "dept": "Support", "hours": 45, "rate": 200},
]
```

**Expected Output**
```text
=== Sales ===
A : ₹8000.00
Total : ₹8000.00
Highest paid: A
Lowest paid : A

=== Support ===
B : ₹10750.00
Total : ₹10750.00
Highest paid: B
Lowest paid : B
```

The department names `Sales` and `Support` are not part of a fixed list; they must be taken from the employee data.
