# 🐍 Python Basics — BA Practice Tasks

> **Goal:** Build real-world Python skills used daily by Business Analysts.
> **Level:** Fresher | **Topics:** Variables, Data Types, Loops, Functions, File Handling

---

## 📋 Progress Tracker

| Task | Topic | Status | 
|------|-------|--------|
| Task 1 | Variables & Data Types | ⬜ |
| Task 2 | String Operations | ⬜ |
| Task 3 | Lists & Loops | ⬜ |
| Task 4 | Dictionaries | ⬜ |
| Task 5 | Functions | ⬜ |
| Task 6 | Conditions & Logic | ⬜ |
| Task 7 | File Handling (CSV) | ⬜ |
| Task 8 | Error Handling | ⬜ |
| Task 9 | List Comprehension | ⬜ |
| Task 10 | Mini Project | ⬜ |
---

## Task 1 — Variables & Data Types

**Real-World Context:** You receive a sales report summary as raw values. Store and display them properly.

### Question
```
A company's monthly report has the following values:
- Company name: "RetailCorp"
- Total Sales: 1500000
- Sales Growth (%): 12.5
- Target Achieved: True
- Region: None (not yet assigned)

1. Store each value in appropriate variables with correct data types.
2. Print each variable with its data type using type().
3. Calculate: What is the actual sales amount if growth is 12.5% over last month?
4. Format and print a summary line:
   "RetailCorp achieved sales of ₹15,00,000 with 12.5% growth. Target met: True"
```

### Expected Output
```
Company: RetailCorp | Type: <class 'str'>
Sales: 1500000 | Type: <class 'int'>
Growth: 12.5 | Type: <class 'float'>
Target: True | Type: <class 'bool'>
Region: None | Type: <class 'NoneType'>
Last Month Sales: 1333333.33
Summary: RetailCorp achieved sales of ₹15,00,000 with 12.5% growth. Target met: True
```

### Hint
```python
company = "RetailCorp"
sales = 1500000
# Use f-strings for formatting
# Last month = current / (1 + growth/100)
```

---

## Task 2 — String Operations

**Real-World Context:** You get messy customer names and emails from a CRM export. Clean and standardize them.

### Question
```
Raw data from CRM:
names = ["  john DOE  ", "MARY smith", "alex KUMAR  ", " priya SINGH"]
emails = ["John.Doe@Company.COM", "MARY.smith@Gmail.com", "Alex.kumar@outlook.COM"]

1. Clean all names: remove spaces, convert to Title Case (e.g., "John Doe")
2. Standardize all emails to lowercase
3. Extract the domain from each email (e.g., "company.com")
4. Check if any name contains "kumar" (case-insensitive)
5. Create a formatted ID for each customer: first 3 letters of first name + last 3 of last name
   e.g., John Doe → "johDoe", Mary Smith → "marith"
6. Count how many customers are from Gmail
```

### Expected Output
```
Cleaned Names: ['John Doe', 'Mary Smith', 'Alex Kumar', 'Priya Singh']
Emails (lowercase): ['john.doe@company.com', 'mary.smith@gmail.com', 'alex.kumar@outlook.com']
Domains: ['company.com', 'gmail.com', 'outlook.com']
Contains 'kumar': True
Customer IDs: ['johDoe', 'marit', 'aleumar']
Gmail count: 1
```

### Hint
```python
# strip(), title(), lower(), split('@'), find()
name.strip().title()
email.lower().split('@')[1]
```

---

## Task 3 — Lists & Loops

**Real-World Context:** You have a product sales list for Q1. Perform analysis using loops.

### Question
```
sales_data = [
    ["Product A", 45000], ["Product B", 72000], ["Product C", 31000],
    ["Product D", 89000], ["Product E", 15000], ["Product F", 62000],
    ["Product G", 55000], ["Product H", 23000]
]

1. Print all products with sales above ₹50,000
2. Find the total sales across all products
3. Find the product with the highest and lowest sales
4. Calculate the average sales
5. Classify each product as "High" (>60k), "Medium" (30k-60k), or "Low" (<30k)
6. Create a new list with only products that are above average
7. Sort products by sales in descending order
```

### Expected Output
```
Products above 50k: Product B, Product D, Product F, Product G
Total Sales: 392000
Highest: Product D (89000) | Lowest: Product E (15000)
Average Sales: 49000.0
Classification:
  Product A → Medium | Product B → High | Product C → Medium ...
Above Average Products: [['Product B', 72000], ['Product D', 89000], ...]
Sorted: [['Product D', 89000], ['Product B', 72000], ...]
```

