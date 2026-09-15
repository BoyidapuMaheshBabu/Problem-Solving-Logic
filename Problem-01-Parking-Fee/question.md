# Problem 01 — Parking Fee Calculator

## Problem Statement

Build a parking fee calculator based on the number of hours a vehicle is parked.

## Rules

- First 2 hours: fixed ₹30.
- Hours 3–5: ₹20 per additional hour.
- After 5 hours: ₹10 per additional hour.
- If the calculated fee is strictly above ₹200, apply a 10% discount.

## Input

Enter the number of hours parked.

## Example

**Input**
```text
h = 7
```

**Expected Output**
```text
Fee is ₹110.00
```

**Calculation:** ₹30 + (3 × ₹20) + (2 × ₹10) = ₹110. No discount applies.

## Constraints

- Hours must be a positive integer.
- Apply the 10% discount only when the calculated fee is strictly greater than ₹200.

## Test Cases

Each test case below shows the complete expected output for that input.

### Test Case 1 — First 2 hours

**Input**
```text
h = 1
```

**Expected Output**
```text
Fee is ₹30.00
```

### Test Case 2 — End of the ₹20-per-hour tier

**Input**
```text
h = 5
```

**Expected Output**
```text
Fee is ₹90.00
```

Calculation: ₹30 + (3 × ₹20) = ₹90.

### Test Case 3 — Discount boundary: calculated fee is exactly ₹200

**Input**
```text
h = 16
```

**Expected Output**
```text
Fee is ₹200.00
```

No discount applies because the rule requires the calculated fee to be strictly greater than ₹200.

### Test Case 4 — Discount applies after 5 hours

**Input**
```text
h = 17
```

**Expected Output**
```text
Fee is ₹189.00
```

Calculation: ₹30 + (3 × ₹20) + (12 × ₹10) = ₹210; 10% discount = ₹21; final fee = ₹189.
