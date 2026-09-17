balance_amount=float(input("Enter the account balance:"))
bonus=500
tax=0.05
tier1_interest=0.02
tier2_interest=0.04
tier3_interest=0.06
tier4_interest=0.08
if balance_amount<=0:
    print("No intrest earned ,because inflicted balnace")
elif balance_amount <=10000:
    interest_amount=balance_amount*tier1_interest
    print(f"Interest earned is ₹{interest_amount:.2f}")
elif balance_amount>10000 and balance_amount<=50000:
    interest_amount=balance_amount*tier2_interest
    print(f"Interest earned is ₹{interest_amount:.2f}")
elif balance_amount>50000 and balance_amount<=100000:      
        interest_amount=balance_amount*tier3_interest
        total_interest=interest_amount+bonus
        print(f"Interest earned is ₹{total_interest:.2f}")
elif balance_amount>100000:
        interest_amount=balance_amount*tier4_interest
        total_interest=interest_amount+bonus
        tax_on_interest=total_interest*tax
        total_earned=total_interest-tax_on_interest
        print(f"Interest earned is ₹{total_earned:.2f}")