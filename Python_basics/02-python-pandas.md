# 🐼 Pandas Library — BA Practice Tasks

> **Goal:** Master data manipulation using Pandas — the #1 BA Python skill.
> **Level:** Fresher | **Dataset:** E-Commerce Sales Data (create it yourself using code below)

---

## 📋 Progress Tracker

| Task | Topic | Status |
|------|-------|--------|
| Task 1 | DataFrame Creation & Basics | ⬜ |
| Task 2 | Data Cleaning | ⬜ |
| Task 3 | Filtering & Selection | ⬜ |
| Task 4 | GroupBy & Aggregation | ⬜ |
| Task 5 | Merging & Joining DataFrames | ⬜ |
| Task 6 | Pivot Tables | ⬜ |
| Task 7 | Date & Time Operations | ⬜ |
| Task 8 | Apply & Lambda Functions | ⬜ |
| Task 9 | Handling Missing Values | ⬜ |
| Task 10 | End-to-End Sales Analysis | ⬜ |

---

## 🗂️ Setup — Create Your Dataset First

```python
import pandas as pd
import numpy as np

# Run this block to create your working dataset
orders_data = {
    'order_id': ['O001','O002','O003','O004','O005','O006','O007','O008','O009','O010',
                 'O011','O012','O013','O014','O015','O016','O017','O018','O019','O020'],
    'customer_id': ['C01','C02','C01','C03','C04','C02','C05','C03','C06','C01',
                    'C04','C07','C05','C08','C06','C02','C09','C07','C08','C10'],
    'product': ['Laptop','Phone','Tablet','Laptop','Phone','Headphones','Tablet',
                'Phone','Laptop','Headphones','Tablet','Phone','Laptop','Tablet',
                'Phone','Laptop','Headphones','Tablet','Phone','Laptop'],
    'category': ['Electronics','Electronics','Electronics','Electronics','Electronics',
                 'Accessories','Electronics','Electronics','Electronics','Accessories',
                 'Electronics','Electronics','Electronics','Electronics','Electronics',
                 'Electronics','Accessories','Electronics','Electronics','Electronics'],
    'amount': [75000, 25000, 35000, 80000, 22000, 3500, 32000, 27000, 78000, 4200,
               33000, 24000, 82000, 36000, 26000, 79000, 3800, 31000, 23000, 85000],
    'quantity': [1, 2, 1, 1, 3, 2, 1, 2, 1, 3, 1, 1, 1, 2, 2, 1, 4, 1, 1, 1],
    'order_date': pd.date_range(start='2024-01-05', periods=20, freq='6D'),
    'region': ['North','South','East','West','North','South','East','West','North','South',
               'East','West','North','South','East','West','North','South','East','West'],
    'salesperson': ['Amit','Priya','Ravi','Sneha','Amit','Priya','Ravi','Sneha','Amit','Priya',
                    'Ravi','Sneha','Amit','Priya','Ravi','Sneha','Amit','Priya','Ravi','Sneha'],
    'discount': [0, 5, 10, 0, 5, 0, 10, 5, 0, 0, 10, 5, 0, 10, 5, 0, 0, 10, 5, 0],
    'status': ['Delivered','Delivered','Shipped','Delivered','Pending','Delivered',
               'Shipped','Delivered','Delivered','Pending','Delivered','Shipped',
               'Delivered','Delivered','Pending','Delivered','Shipped','Delivered','Delivered','Pending']
}

df = pd.DataFrame(orders_data)
df.to_csv('ecommerce_orders.csv', index=False)
print("Dataset created! Shape:", df.shape)
print(df.head())
```

---

## Task 1 — DataFrame Creation & Basics

**Real-World Context:** First thing every BA does — understand the dataset before analysis.

### Question
```python
# Load the dataset
df = pd.read_csv('ecommerce_orders.csv')

# Answer the following:

# Q1. How many rows and columns does the dataset have?
# Q2. What are the column names and their data types?
# Q3. Show the first 5 and last 5 rows
# Q4. Get basic statistics (mean, min, max, std) for numeric columns
# Q5. How many unique products are there? List them.
# Q6. What is the total sales amount (sum of 'amount' column)?
# Q7. How many orders are in each status category? (use value_counts)
# Q8. Display the orders sorted by amount in descending order — show top 5
```

