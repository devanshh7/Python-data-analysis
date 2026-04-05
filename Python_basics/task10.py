#10 Task 10 — Mini Project: Monthly Sales Dashboard

'''Build a "Monthly Sales Dashboard" Python script that:

INPUT: A list of daily sales records:
daily_sales = [
    {"date": "2024-01-01", "salesperson": "Amit", "region": "North", "amount": 15000, "product": "Laptop"},
    {"date": "2024-01-01", "salesperson": "Priya", "region": "South", "amount": 8000, "product": "Phone"},
    # ... (create at least 15 records yourself across different people, regions, products)
]

OUTPUT (printed to console AND saved to "dashboard_report.txt"):
==== MONTHLY SALES DASHBOARD - JANUARY 2024 ====
Total Sales: ₹X,XX,XXX
Top Salesperson: Amit (₹XX,XXX)
Top Region: North (₹XX,XXX)
Top Product: Laptop (₹XX,XXX)

--- Region-wise Breakdown ---
North: ₹XX,XXX (XX%)
South: ₹XX,XXX (XX%)

--- Salesperson Rankings ---
1. Amit - ₹XX,XXX
2. Priya - ₹XX,XXX

--- Daily Average Sales: ₹XX,XXX ---
Days above average: X

Use functions for each section. No external libraries — pure Python only.'''

import random
from datetime import datetime, timedelta

salespeople = ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Neha", "Arjun", "Pooja"]
regions = ["North", "South", "East", "West"]
products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]

start_date = datetime(2024, 1, 1)

daily_sales = []

for i in range(150):
    record = {
        "date": (start_date + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d"),
        "salesperson": random.choice(salespeople),
        "region": random.choice(regions),
        "amount": random.randint(5000, 50000),
        "product": random.choice(products)
    }
    daily_sales.append(record)

# Print first 5 records to check
'''for i in range(5):
    print(daily_sales[i])  '''

print("==== MONTHLY SALES DASHBOARD - JANUARY 2024 ====")

total_sales = sum(daily_sales[i]['amount'] for i in range(len(daily_sales)))
print(f"Total Sales: ₹{total_sales:,}")

#total_sales = sum(record["amount"] for record in daily_sales)

#2. Top Salesperson
sales_by_person = {}
for record in daily_sales:
    salesperson= record["salesperson"]
    amount= record["amount"]
    if salesperson in sales_by_person:
        sales_by_person[salesperson] += amount
    else:
        sales_by_person[salesperson] = amount
# top_sp= max(sales_by_person, key=sales_by_person.get)
# print(f"Top Salesperson: {top_sp} (₹{sales_by_person[top_sp]:,})")

top_sp = None
max_sales = 0

for person in sales_by_person:
    if sales_by_person[person] > max_sales:
        max_sales = sales_by_person[person]
        top_sp = person
print(f"Top Salesperson: {top_sp}, Sales: ₹{max_sales:,}")

# 3. Top Region
sales_by_region={}
for record in daily_sales:
    region= record["region"]
    amount= record["amount"]
    if region in sales_by_region:
        sales_by_region[region] += amount
    else:
        sales_by_region[region] = amount

top_region = None
max_region_sales = 0

for region in sales_by_region:
    if sales_by_region[region] > max_region_sales:
        max_region_sales = sales_by_region[region]
        top_region = region

print(f"Top Region: {top_region}, Sales: ₹{max_region_sales:,}")

# 4. Top Product
sales_by_product = {}
for record in daily_sales:
    product = record["product"]
    amount = record["amount"]
    if product in sales_by_product:
        sales_by_product[product] += amount
    else:
        sales_by_product[product] = amount

top_product = None
max_product_sales = 0

for product in sales_by_product:
    if sales_by_product[product] > max_product_sales:
        max_product_sales = sales_by_product[product]
        top_product = product

print(f"Top Product: {top_product}, Sales: ₹{max_product_sales:,}")

print("\n--- Region-wise Breakdown ---")
