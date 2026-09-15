# Problem 09 — Team Payroll Summary

## Problem Statement

Process the payroll for a team of employees and generate a summary report.

## Salary Rules

- Up to 40 hours: paid at the normal hourly rate.
- Hours beyond 40: paid at 1.5× the normal hourly rate.

## Report Requirements

Calculate and report:

- Individual salary for each employee.
- Total team payroll.
- Average pay across the team.
- Name of the highest-paid employee.
- Number of employees who worked overtime.

## Input/Data

```python
employees = [
    {"name": "Ravi",  "hours": 45, "rate": 200},
    {"name": "Sita",  "hours": 38, "rate": 250},
    {"name": "Arjun", "hours": 50, "rate": 180},
    {"name": "Divya", "hours": 40, "rate": 220},
]
```

## Expected Output

```text
Ravi  : ₹9500.00
Sita  : ₹9500.00
Arjun : ₹9900.00
Divya : ₹8800.00
Total payroll           : ₹37700.00
Average pay             : ₹9425.00
Highest paid            : Arjun
Employees with overtime : 2
```

## Constraints

- Overtime rate is exactly 1.5× the normal hourly rate.
- Only hours beyond 40 count as overtime.
- Handle an empty employee list safely.

## Test Cases

Every test case below uses the same complete output structure as the main expected output.

### Test Case 1 — Mixed regular and overtime employees

**Input**
```python
employees = [
    {"name": "Ravi",  "hours": 45, "rate": 200},
    {"name": "Sita",  "hours": 38, "rate": 250},
    {"name": "Arjun", "hours": 50, "rate": 180},
    {"name": "Divya", "hours": 40, "rate": 220},
]
```

**Expected Output**
```text
Ravi  : ₹9500.00
Sita  : ₹9500.00
Arjun : ₹9900.00
Divya : ₹8800.00
Total payroll           : ₹37700.00
Average pay             : ₹9425.00
Highest paid            : Arjun
Employees with overtime : 2
```

### Test Case 2 — Everyone works exactly 40 hours

**Input**
```python
employees = [
    {"name": "Kiran", "hours": 40, "rate": 300},
    {"name": "Meena", "hours": 40, "rate": 250},
]
```

**Expected Output**
```text
Kiran : ₹12000.00
Meena : ₹10000.00
Total payroll           : ₹22000.00
Average pay             : ₹11000.00
Highest paid            : Kiran
Employees with overtime : 0
```

### Test Case 3 — Everyone works overtime

**Input**
```python
employees = [
    {"name": "Asha",  "hours": 48, "rate": 200},
    {"name": "Vijay", "hours": 44, "rate": 300},
]
```

**Expected Output**
```text
Asha  : ₹10400.00
Vijay : ₹13800.00
Total payroll           : ₹24200.00
Average pay             : ₹12100.00
Highest paid            : Vijay
Employees with overtime : 2
```

### Test Case 4 — Single employee at the 40-hour boundary

**Input**
```python
employees = [
    {"name": "Raj", "hours": 40, "rate": 500},
]
```

**Expected Output**
```text
Raj : ₹20000.00
Total payroll           : ₹20000.00
Average pay             : ₹20000.00
Highest paid            : Raj
Employees with overtime : 0
```

### Test Case 5 — Empty employee list

**Input**
```python
employees = []
```

**Expected Output**
```text
No employees found.
```
