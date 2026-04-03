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