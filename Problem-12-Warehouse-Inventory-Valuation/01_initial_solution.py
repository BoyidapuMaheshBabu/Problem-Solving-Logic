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

category_total_list=[]

#discounts

ten_d=0.10

five_d=0.05

zero_d=0


def calculate_stockvalue(units,unit_price):

    return units*unit_price
     


product_list=[]

for pro in products:  

    values=pro

    keys=("product_name","category","quantity","unit_price")

    prodict=dict(zip(keys,values))

    product_list.append(prodict)

#print(product_list)


category=[]

product_name=[]

def append_name_or_category(key,target_list,data):
    seen=set()
    for target in target_list:

       value=target[key]

       if value not in seen:
            seen.add(value)
            data.append(value)

append_name_or_category("category",product_list,category)
append_name_or_category("product_name",product_list,product_name)
print()
print("================================Product Inventory Valuation================================")
print()
for name in product_name:

    for prod in product_list:

       if prod["product_name"] == name:

            stock_value=calculate_stockvalue(prod["quantity"],prod["unit_price"])
            
            if prod["category"] == "Electronics":
              dis_p=five_d
            elif prod["category"] == "Grocery":
              dis_p=ten_d
            else:
              dis_p=zero_d
            discount=stock_value*dis_p            
            final_value=stock_value - discount
            category_total_list.append({"name_product":prod["product_name"],"category_product":prod["category"],"final_value":final_value})
              
            
            print(f"{name:<11}: Stock value: Rs.{stock_value},    Final value: Rs.{final_value:.2f}")  
#print(category_total_list)

print()

print("---Category totals---")



for cat in category:
      total=0
      for category in category_total_list:
           if category["category_product"] == cat:
               total+=category["final_value"] 
      print(f"  {cat:<11}: Rs.{total:.2f}")
print()

high_value_stock=[]

for category in category_total_list:
           if category["final_value"] > 10000:
               high_value_stock.append(category["name_product"])

print("---High value stock---")
print()
for name in high_value_stock:
  print(name)
print()