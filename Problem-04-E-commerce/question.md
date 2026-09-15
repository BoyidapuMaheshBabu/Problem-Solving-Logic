# Problem 04 — E-Commerce Order Calculator

## Problem Statement

Calculate the final order amount for an e-commerce purchase by applying every rule strictly in the stated order.

## Rules

### 1. Category discount

Applied to the original order amount:

- Electronics: 5%.
- Clothing: 15%.
- Books: 10%.
- Groceries: no discount.

### 2. Bonus discount

Applied after the category discount:

- Below ₹1,000: 0%.
- ₹1,000–₹4,999: 5%.
- ₹5,000–₹9,999: 10%.
- ₹10,000 and above: 15%.

### 3. Shipping cost

Applied after both discounts:

- Below ₹500: ₹100.
- ₹500–₹1,999: ₹50.
- ₹2,000 and above: Free.

### 4. Coupon SAVE10

- Valid only when the amount after both discounts is strictly greater than ₹1,000.
- If valid, deduct ₹100.

## Input

Enter category, order amount, and coupon code.

## Example

**Input**
```text
category = Electronics
amount = 8000
coupon = SAVE10
```

**Expected Output**
```text
Category discount: 5% = ₹400.00
After category discount: ₹7600.00
Bonus discount: 10% = ₹760.00
After bonus discount: ₹6840.00
Shipping cost: Free
Coupon: SAVE10 valid = −₹100.00
Final amount: ₹6740.00
```

## Constraints

- Category must be Electronics, Clothing, Books, or Groceries.
- Order amount must be greater than 0.
- Apply discounts in the given order.
- The coupon eligibility check uses the amount after both discounts.

## Test Cases

Every test case below uses the same complete output structure as the example.

### Test Case 1 — Electronics, valid coupon, large order

**Input**
```text
category = Electronics
amount = 8000
coupon = SAVE10
```

**Expected Output**
```text
Category discount: 5% = ₹400.00
After category discount: ₹7600.00
Bonus discount: 10% = ₹760.00
After bonus discount: ₹6840.00
Shipping cost: Free
Coupon: SAVE10 valid = −₹100.00
Final amount: ₹6740.00
```

### Test Case 2 — Groceries, small order, no coupon

**Input**
```text
category = Groceries
amount = 400
coupon = NONE
```

**Expected Output**
```text
Category discount: 0% = ₹0.00
After category discount: ₹400.00
Bonus discount: 0% = ₹0.00
After bonus discount: ₹400.00
Shipping cost: ₹100.00
Coupon: NONE = ₹0.00
Final amount: ₹500.00
```

### Test Case 3 — Clothing, highest bonus tier, no coupon

**Input**
```text
category = Clothing
amount = 12000
coupon = NONE
```

**Expected Output**
```text
Category discount: 15% = ₹1800.00
After category discount: ₹10200.00
Bonus discount: 15% = ₹1530.00
After bonus discount: ₹8670.00
Shipping cost: Free
Coupon: NONE = ₹0.00
Final amount: ₹8670.00
```

### Test Case 4 — Boundary: amount after category discount is just above ₹1,000

**Input**
```text
category = Books
amount = 1112
coupon = SAVE10
```

**Expected Output**
```text
Category discount: 10% = ₹111.20
After category discount: ₹1000.80
Bonus discount: 5% = ₹50.04
After bonus discount: ₹950.76
Shipping cost: ₹50.00
Coupon: SAVE10 invalid = ₹0.00
Final amount: ₹1000.76
```

The coupon is invalid because the amount after both discounts is not strictly greater than ₹1,000.

### Test Case 5 — Invalid category

**Input**
```text
category = Furniture
amount = 5000
coupon = NONE
```

**Expected Output**
```text
Invalid category!
```
