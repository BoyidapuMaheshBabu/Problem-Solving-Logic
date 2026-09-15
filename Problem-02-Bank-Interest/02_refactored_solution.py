"""
Bank Interest Calculator

Description:
This program calculates the interest earned based on the account balance.
It also applies a bonus and tax for higher balance accounts.

Interest Rates:
- ₹0 or less        : No interest
- Up to ₹10,000     : 2%
- ₹10,001–₹50,000   : 4%
- ₹50,001–₹100,000  : 6% + ₹500 bonus
- Above ₹100,000    : 8% + ₹500 bonus - 5% tax on interest
"""

# -------------------------------
# User Input
# -------------------------------

balance_amount = float(input("Enter the account balance (₹): "))

# -------------------------------
# Constants
# -------------------------------

BONUS = 500          # Bonus for eligible accounts
TAX_RATE = 0.05      # 5% tax on interest

# Interest rates for different balance ranges
TIER1_RATE = 0.02
TIER2_RATE = 0.04
TIER3_RATE = 0.06
TIER4_RATE = 0.08

# -------------------------------
# Interest Calculation
# -------------------------------

# Invalid or zero balance
if balance_amount <= 0:
    print("No interest earned, because the balance is invalid.")

# Balance up to ₹10,000
elif balance_amount <= 10000:
    interest = balance_amount * TIER1_RATE
    print(f"Interest Earned: ₹{interest:.2f}")

# Balance from ₹10,001 to ₹50,000
elif balance_amount <= 50000:
    interest = balance_amount * TIER2_RATE
    print(f"Interest Earned: ₹{interest:.2f}")

# Balance from ₹50,001 to ₹100,000
elif balance_amount <= 100000:
    interest = balance_amount * TIER3_RATE
    total_interest = interest + BONUS

    print(f"Interest: ₹{interest:.2f}")
    print(f"Bonus: ₹{BONUS:.2f}")
    print(f"Total Interest Earned: ₹{total_interest:.2f}")

# Balance above ₹100,000
else:
    interest = balance_amount * TIER4_RATE
    total_interest = interest + BONUS
    tax_amount = total_interest * TAX_RATE
    final_amount = total_interest - tax_amount

    print(f"Interest: ₹{interest:.2f}")
    print(f"Bonus: ₹{BONUS:.2f}")
    print(f"Tax Deducted (5%): ₹{tax_amount:.2f}")
    print(f"Final Interest Earned: ₹{final_amount:.2f}")
