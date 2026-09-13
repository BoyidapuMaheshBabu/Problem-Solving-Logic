# Problem 12 — Warehouse Inventory Valuation

## Curriculum Mapping

- **Main Topic:** Introduction to Programming → Loops and Functions
- **Sub-topic:** Functions
- **Supporting Concepts:** Loops, dictionaries, conditionals, aggregation, sorting (all already practiced in Problems 9–11)
- **Learning Goal:** Structure a program around two purpose-built functions that are called repeatedly, so function use survives into the refactor instead of disappearing.
- **Why Now:** In both Problem 10 and Problem 11, a function appeared in the initial solution and was removed during refactoring. Loops, dictionaries, and aggregation are already solid. Functions are the one skill that hasn't stuck yet. This problem is designed so that avoiding functions means writing the same two calculations seven separate times by hand.

## Problem Statement

A warehouse tracks its inventory across multiple products. Each product belongs to a category, and each category has its own clearance discount applied to the stock's value before reporting.

You must calculate, for every product, its raw stock value and its final (discounted) value — then use those per-product values to build category-level and warehouse-level totals.

## Input / Data

```python
products = [
    ("Laptop",    "Electronics", 5,   55000),
    ("Mouse",     "Electronics", 20,  500),
    ("Rice Bag",  "Grocery",     50,  1200),
    ("Sugar Bag", "Grocery",     40,  450),
    ("Notebook",  "Stationery",  100, 60),
    ("Pen Pack",  "Stationery",  200, 20),
    ("Monitor",   "Electronics", 8,  12000),
]
```

Each tuple is:

```text
(product_name, category, quantity, unit_price)
```

## Rules

1. **Stock value for a product** = `quantity × unit_price`.

2. **Category discount**, applied to a product's stock value to get its final value:
   - Electronics: 5% discount
   - Grocery: 10% discount
   - Stationery: no discount
   - Any other / unrecognized category: no discount (treat it the same as Stationery)

3. **Category total** = sum of the **FINAL values** of every product in that category.

4. **Grand total** = sum of all category totals.

5. **High Value Stock** = any product whose **FINAL value is strictly greater than Rs.10,000**.

## Required Output

1. Every product's stock value and final value.
2. Total final value per category.
3. Grand total inventory value.
4. The category with the highest total value.
5. The list of High Value Stock products (final value > Rs.10,000).

## Constraints

- If the product list is empty, print `No products found.` and stop — do not calculate totals.
- Round final values to 2 decimal places wherever a discount produces a decimal result.
- If two categories tie for the highest total, either one may be reported.

## Important Notes

- You must write **at least two functions**:
  1. One that calculates a product's stock value.
  2. One that applies the category discount.
- Both functions must be called once per product, inside your loop — not written once and then abandoned in the refactor.
- Do not use pandas or any external library. Plain Python only.

## Test Cases

### Test Case 1 — Normal Case (given data, mixed categories)

Use the products list above.

**Expected:**

```text
Laptop   : stock value Rs.275000, final value Rs.261250.00
Mouse    : stock value Rs.10000,  final value Rs.9500.00
Rice Bag : stock value Rs.60000,  final value Rs.54000.00
Sugar Bag: stock value Rs.18000,  final value Rs.16200.00
Notebook : stock value Rs.6000,   final value Rs.6000
Pen Pack : stock value Rs.4000,   final value Rs.4000
Monitor  : stock value Rs.96000,  final value Rs.91200.00

Category totals : Electronics Rs.361950.00, Grocery Rs.70200.00, Stationery Rs.10000
Grand total     : Rs.442150.00
Highest category: Electronics
High Value Stock: Laptop, Rice Bag, Sugar Bag, Monitor
```

### Test Case 2 — Single Category Only

```python
products = [
    ("Keyboard", "Electronics", 15, 800),
    ("Charger",  "Electronics", 30, 300),
]
```

**Expected:**

```text
Keyboard: stock value Rs.12000, final value Rs.11400.00
Charger : stock value Rs.9000,  final value Rs.8550.00
Electronics total: Rs.19950.00
Grand total      : Rs.19950.00
High Value Stock : Keyboard only
```

`Rs.11400.00 > Rs.10000`; Charger's `Rs.8550.00` does not qualify.

### Test Case 3 — Boundary: Final Value Exactly Rs.10,000

```python
products = [
    ("Widget", "Stationery", 100, 100),
]
```

**Expected:**

```text
Stock value: Rs.10000, final value: Rs.10000
High Value Stock: None
```

The rule requires **strictly greater than Rs.10,000**, not equal.

### Test Case 4 — Tie Between Two Categories

```python
products = [
    ("Item A", "Electronics", 2, 900),
    ("Item B", "Grocery",     2, 950),
]
```

**Expected:**

```text
Item A: stock value Rs.1800, final value Rs.1710.00
Item B: stock value Rs.1900, final value Rs.1710.00
Electronics total: Rs.1710.00
Grocery total    : Rs.1710.00  (TIE)
Highest category : either Electronics or Grocery is acceptable
```

### Test Case 5 — Unrecognized Category

```python
products = [
    ("Mystery Item", "Toys", 10, 100),
]
```

**Expected:**

```text
Stock value: Rs.1000, final value: Rs.1000
Toys total: Rs.1000.00
```

The unrecognized category `Toys` gets no discount, the same as Stationery.

### Test Case 6 — Empty Product List

```python
products = []
```

**Expected:**

```text
No products found.
```
