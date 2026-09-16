# Problem 12 — Warehouse Inventory Valuation

## Problem Statement

A warehouse tracks its inventory across multiple products. Each product belongs to a category, and each category has its own clearance discount applied to the stock's value before reporting.

You must calculate, for every product, its raw stock value and its final (discounted) value — then use those per-product values to build category-level and warehouse-level totals.

## Input / Data

```python
products = [
    ("Laptop",     "Electronics", 4, 62000),
    ("Keyboard",   "Electronics", 10, 850),
    ("Chair",      "Furniture",   5, 3500),
    ("Sofa",       "Furniture",   2, 18500),
    ("Rice",       "Grocery",      20, 1100),
    ("T-Shirt",    "Clothing",     10, 900),
    ("Football",   "Sports",        8, 1200),
    ("Notebook",   "Stationery",   50, 75),
    ("Mixer",      "Appliances",    3, 4200),
    ("Wall Clock", "Home Decor",   10, 650),
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

6. **Category reporting** = report every category found in the input separately, including unrecognized categories. Do not combine different category names into one total.

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
- Both functions must be called once per product, inside your loop.
- Do not use pandas or any external library. Plain Python only.

## Test Cases

Every non-empty test case below follows the same complete output structure as the main expected output. Product results, category totals, grand total, highest category, and High Value Stock are all shown.

### Test Case 1 — Normal case with multiple categories

**Input**
```python
products = [
    ("Laptop",     "Electronics", 4, 62000),
    ("Keyboard",   "Electronics", 10, 850),
    ("Chair",      "Furniture",   5, 3500),
    ("Sofa",       "Furniture",   2, 18500),
    ("Rice",       "Grocery",      20, 1100),
    ("T-Shirt",    "Clothing",     10, 900),
    ("Football",   "Sports",        8, 1200),
    ("Notebook",   "Stationery",   50, 75),
    ("Mixer",      "Appliances",    3, 4200),
    ("Wall Clock", "Home Decor",   10, 650),
]
```

**Expected Output**
```text
Laptop     : stock value Rs.248000, final value Rs.235600.00
Keyboard   : stock value Rs.8500,   final value Rs.8075.00
Chair      : stock value Rs.17500,  final value Rs.17500.00
Sofa       : stock value Rs.37000,  final value Rs.37000.00
Rice       : stock value Rs.22000,  final value Rs.19800.00
T-Shirt    : stock value Rs.9000,   final value Rs.9000.00
Football   : stock value Rs.9600,   final value Rs.9600.00
Notebook   : stock value Rs.3750,   final value Rs.3750.00
Mixer      : stock value Rs.12600,  final value Rs.12600.00
Wall Clock : stock value Rs.6500,   final value Rs.6500.00

Category totals : Electronics Rs.243675.00, Furniture Rs.54500.00, Grocery Rs.19800.00, Clothing Rs.9000.00, Sports Rs.9600.00, Stationery Rs.3750.00, Appliances Rs.12600.00, Home Decor Rs.6500.00
Grand total     : Rs.359425.00
Highest category: Electronics
High Value Stock: Laptop, Chair, Sofa, Rice, Mixer
```

### Test Case 2 — Single known category

**Input**
```python
products = [
    ("Keyboard", "Electronics", 15, 800),
    ("Charger",  "Electronics", 30, 300),
]
```

**Expected Output**
```text
Keyboard: stock value Rs.12000, final value Rs.11400.00
Charger : stock value Rs.9000,  final value Rs.8550.00

Category totals : Electronics Rs.19950.00
Grand total     : Rs.19950.00
Highest category: Electronics
High Value Stock: Keyboard
```

### Test Case 3 — Boundary: final value exactly Rs.10,000

**Input**
```python
products = [
    ("Widget", "Stationery", 100, 100),
]
```

**Expected Output**
```text
Widget: stock value Rs.10000, final value Rs.10000.00

Category totals : Stationery Rs.10000.00
Grand total     : Rs.10000.00
Highest category: Stationery
High Value Stock: None
```

The product is not high value because the rule requires a final value **strictly greater than Rs.10,000**.

### Test Case 4 — Tie between category totals

**Input**
```python
products = [
    ("Item A", "Electronics", 2, 900),
    ("Item B", "Grocery",     2, 950),
]
```

**Expected Output**
```text
Item A: stock value Rs.1800, final value Rs.1710.00
Item B: stock value Rs.1900, final value Rs.1710.00

Category totals : Electronics Rs.1710.00, Grocery Rs.1710.00
Grand total     : Rs.3420.00
Highest category: Electronics
High Value Stock: None
```

`Electronics` and `Grocery` are tied, so either category is acceptable as the highest category.

### Test Case 5 — Multiple unrecognized categories

**Input**
```python
products = [
    ("Toy Car",       "Toys",   10,  100),
    ("Chair",         "Home",   5,  2000),
    ("Monitor Stand", "Screen", 8,  12000),
]
```

**Expected Output**
```text
Toy Car       : stock value Rs.1000,  final value Rs.1000.00
Chair         : stock value Rs.10000, final value Rs.10000.00
Monitor Stand : stock value Rs.96000, final value Rs.96000.00

Category totals : Toys Rs.1000.00, Home Rs.10000.00, Screen Rs.96000.00
Grand total     : Rs.107000.00
Highest category: Screen
High Value Stock: Monitor Stand
```

`Toys`, `Home`, and `Screen` are unrecognized categories, so each category is reported separately and receives no discount.

### Test Case 6 — Empty product list

**Input**
```python
products = []
```

**Expected Output**
```text
No products found.
```
