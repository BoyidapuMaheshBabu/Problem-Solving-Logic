# Problem 05 — Library Fine Calculator

## Problem Statement

Calculate the library fine for a book returned late.

## Fine Rules

The fine tiers are cumulative:

- Days 1–7: ₹5 per day.
- Days 8–14: ₹10 per day for days beyond 7.
- Days 15–30: ₹20 per day for days beyond 14.
- Days 31+: ₹50 per day for days beyond 30.

## Book Type Multiplier

- Fiction: 1×.
- Non-fiction: 1.5×.
- Reference: 2×.

## Membership Discount

Applied after the book-type multiplier:

- Non-member: 0%.
- Regular: 10%.
- Premium: 20%.

## Maximum Fine

The final fine is capped at ₹500.

## Input

Enter days overdue, book type, and membership status.

## Example

**Input**
```text
days = 20
book = Reference
membership = Regular
```

**Expected Output**
```text
Base fine: ₹225.00
Multiplier: Reference (2×) = ₹450.00
Membership discount: 10% = −₹45.00
After discount: ₹405.00
Final fine: ₹405.00
```

**Calculation:** 7 × ₹5 + 7 × ₹10 + 6 × ₹20 = ₹225; Reference multiplier gives ₹450; 10% membership discount gives a final fine of ₹405.

## Constraints

- Days overdue must be 0 or greater.
- Fine tiers are cumulative.
- Apply the book-type multiplier before the membership discount.
- Cap the final fine at ₹500.

## Test Cases

Every test case below uses the same complete output structure.

### Test Case 1 — Tier 1, Fiction, non-member

**Input**
```text
days = 5
book = Fiction
membership = Non-member
```

**Expected Output**
```text
Base fine: ₹25.00
Multiplier: Fiction (1×) = ₹25.00
Membership discount: 0% = ₹0.00
After discount: ₹25.00
Final fine: ₹25.00
```

### Test Case 2 — Cumulative tiers, Non-fiction, Regular member

**Input**
```text
days = 10
book = Non-fiction
membership = Regular
```

**Expected Output**
```text
Base fine: ₹65.00
Multiplier: Non-fiction (1.5×) = ₹97.50
Membership discount: 10% = −₹9.75
After discount: ₹87.75
Final fine: ₹87.75
```

### Test Case 3 — Tier 4 with Reference multiplier and Premium discount

**Input**
```text
days = 35
book = Reference
membership = Premium
```

**Expected Output**
```text
Base fine: ₹675.00
Multiplier: Reference (2×) = ₹1350.00
Membership discount: 20% = −₹270.00
After discount: ₹1080.00
Final fine: ₹500.00
```

The fine is capped at ₹500 after all other calculations.

### Test Case 4 — Boundary: exactly 0 days overdue

**Input**
```text
days = 0
book = Fiction
membership = Non-member
```

**Expected Output**
```text
Base fine: ₹0.00
Multiplier: Fiction (1×) = ₹0.00
Membership discount: 0% = ₹0.00
After discount: ₹0.00
Final fine: ₹0.00
```

### Test Case 5 — Boundary: first day of the 31+ tier

**Input**
```text
days = 31
book = Fiction
membership = Non-member
```

**Expected Output**
```text
Base fine: ₹475.00
Multiplier: Fiction (1×) = ₹475.00
Membership discount: 0% = ₹0.00
After discount: ₹475.00
Final fine: ₹475.00
```

### Test Case 6 — Invalid book type

**Input**
```text
days = 5
book = Magazine
membership = Regular
```

**Expected Output**
```text
Invalid book type!
```