---

## Task 4 — Dictionaries

**Real-World Context:** Employee data management — common in HR analytics.

### Question
```
employees = [
    {"id": "E001", "name": "Ravi Kumar", "dept": "Sales", "salary": 45000, "years": 3},
    {"id": "E002", "name": "Sneha Patel", "dept": "IT", "salary": 72000, "years": 5},
    {"id": "E003", "name": "Arjun Mehta", "dept": "Sales", "salary": 38000, "years": 2},
    {"id": "E004", "name": "Divya Nair", "dept": "HR", "salary": 52000, "years": 4},
    {"id": "E005", "name": "Karan Singh", "dept": "IT", "salary": 68000, "years": 6},
]

1. Print all employees in the IT department
2. Calculate average salary department-wise
3. Find all employees with more than 4 years of experience
4. Give a 10% salary hike to employees in Sales — update the dictionary
5. Add a new key "appraisal" to each employee:
   - "Excellent" if years >= 5
   - "Good" if years >= 3
   - "Average" otherwise
6. Find total salary cost per department
```

---

## Task 5 — Functions

**Real-World Context:** Create reusable functions for common BA calculations.

### Question
```
Build the following functions:

1. calculate_growth(current, previous) 
   → Returns growth percentage
   → Handle division by zero with a meaningful message

2. classify_customer(purchase_amount)
   → "Platinum" if > 100000
   → "Gold" if > 50000
   → "Silver" if > 20000
   → "Bronze" otherwise

3. format_indian_currency(amount)
   → Returns ₹1,50,000 format (Indian number system)

4. get_quarter(month_number)
   → Returns "Q1", "Q2", "Q3", or "Q4"

5. calculate_kpi(target, achieved)
   → Returns % achievement and a status: "Met", "Near Miss" (>90%), or "Missed"

Test each function with at least 3 different inputs.
```

---

## Task 6 — Conditions & Logic

**Real-World Context:** Business rule engine for order processing system.

### Question
```
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
```

---

## Task 7 — File Handling (CSV)

**Real-World Context:** Reading and writing sales reports — done daily by BAs.

### Question
```
1. Create a CSV file "sales_report.csv" with this data:
   Month, Region, Sales, Target, Achievement%
   January, North, 450000, 500000, ?
   February, South, 620000, 600000, ?
   March, East, 380000, 400000, ?
   April, West, 710000, 700000, ?

2. Calculate Achievement% = (Sales/Target)*100 — fill it while writing

3. Read the CSV back and:
   - Print all months where target was missed
   - Find the best performing region
   - Calculate total sales and overall achievement

4. Append a new row for May: West, 550000, 600000
   (Calculate achievement automatically)

5. Write a new filtered CSV with only rows where Achievement > 100%
```

### Hint
```python
import csv

# Writing
with open('sales_report.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Month', 'Region', 'Sales', 'Target', 'Achievement%'])

# Reading
with open('sales_report.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

---

## Task 8 — Error Handling

**Real-World Context:** Building a robust data validation tool.

### Question
```
You're building a data entry validator for a sales system.
Write functions with proper error handling for:

1. validate_sales_input(sales_str)
   - Convert string to float
   - Handle: empty string, non-numeric values, negative values
   - Return (True, value) or (False, error_message)

2. read_customer_file(filename)
   - Read a CSV file
   - Handle: file not found, permission error, empty file
   - Log errors to "error_log.txt" with timestamp

3. divide_metrics(numerator, denominator)
   - Handle division by zero
   - Handle non-numeric inputs
   - Return None for invalid, result for valid

Test each function with both valid and invalid inputs.
Use try/except/finally blocks properly.
```

---

## Task 9 — List Comprehension

**Real-World Context:** Quick data transformations on business datasets.

### Question
```
transactions = [
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
6. Filter out failed transactions and return only the cleaned list
```

---

## Task 10 — Mini Project: Monthly Sales Dashboard

**Real-World Context:** Build a complete sales summary tool from scratch.

### Question
```
Build a "Monthly Sales Dashboard" Python script that:

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

Use functions for each section. No external libraries — pure Python only.
```

---

## 📚 Resources

- **Practice Python:** [https://www.practicepython.org](https://www.practicepython.org)
- **Beginner Exercises:** [https://www.w3schools.com/python/exercise.asp](https://www.w3schools.com/python/exercise.asp)
- **Real Datasets:** [https://www.kaggle.com/datasets](https://www.kaggle.com/datasets)

---

*Update your status column daily. Mark ✅ when done, 🔄 when in progress.*
