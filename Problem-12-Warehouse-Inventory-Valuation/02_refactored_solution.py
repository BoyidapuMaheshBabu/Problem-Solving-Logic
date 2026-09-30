"""
Warehouse Inventory Valuation

This program calculates the raw stock value and discounted final value
for each product, then generates category-level and warehouse-level
inventory totals.

Report Includes:
- Every product's stock value and final value
- Total final value per category
- Grand total inventory value
- Category with the highest total value
- High Value Stock products
"""

# ===============================================
# Step 1: Product Data
# ===============================================

products = [
    ("Laptop",     "Electronics", 4, 62000),
    ("Keyboard",   "Electronics", 10, 850),
    ("Chair",      "Furniture",   5, 3500),
    ("Sofa",       "Furniture",   2, 18500),
    ("Rice",       "Grocery",     20, 1100),
    ("T-Shirt",    "Clothing",   10, 900),
    ("Football",   "Sports",       8, 1200),
    ("Notebook",   "Stationery",  50, 75),
    ("Mixer",      "Appliances",   3, 4200),
    ("Wall Clock", "Home Decor",  10, 650),
]


# ===============================================
# Step 2: Program Constants
# ===============================================

PRODUCT_KEYS = ("product_name", "category", "quantity", "unit_price")

CATEGORY_DISCOUNTS = {
    "Electronics": 0.05,
    "Grocery": 0.10,
    "Stationery": 0.00,
}

HIGH_VALUE_THRESHOLD = 10_000


# ===============================================
# Step 3: Convert Product Tuples into Dictionaries
# ===============================================

product_list = []

for product in products:
    product_list.append(dict(zip(PRODUCT_KEYS, product)))


# ===============================================
# Utility Functions
# ===============================================

def calculate_stock_value(quantity, unit_price):
    """Calculate the raw stock value of one product."""
    return quantity * unit_price


def apply_category_discount(category, stock_value):
    """Apply the category discount and return discount and final value."""
    discount_rate = CATEGORY_DISCOUNTS.get(category, 0.00)
    discount = stock_value * discount_rate
    final_value = round(stock_value - discount, 2)

    return discount, final_value


def print_product_valuation(product):
    """Display one product's inventory valuation."""
    print(
        f"{product['product_name']:<11}: "
        f"stock value Rs.{product['stock_value']}, "
        f"final value Rs.{product['final_value']:.2f}"
    )


def print_category_totals(category_totals):
    """Display final inventory value for every category."""
    print("\n---Category Totals---")

    for category, total in category_totals.items():
        print(f"  {category:<11}: Rs.{total:.2f}")


# ===============================================
# Main Program
# ===============================================

def main():
    if not products:
        print("No products found.")
        return

    product_records = []
    category_totals = {}

    # ===========================================
    # Step 4: Calculate Every Product
    # ===========================================

    for product in product_list:
        stock_value = calculate_stock_value(
            product["quantity"],
            product["unit_price"]
        )

        discount, final_value = apply_category_discount(
            product["category"],
            stock_value
        )

        product_record = {
            "product_name": product["product_name"],
            "category": product["category"],
            "stock_value": stock_value,
            "discount": discount,
            "final_value": final_value,
        }

        product_records.append(product_record)

        category = product["category"]
        category_totals[category] = (
            category_totals.get(category, 0) + final_value
        )

    # ===========================================
    # Step 5: Display Product Valuation
    # ===========================================

    print(
        "\n================================"
        "Product Inventory Valuation"
        "================================\n"
    )

    for product in product_records:
        print_product_valuation(product)

    # ===========================================
    # Step 6: Display Category Totals
    # ===========================================

    print_category_totals(category_totals)

    # ===========================================
    # Step 7: Calculate Warehouse Summary
    # ===========================================

    grand_total = sum(category_totals.values())

    highest_category = max(
        category_totals,
        key=category_totals.get
    )

    high_value_stock = []

    for product in product_records:
        if product["final_value"] > HIGH_VALUE_THRESHOLD:
            high_value_stock.append(product["product_name"])

    # ===========================================
    # Step 8: Display Warehouse Summary
    # ===========================================

    print(f"\nGrand total     : Rs.{grand_total:.2f}")
    print(f"Highest category: {highest_category}")

    if high_value_stock:
        print(f"High Value Stock: {', '.join(high_value_stock)}")
    else:
        print("High Value Stock: None")


if __name__ == "__main__":
    main()