### Expected Skills Used
`shape`, `dtypes`, `head()`, `tail()`, `describe()`, `nunique()`, `unique()`, `sum()`, `value_counts()`, `sort_values()`

---

## Task 2 — Data Cleaning

**Real-World Context:** Real data is messy. Cleaning is 60% of a BA's job.

### Question
```python
# Create a MESSY version of the dataset for cleaning practice
messy_data = {
    'order_id': ['O001','O002','O002','O003',None,'O005'],       # duplicate + null
    'customer_name': ['  Ravi Kumar ','PRIYA SHARMA','priya sharma','Amit Singh','Sneha',''],
    'amount': [15000, None, 25000, -500, 32000, 'N/A'],           # null, negative, string
    'email': ['ravi@gmail.com','PRIYA@GMAIL.COM','priya@gmail.com','amit@','sneha@gmail.com',''],
    'phone': ['9876543210', '987-654-3210', '98765', '9876543212', None, '9876543214'],
    'city': ['mumbai','DELHI','Delhi','Bangalore ','  Chennai','pune'],
}
messy_df = pd.DataFrame(messy_data)

# Tasks:
# Q1. Find all null values — show count per column
# Q2. Drop duplicate rows (based on order_id)
# Q3. Clean customer_name: strip spaces + Title Case
# Q4. Standardize city: strip + Title Case
# Q5. Remove rows where amount is null or negative or non-numeric
# Q6. Standardize email to lowercase
# Q7. Flag invalid emails (those not containing '@' and '.')
# Q8. Fill null phone with "Not Provided"
# Q9. Reset the index after cleaning
# Q10. Save the cleaned dataframe to "cleaned_orders.csv"
```

### Hint
```python
df.isnull().sum()
df.drop_duplicates(subset=['order_id'])
df['name'].str.strip().str.title()
pd.to_numeric(df['amount'], errors='coerce')  # converts invalid to NaN
```

---

## Task 3 — Filtering & Selection

**Real-World Context:** Answering specific business questions by slicing data.

### Question
```python
df = pd.read_csv('ecommerce_orders.csv')

# Answer these business questions using filters:

# Q1. Show all orders from the "North" region
# Q2. Find all orders with amount greater than ₹50,000
# Q3. Show all "Pending" orders from salesperson "Amit"
# Q4. Find orders where discount is 0 AND amount > 30000
# Q5. Show all orders for "Laptop" or "Tablet" (use isin)
# Q6. Find orders where amount is between ₹20,000 and ₹40,000
# Q7. Select only columns: order_id, product, amount, region
# Q8. Find the top 3 orders by amount in the "South" region
# Q9. Show orders where salesperson name starts with 'A' or 'P'
# Q10. Find orders placed in February 2024 (use order_date column)
```

### Hint
```python
df[df['region'] == 'North']
df[df['amount'].between(20000, 40000)]
df[df['product'].isin(['Laptop', 'Tablet'])]
df['order_date'] = pd.to_datetime(df['order_date'])
df[df['order_date'].dt.month == 2]
```

---

## Task 4 — GroupBy & Aggregation

**Real-World Context:** Summarizing sales performance — the core of BA reporting.

### Question
```python
df = pd.read_csv('ecommerce_orders.csv')

# Q1. Total sales amount by Region
# Q2. Average order amount by Product
# Q3. Total sales AND order count by Salesperson
# Q4. Maximum and minimum order amount by Category
# Q5. Total quantity sold by Product (sorted descending)
# Q6. How many orders per Status per Region? (multi-level groupby)
# Q7. What % of total sales does each Region contribute?
#     (hint: divide group sum by total sum * 100)
# Q8. Average discount offered by each Salesperson
# Q9. Total revenue per month (group by month of order_date)
# Q10. Find the salesperson with highest total sales in each region
```

### Hint
```python
df.groupby('region')['amount'].sum()
df.groupby('salesperson').agg({'amount': ['sum', 'count'], 'discount': 'mean'})
df.groupby('region')['amount'].sum() / df['amount'].sum() * 100
```

---

## Task 5 — Merging & Joining DataFrames

