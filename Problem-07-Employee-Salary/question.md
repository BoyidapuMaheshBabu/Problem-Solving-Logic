# Problem 07 — Employee Salary Calculator

## Problem Statement

Calculate an employee's final salary based on experience, performance, attendance, and tax.

## Rules

### Base salary by experience

- 0–2 years: ₹25,000.
- 3–5 years: ₹40,000.
- 6–10 years: ₹60,000.
- 11+ years: ₹90,000.

### Performance bonus

Applied to the base salary:

- Poor: 0%.
- Average: 5%.
- Good: 10%.
- Excellent: 20%.

### Attendance penalty

Applied after the performance bonus:

- Below 70%: 20% penalty.
- 70–84%: 10% penalty.
- 85–94%: 5% penalty.
- 95–100%: no penalty.

### Tax

Applied after the attendance penalty:

- Up to ₹30,000: 0% tax.
- ₹30,001–₹60,000: 10% tax.
- ₹60,001–₹1,00,000: 20% tax.
- Above ₹1,00,000: 30% tax.

## Input

Enter years of experience, performance rating, and attendance percentage.

## Example

**Input**
```text
years = 8
rating = Excellent
attendance = 92
```

**Expected Output**
```text
Base salary: ₹60000.00
Bonus: 20% = ₹12000.00
After bonus: ₹72000.00
Attendance penalty: 5% = ₹3600.00
After penalty: ₹68400.00
Tax: 20% = ₹13680.00
Final salary: ₹54720.00
```

## Constraints

- Years of experience must be 0 or more.
- Attendance must be between 0 and 100.
- Rating must be Poor, Average, Good, or Excellent.
- Apply all rules strictly in the given order.

## Test Cases

Every valid test case below uses the same complete output structure as the example.

### Test Case 1 — Mid-level employee, excellent rating, 5% attendance penalty

**Input**
```text
years = 8
rating = Excellent
attendance = 92
```

**Expected Output**
```text
Base salary: ₹60000.00
Bonus: 20% = ₹12000.00
After bonus: ₹72000.00
Attendance penalty: 5% = ₹3600.00
After penalty: ₹68400.00
Tax: 20% = ₹13680.00
Final salary: ₹54720.00
```

### Test Case 2 — Junior employee, poor rating, low attendance

**Input**
```text
years = 1
rating = Poor
attendance = 65
```

**Expected Output**
```text
Base salary: ₹25000.00
Bonus: 0% = ₹0.00
After bonus: ₹25000.00
Attendance penalty: 20% = ₹5000.00
After penalty: ₹20000.00
Tax: 0% = ₹0.00
Final salary: ₹20000.00
```

### Test Case 3 — Senior employee, excellent rating, no attendance penalty

**Input**
```text
years = 15
rating = Excellent
attendance = 100
```

**Expected Output**
```text
Base salary: ₹90000.00
Bonus: 20% = ₹18000.00
After bonus: ₹108000.00
Attendance penalty: 0% = ₹0.00
After penalty: ₹108000.00
Tax: 30% = ₹32400.00
Final salary: ₹75600.00
```

### Test Case 4 — Boundary: exactly 2 years of experience

**Input**
```text
years = 2
rating = Average
attendance = 80
```

**Expected Output**
```text
Base salary: ₹25000.00
Bonus: 5% = ₹1250.00
After bonus: ₹26250.00
Attendance penalty: 10% = ₹2625.00
After penalty: ₹23625.00
Tax: 0% = ₹0.00
Final salary: ₹23625.00
```

### Test Case 5 — Invalid performance rating

**Input**
```text
years = 5
rating = Outstanding
attendance = 90
```

**Expected Output**
```text
Invalid rating!
```

### Test Case 6 — Invalid attendance percentage

**Input**
```text
years = 5
rating = Good
attendance = 110
```

**Expected Output**
```text
Invalid employee attendance percentage!
```
