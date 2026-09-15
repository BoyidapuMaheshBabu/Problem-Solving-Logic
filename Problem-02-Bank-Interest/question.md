# Problem 02 — Bank Interest Calculator

## Problem Statement

Calculate the interest earned from a bank account balance.

## Interest Rules

- Balance ≤ 0: no interest; the balance is invalid.
- Balance ≤ ₹10,000: 2% interest.
- Balance ≤ ₹50,000: 4% interest.
- Balance ≤ ₹1,00,000: 6% interest + ₹500 bonus.
- Balance > ₹1,00,000: 8% interest + ₹500 bonus, then 5% tax on the interest plus bonus.

## Input

Enter the account balance.

## Example

**Input**
```text
balance = 75000
```

**Expected Output**
```text
Interest earned is ₹5000.00
```

**Calculation:** ₹75,000 × 6% = ₹4,500; plus ₹500 bonus = ₹5,000.

## Constraints

- Balance must be a positive number for a valid calculation.
- Tax applies only to the highest balance tier and is calculated on interest plus bonus.
- Round the final monetary result to 2 decimal places.

## Test Cases

Each test case below shows the complete expected result for that balance.

### Test Case 1 — Balance in the 2% tier

**Input**
```text
balance = 5000
```

**Expected Output**
```text
Interest earned is ₹100.00
```

### Test Case 2 — Balance in the 4% tier

**Input**
```text
balance = 30000
```

**Expected Output**
```text
Interest earned is ₹1200.00
```

### Test Case 3 — Balance in the 6% tier with bonus

**Input**
```text
balance = 75000
```

**Expected Output**
```text
Interest earned is ₹5000.00
```

### Test Case 4 — Highest tier with bonus and tax

**Input**
```text
balance = 200000
```

**Expected Output**
```text
Interest earned is ₹15675.00
```

Calculation: ₹200,000 × 8% = ₹16,000; + ₹500 bonus = ₹16,500; 5% tax = ₹825; final interest earned = ₹15,675.

### Test Case 5 — Boundary: exactly ₹10,000

**Input**
```text
balance = 10000
```

**Expected Output**
```text
Interest earned is ₹200.00
```

### Test Case 6 — Invalid zero balance

**Input**
```text
balance = 0
```

**Expected Output**
```text
No interest earned, because the balance is invalid.
```
