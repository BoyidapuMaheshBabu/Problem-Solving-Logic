# Problem 13 — Order Payment Reconciliation

## Problem Statement

An online store maintains two separate records: customer orders and the payments received for those orders.

Customers may pay an order in multiple transactions. Some orders may be partially paid, unpaid, or overpaid. Payment records may also refer to order IDs that do not exist.

Build a Python program that reconciles the order and payment records and generates a complete financial report.

## Input / Data

Two lists are provided.

**Orders** — each tuple contains:

```python
(order_id, customer_name, order_total)
```

**Payments** — each tuple contains:

```python
(order_id, payment_amount)
```

Example structure:

```python
orders = [
    ("ORD-101", "Aditi", 2500),
    ("ORD-102", "Ravi", 1800),
]

payments = [
    ("ORD-101", 1000),
    ("ORD-101", 1500),
    ("ORD-102", 1000),
]
```

## Rules

1. An order can have multiple payment records. The total amount paid for an order is the sum of all its matching payment records.
2. Determine each order's payment status:
   - **Paid:** total paid equals the order total.
   - **Partially Paid:** total paid is greater than zero but less than the order total.
   - **Unpaid:** total paid is zero.
   - **Overpaid:** total paid exceeds the order total.
3. **Balance due** is the remaining amount owed. It must never be negative.
4. **Overpayment** is the amount paid beyond the order total. It must be zero when the order is not overpaid.
5. A payment whose order ID does not exist in the orders list is an **unmatched payment**. Do not include it in any order's payment total.
6. Report unmatched payment records individually, even when multiple unmatched records have the same order ID.

## Required Output

1. A reconciliation report for every order, showing its ID, customer, order total, total paid, balance due, overpayment, and payment status.
2. The total value of all orders.
3. The total payments matched to valid orders.
4. The total outstanding balance across all orders.
5. The total overpayment across all orders.
6. Every unmatched payment record and the total value of unmatched payments.

## Constraints

- Order IDs in the orders list are unique.
- An order can have any number of payment records, including none.
- Order totals must be positive integers. Payment amounts must be non-negative integers.
- Order IDs must match exactly.
- Display orders in their original input order.
- Display unmatched payment records in their original input order.
- If no orders are provided, print `No orders to reconcile.` Still report any unmatched payments and provide the financial summary with zero values where appropriate.
- If no unmatched payment records exist, display `None` in the unmatched-payments section.
- Use plain Python; do not use external libraries.

## Test Cases

### Test Case 1 — Multiple payment statuses and an unmatched payment

**Input**

```python
orders = [
    ("ORD-101", "Aditi", 2500),
    ("ORD-102", "Ravi", 1800),
    ("ORD-103", "Priya", 3200),
    ("ORD-104", "Kumar", 950),
    ("ORD-105", "Meena", 1200),
]

payments = [
    ("ORD-101", 1000),
    ("ORD-101", 1500),
    ("ORD-102", 1000),
    ("ORD-104", 950),
    ("ORD-105", 1500),
    ("ORD-999", 250),
]
```

**Expected Output**

```text
--- Order Reconciliation ---
ORD-101 | Aditi | Order: Rs.2500 | Paid: Rs.2500 | Due: Rs.0 | Overpayment: Rs.0 | Status: Paid
ORD-102 | Ravi | Order: Rs.1800 | Paid: Rs.1000 | Due: Rs.800 | Overpayment: Rs.0 | Status: Partially Paid
ORD-103 | Priya | Order: Rs.3200 | Paid: Rs.0 | Due: Rs.3200 | Overpayment: Rs.0 | Status: Unpaid
ORD-104 | Kumar | Order: Rs.950 | Paid: Rs.950 | Due: Rs.0 | Overpayment: Rs.0 | Status: Paid
ORD-105 | Meena | Order: Rs.1200 | Paid: Rs.1500 | Due: Rs.0 | Overpayment: Rs.300 | Status: Overpaid

--- Summary ---
Total order value: Rs.9650
Payments matched to orders: Rs.5950
Total outstanding balance: Rs.4000
Total overpayment: Rs.300

--- Unmatched Payments ---
ORD-999: Rs.250
Unmatched payment total: Rs.250
```

### Test Case 2 — No unmatched payments

**Input**

```python
orders = [
    ("ORD-201", "Dev", 1000),
    ("ORD-202", "Sara", 600),
]

payments = [
    ("ORD-201", 600),
    ("ORD-201", 400),
]
```

**Expected Output**

```text
--- Order Reconciliation ---
ORD-201 | Dev | Order: Rs.1000 | Paid: Rs.1000 | Due: Rs.0 | Overpayment: Rs.0 | Status: Paid
ORD-202 | Sara | Order: Rs.600 | Paid: Rs.0 | Due: Rs.600 | Overpayment: Rs.0 | Status: Unpaid

--- Summary ---
Total order value: Rs.1600
Payments matched to orders: Rs.1000
Total outstanding balance: Rs.600
Total overpayment: Rs.0

--- Unmatched Payments ---
None
Unmatched payment total: Rs.0
```

### Test Case 3 — Empty orders with unmatched payments

**Input**

```python
orders = []

payments = [
    ("ORD-404", 700),
]
```

**Expected Output**

```text
--- Order Reconciliation ---
No orders to reconcile.

--- Summary ---
Total order value: Rs.0
Payments matched to orders: Rs.0
Total outstanding balance: Rs.0
Total overpayment: Rs.0

--- Unmatched Payments ---
ORD-404: Rs.700
Unmatched payment total: Rs.700
```

### Test Case 4 — Repeated unmatched IDs and a zero-value payment

**Input**

```python
orders = [
    ("ORD-301", "Nila", 500),
]

payments = [
    ("ORD-900", 100),
    ("ORD-900", 250),
    ("ORD-301", 0),
]
```

**Expected Output**

```text
--- Order Reconciliation ---
ORD-301 | Nila | Order: Rs.500 | Paid: Rs.0 | Due: Rs.500 | Overpayment: Rs.0 | Status: Unpaid

--- Summary ---
Total order value: Rs.500
Payments matched to orders: Rs.0
Total outstanding balance: Rs.500
Total overpayment: Rs.0

--- Unmatched Payments ---
ORD-900: Rs.100
ORD-900: Rs.250
Unmatched payment total: Rs.350
```
