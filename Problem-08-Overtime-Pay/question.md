# Problem 08 — Overtime Pay Calculator

## Problem Statement

Calculate an employee's total pay including regular pay, overtime pay, and a night-shift bonus.

## Rules

### Regular pay

- First 8 hours are regular hours.
- Regular pay = regular hours × hourly rate.

### Overtime pay

- Hours beyond 8 are overtime.
- Overtime is capped at 4 hours maximum.
- Weekday overtime rate: 1.5× hourly rate.
- Saturday overtime rate: 2.0× hourly rate.
- Sunday overtime rate: 2.5× hourly rate.

### Night-shift bonus

- Applies only when the employee is on a night shift **and** has overtime hours.
- Bonus = overtime hours × ₹50.

## Input

Enter hourly rate, hours worked, day (Weekday/Saturday/Sunday), and night shift (Yes/No).

## Example

**Input**
```text
rate = 200
hours = 11
day = Saturday
night = Yes
```

**Expected Output**
```text
Regular hours: 8
Regular pay: 8 × ₹200 = ₹1600.00
Overtime hours: 3
Overtime rate: 2.0× = ₹400.00/hr
Overtime pay: 3 × ₹400 = ₹1200.00
Night bonus: 3 × ₹50 = ₹150.00
Total payment: ₹2950.00
```

## Constraints

- Overtime is capped at 4 hours even when more hours are worked.
- Night bonus applies only when overtime hours exist.
- Day must be Weekday, Saturday, or Sunday.

## Test Cases

Every test case below uses the same complete output structure as the example.

### Test Case 1 — Weekday overtime with night shift

**Input**
```text
rate = 200
hours = 11
day = Weekday
night = Yes
```

**Expected Output**
```text
Regular hours: 8
Regular pay: 8 × ₹200 = ₹1600.00
Overtime hours: 3
Overtime rate: 1.5× = ₹300.00/hr
Overtime pay: 3 × ₹300 = ₹900.00
Night bonus: 3 × ₹50 = ₹150.00
Total payment: ₹2650.00
```

### Test Case 2 — Sunday overtime beyond the 4-hour cap

**Input**
```text
rate = 300
hours = 15
day = Sunday
night = No
```

**Expected Output**
```text
Regular hours: 8
Regular pay: 8 × ₹300 = ₹2400.00
Overtime hours: 4 (capped from 7)
Overtime rate: 2.5× = ₹750.00/hr
Overtime pay: 4 × ₹750 = ₹3000.00
Night bonus: ₹0.00
Total payment: ₹5400.00
```

### Test Case 3 — Exactly 8 hours, no overtime

**Input**
```text
rate = 200
hours = 8
day = Weekday
night = Yes
```

**Expected Output**
```text
Regular hours: 8
Regular pay: 8 × ₹200 = ₹1600.00
Overtime hours: 0
Overtime rate: ₹0.00/hr
Overtime pay: ₹0.00
Night bonus: ₹0.00
Total payment: ₹1600.00
```

### Test Case 4 — Saturday overtime

**Input**
```text
rate = 150
hours = 10
day = Saturday
night = No
```

**Expected Output**
```text
Regular hours: 8
Regular pay: 8 × ₹150 = ₹1200.00
Overtime hours: 2
Overtime rate: 2.0× = ₹300.00/hr
Overtime pay: 2 × ₹300 = ₹600.00
Night bonus: ₹0.00
Total payment: ₹1800.00
```

### Test Case 5 — Night shift without overtime

**Input**
```text
rate = 200
hours = 6
day = Weekday
night = Yes
```

**Expected Output**
```text
Regular hours: 6
Regular pay: 6 × ₹200 = ₹1200.00
Overtime hours: 0
Overtime rate: ₹0.00/hr
Overtime pay: ₹0.00
Night bonus: ₹0.00
Total payment: ₹1200.00
```
