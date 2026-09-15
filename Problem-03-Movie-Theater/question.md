# Problem 03 — Movie Theater Ticket Pricing

## Problem Statement

Calculate the final price for a movie theater booking. The price is calculated per ticket and then multiplied by the number of tickets.

## Rules

### Age-based base price

- Child (1–12): ₹150.
- Teen (13–17): ₹200.
- Adult (18–60): ₹300.
- Senior (61+): ₹200.

### Show-time adjustment

Applied to the base price:

- Matinee (10:00–16:59): −₹50.
- Evening (17:00–20:59): +₹100.
- Night (21:00–23:59): +₹150.
- Times outside these ranges receive no time adjustment.

### Group discount

Applied to the price after the time adjustment:

- Fewer than 5 tickets: 0%.
- 5–9 tickets: 10%.
- 10–19 tickets: 15%.
- 20 or more tickets: 20%.

### Membership discount

Applied after the group discount:

- Member: 5%.
- Non-member: 0%.

## Input

Enter age, number of tickets, show time in 24-hour format, and membership status (Yes/No).

## Example

**Input**
```text
age = 25
tickets = 10
show_time = 19
membership = Yes
```

**Expected Output**
```text
Base price: ₹300
Time adjustment: +₹100
Price after time adjustment: ₹400
Group discount: 15% = ₹60.00
Price after group discount: ₹340.00
Membership discount: 5% = ₹17.00
Final price per ticket: ₹323.00
Total for 10 tickets: ₹3230.00
```

## Constraints

- Apply discounts in this order: group discount first, then membership discount.
- Show time is given in 24-hour format.
- The age, ticket count, and membership values should be valid for the rules above.

## Test Cases

Every test case below uses the same complete output structure as the example.

### Test Case 1 — Adult, evening, member, fewer than 5 tickets

**Input**
```text
age = 25
tickets = 3
show_time = 18
membership = Yes
```

**Expected Output**
```text
Base price: ₹300
Time adjustment: +₹100
Price after time adjustment: ₹400
Group discount: 0% = ₹0.00
Price after group discount: ₹400.00
Membership discount: 5% = ₹20.00
Final price per ticket: ₹380.00
Total for 3 tickets: ₹1140.00
```

### Test Case 2 — Child, matinee, 5–9 tickets, non-member

**Input**
```text
age = 10
tickets = 8
show_time = 14
membership = No
```

**Expected Output**
```text
Base price: ₹150
Time adjustment: −₹50
Price after time adjustment: ₹100
Group discount: 10% = ₹10.00
Price after group discount: ₹90.00
Membership discount: 0% = ₹0.00
Final price per ticket: ₹90.00
Total for 8 tickets: ₹720.00
```

### Test Case 3 — Senior, night show, 20+ tickets, member

**Input**
```text
age = 65
tickets = 20
show_time = 22
membership = Yes
```

**Expected Output**
```text
Base price: ₹200
Time adjustment: +₹150
Price after time adjustment: ₹350
Group discount: 20% = ₹70.00
Price after group discount: ₹280.00
Membership discount: 5% = ₹14.00
Final price per ticket: ₹266.00
Total for 20 tickets: ₹5320.00
```

### Test Case 4 — Boundary: exactly 5 tickets

**Input**
```text
age = 30
tickets = 5
show_time = 19
membership = No
```

**Expected Output**
```text
Base price: ₹300
Time adjustment: +₹100
Price after time adjustment: ₹400
Group discount: 10% = ₹40.00
Price after group discount: ₹360.00
Membership discount: 0% = ₹0.00
Final price per ticket: ₹360.00
Total for 5 tickets: ₹1800.00
```

### Test Case 5 — Show time outside all adjustment ranges

**Input**
```text
age = 15
tickets = 2
show_time = 9
membership = No
```

**Expected Output**
```text
Base price: ₹200
Time adjustment: ₹0
Price after time adjustment: ₹200
Group discount: 0% = ₹0.00
Price after group discount: ₹200.00
Membership discount: 0% = ₹0.00
Final price per ticket: ₹200.00
Total for 2 tickets: ₹400.00
```