**Real-World Context:** Combining data from multiple sources — like joining orders with customer info.

### Question
```python
# Create 3 related dataframes:

customers = pd.DataFrame({
    'customer_id': ['C01','C02','C03','C04','C05','C06','C07','C08','C09'],
    'customer_name': ['Ravi Kumar','Priya Sharma','Amit Singh','Sneha Patel',
                      'Karan Mehta','Divya Nair','Rohit Gupta','Anita Joshi','Vikram Das'],
    'tier': ['Gold','Silver','Platinum','Silver','Gold','Bronze','Silver','Platinum','Bronze'],
    'city': ['Mumbai','Delhi','Bangalore','Chennai','Hyderabad','Pune','Kolkata','Ahmedabad','Jaipur']
})

products = pd.DataFrame({
    'product': ['Laptop','Phone','Tablet','Headphones'],
    'brand': ['Dell','Samsung','Apple','Sony'],
    'cost_price': [60000, 18000, 28000, 2500],
    'warranty_years': [2, 1, 1, 1]
})

df = pd.read_csv('ecommerce_orders.csv')

# Q1. Merge orders with customers on customer_id (INNER JOIN)
#     → How many orders matched?
# Q2. LEFT JOIN orders with customers — find orders with no customer info
# Q3. Merge orders with products on product name
#     → Calculate profit = amount - cost_price for each order
# Q4. After merging all 3: find profit by customer tier
# Q5. Find customers who have NEVER placed an order (use outer join + filter nulls)
# Q6. Which city generates the most revenue? (requires customer merge)
# Q7. Create a final "enriched_orders" dataframe with all info combined
#     Save it to "enriched_orders.csv"
```

### Hint
```python
pd.merge(df, customers, on='customer_id', how='inner')
pd.merge(df, customers, on='customer_id', how='left')
merged[merged['customer_name'].isnull()]  # no customer info
```

---

## Task 6 — Pivot Tables

**Real-World Context:** Creating summary reports like Excel pivot tables in Python.

### Question
```python
df = pd.read_csv('ecommerce_orders.csv')

# Q1. Create a pivot: Rows = Region, Columns = Product, Values = Total Amount
# Q2. Pivot: Salesperson vs Region showing COUNT of orders
# Q3. Pivot: Product vs Status showing total Amount + add row/column totals (margins=True)
# Q4. Multi-value pivot: Region vs Product showing both SUM of amount AND COUNT of orders
# Q5. Create a pivot showing average discount per Salesperson per Region
# Q6. From Q1 pivot — find which product has highest sales in each region
# Q7. Flatten the multi-index columns from Q4 into readable names
#     e.g., ('amount','sum') → 'amount_sum'
# Q8. Export the pivot table from Q3 to "pivot_report.csv"
```

### Hint
```python
pd.pivot_table(df, values='amount', index='region', columns='product', aggfunc='sum', fill_value=0)
pd.pivot_table(df, values='amount', index='region', columns='product',
               aggfunc='sum', margins=True, margins_name='Total')
```

---

## Task 7 — Date & Time Operations

**Real-World Context:** Time-based analysis is core to business reporting (MoM, QoQ trends).

### Question
```python
df = pd.read_csv('ecommerce_orders.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

# Q1. Extract year, month, day, day-of-week from order_date into separate columns
# Q2. Add a column "quarter" (Q1/Q2/Q3/Q4) based on order month
# Q3. Monthly sales trend — total amount per month
# Q4. Which day of the week has highest average sales?
# Q5. Add column "delivery_date" = order_date + 5 business days
# Q6. Calculate "days_since_order" = today's date - order_date
# Q7. Filter all orders placed on weekends
# Q8. Find orders placed in the last 30 days (from max order_date)
# Q9. Resample sales data to weekly totals (set order_date as index first)
# Q10. Create a "Month-Year" column like "Jan-2024" for reporting
```

### Hint
```python
df['month'] = df['order_date'].dt.month
df['day_name'] = df['order_date'].dt.day_name()
df['quarter'] = df['order_date'].dt.quarter.map({1:'Q1',2:'Q2',3:'Q3',4:'Q4'})
df.set_index('order_date').resample('W')['amount'].sum()
```

---

