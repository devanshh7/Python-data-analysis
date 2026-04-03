#6 Task 6 — Conditions & Logic

'''
Order Processing Rules:
- Orders above ₹10,000 get 5% discount
- Orders above ₹50,000 get 10% discount
- If customer is "Premium", add extra 5% on top
- If payment is "Prepaid", add extra 2% discount
- Minimum order value after all discounts must be ₹500
- If final amount < ₹500, set to ₹500 and flag as "Minimum Applied"

orders = [
    {"order_id": "O1", "amount": 8000, "customer_type": "Regular", "payment": "COD"},
    {"order_id": "O2", "amount": 55000, "customer_type": "Premium", "payment": "Prepaid"},
    {"order_id": "O3", "amount": 200, "customer_type": "Regular", "payment": "Prepaid"},
    {"order_id": "O4", "amount": 12000, "customer_type": "Premium", "payment": "COD"},
]

Write a function process_order(order) that returns final amount and discount applied.
Process all orders and print a summary table.
'''

# table
orders = [
    {"order_id": "O1", "amount": 8000, "customer_type": "Regular", "payment": "COD"},
    {"order_id": "O2", "amount": 55000, "customer_type": "Premium", "payment": "Prepaid"},
    {"order_id": "O3", "amount": 200, "customer_type": "Regular", "payment": "Prepaid"},
    {"order_id": "O4", "amount": 12000, "customer_type": "Premium", "payment": "COD"},
]
def process_order(order):
    amount= order["amount"]
    payment= order["payment"]
    customer_type= order["customer_type"]
    
    # dicount in total
    discount=0
    
    if amount> 50000:
        discount+=10
    elif amount> 10000:
        discount+=5
    
    # based on customer:
    
    if customer_type == "Premium":
        discount+=5
    
    # based on payment:
    if payment == "Prepaid":
        discount+=2
    final_amount = amount - (amount * discount / 100)
    
    f=""
    if final_amount <500:
        final_amount=500
        f="Minimum Applied"
        
    return final_amount, discount, f

print("Order ID | Original | Discount % | Final Amount | Flag")
print("-" * 60)

for order in orders:
    final_amount, discount, flag = process_order(order)
    
    print(f"{order['order_id']:8} | "
          f"{order['amount']:8} | "
          f"{discount:10}% | "
          f"{int(final_amount):12} | "
          f"{flag}")
    
    """print(f"{order['order_id']:8} | ₹{order['amount']:8} | {discount}% | ₹{int(final_amount):12} | {flag}")"""
    # To print in table format :8 -> Means: “Reserve 8 spaces for this value” ✔️ Used for alignment (table format)
    
    #print(f"{order['order_id']} | ₹{order['amount']} | {discount}% | ₹{final_amount} | {flag}")
    