#Task 9 — List Comprehension
'''transactions = [
    {"id": "T1", "amount": 1500, "status": "completed", "category": "Electronics"},
    {"id": "T2", "amount": 300, "status": "pending", "category": "Clothing"},
    {"id": "T3", "amount": 8900, "status": "completed", "category": "Electronics"},
    {"id": "T4", "amount": 450, "status": "failed", "category": "Food"},
    {"id": "T5", "amount": 2200, "status": "completed", "category": "Clothing"},
    {"id": "T6", "amount": 5600, "status": "completed", "category": "Electronics"},
]

Using LIST COMPREHENSIONS (single line), solve:
1. Get all transaction IDs where status is "completed"
2. Get amounts of all Electronics transactions
3. Add 18% GST to all completed transaction amounts
4. Get a list of (id, amount) tuples for transactions > 1000
5. Create a list of formatted strings: "T1: ₹1,500 [completed]" for each transaction
6. Filter out failed transactions and return only the cleaned list'''

transactions = [
    {"id": "T1", "amount": 1500, "status": "completed", "category": "Electronics"},
    {"id": "T2", "amount": 300, "status": "pending", "category": "Clothing"},
    {"id": "T3", "amount": 8900, "status": "completed", "category": "Electronics"},
    {"id": "T4", "amount": 450, "status": "failed", "category": "Food"},
    {"id": "T5", "amount": 2200, "status": "completed", "category": "Clothing"},
    {"id": "T6", "amount": 5600, "status": "completed", "category": "Electronics"},
]

for i in transactions:
    if i["status"]=="completed":
        print(f'{i["id"]},{i["status"]}')

print("-----------------------------------------")
#2 Get amounts of all Electronics transactions
a=0
for j in transactions:
    
    if j["category"]=="Electronics":
        a+=j["amount"]
print("Total amount of Electronics transactions:",a)

print("-----------------------------------------")
#. Add 18% GST to all completed transaction amounts
print("--Adding 18% GST to all completed transaction amounts---")
for j in transactions:
    
    if j["status"]=="completed":
        
        print(f'{j["id"]},{j["amount"]*1.18}')

print("-----------------------------------------")
#4. Get a list of (id, amount) tuples for transactions > 1000
print("--List of (id, amount) for transactions > 1000--")
for j in transactions:
    
    if j["amount"]>1000:
        
        print(f'{j["id"]},{j["amount"]}')


print("-----------------------------------------")

#5. Create a list of formatted strings: "T1: ₹1,500 [completed]" for each transaction

print("--List of formatted strings for each transaction--")
for j in transactions:
    print(f'{j["id"]}: ₹{j["amount"]} [{j["status"]}]')



#6. Filter out failed transactions and return only the cleaned list'''

print("-----------------------------------------")

print("-- Filter out failed transactions and return only the cleaned list--")
for j in transactions:
    if j["status"]!= "failed":
        print(j)