## Task 8 — Apply & Lambda Functions

**Real-World Context:** Applying business logic to transform data column by column.

### Question
```python
df = pd.read_csv('ecommerce_orders.csv')

# Q1. Add column "discount_amount" = amount * discount / 100
#     Use apply with lambda

# Q2. Add column "net_amount" = amount - discount_amount (after Q1)

# Q3. Add column "tax" = 18% of net_amount if category is "Electronics"
#                        12% if category is "Accessories"

# Q4. Add column "customer_tier_label":
#     Use apply on customer_id:
#     C01, C03, C08 → "Platinum" | C02, C05, C07 → "Gold" | rest → "Silver"

# Q5. Add column "order_size":
#     net_amount > 70000 → "Large"
#     net_amount > 30000 → "Medium"
#     otherwise → "Small"

# Q6. Create column "salesperson_code" = first 2 chars of name + "_" + region first char
#     e.g., Amit + North → "Am_N"  (use apply on multiple columns)

# Q7. Apply a function to flag "suspicious" orders:
#     discount == 0 AND amount > 70000 → True, else False
```

### Hint
```python
df['discount_amount'] = df.apply(lambda row: row['amount'] * row['discount'] / 100, axis=1)
df['order_size'] = df['net_amount'].apply(lambda x: 'Large' if x > 70000 else ('Medium' if x > 30000 else 'Small'))
df['code'] = df.apply(lambda row: row['salesperson'][:2] + '_' + row['region'][0], axis=1)
```

---

## Task 9 — Handling Missing Values

**Real-World Context:** Every real-world dataset has nulls. Knowing how to handle them is critical.

### Question
```python
# Create a dataset with intentional missing values
import numpy as np

df_missing = pd.read_csv('ecommerce_orders.csv')
# Introduce missing values
df_missing.loc[[2,5,8,12], 'amount'] = np.nan
df_missing.loc[[1,6,15], 'discount'] = np.nan
df_missing.loc[[3,9], 'region'] = np.nan
df_missing.loc[[0,7,14,19], 'salesperson'] = np.nan

# Q1. Count missing values in each column
# Q2. What % of data is missing in each column?
# Q3. Fill missing 'amount' with the MEDIAN amount
# Q4. Fill missing 'discount' with 0 (business rule: no discount if not specified)
# Q5. Fill missing 'region' with "Unknown"
# Q6. Fill missing 'salesperson' with the MOST FREQUENT salesperson (mode)
# Q7. Drop any rows that STILL have null values after filling
# Q8. Verify: show isnull().sum() again to confirm no nulls remain
# Q9. Use interpolation to fill amounts in a time-ordered series
#     (sort by order_date first, then interpolate 'amount')
# Q10. Compare: original row count vs cleaned row count
```

---

## Task 10 — End-to-End Sales Analysis Report

**Real-World Context:** Full BA deliverable — from raw data to insights.

### Question
```
Using ecommerce_orders.csv + customer and product tables from Task 5:

Build a complete "Q1 2024 Sales Analysis" script that produces:

SECTION 1 - Overview
- Total orders, total revenue, average order value
- Orders by status (count + %)

SECTION 2 - Product Performance
- Revenue, units sold, avg order value per product
- Best and worst performing product

SECTION 3 - Regional Analysis
- Revenue, order count, avg order value per region
- Region-wise top salesperson

SECTION 4 - Salesperson Scorecard
- Total sales, order count, avg discount given per salesperson
- Rank them

SECTION 5 - Customer Insights (after merging)
- Revenue per customer tier
- Top 3 customers by total spend
- Customers who placed more than 2 orders

SECTION 6 - Save to Files
- Full report to "sales_analysis.csv"
- Pivot summary to "pivot_summary.csv"
- Print a text summary to console

Use functions for each section. Add comments explaining your logic.
```

---

## 📚 Resources

- **Pandas Docs:** [https://pandas.pydata.org/docs](https://pandas.pydata.org/docs)
- **Kaggle Pandas Course:** [https://www.kaggle.com/learn/pandas](https://www.kaggle.com/learn/pandas)
- **Practice Dataset:** [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

*Update your status column daily. Mark ✅ when done, 🔄 when in progress.*
