1. What is a Pivot Table (in Pandas)?

👉 A pivot table is just:

**A way to summarize data by grouping + aggregating + reshaping**

It answers questions like:

- Total sales by region?
- Avg revenue per product?
- Count of orders per customer?

2. Core Idea (VERY IMPORTANT)

Pivot = 3 things combined:

- Group by (rows)
- Split by (columns)
- Aggregate (values)

**Mental Model**

Think like this:

```
Rows → grouping level
Columns → categories to spread
Values → what to calculate
```

3. Basic Syntax

```
pd.pivot_table(
    data=df,
    index='row_column',
    columns='column_category',
    values='value_column',
    aggfunc='sum'
)
```

4. Basic Pivot Example

```
pd.pivot_table(
    df,
    index='Region',
    values='Sales',
    aggfunc='sum'
)
```

👉 Output:

Region	Sales

North	300

South	450

🔹 5. Add Columns Dimension

```
pd.pivot_table(
    df,
    index='Region',
    columns='Product',
    values='Sales',
    aggfunc='sum'
)
```

👉 Output:

Region	A	B

North	100	200

South	150	300

🔹 6. Multiple Aggregations

```
pd.pivot_table(
    df,
    index='Region',
    values='Sales',
    aggfunc=['sum', 'mean', 'count']
)
```

🔹 7. Multiple Values

```
pd.pivot_table(
    df,
    index='Region',
    values=['Sales', 'Profit'],
    aggfunc='sum'
)
```

🔹 8. Fill Missing Values

```
pd.pivot_table(
    df,
    index='Region',
    columns='Product',
    values='Sales',
    aggfunc='sum',
    fill_value=0
)
```

👉 Prevents NaN

🔹 9. Margins (Grand Total)

```
pd.pivot_table(
    df,
    index='Region',
    columns='Product',
    values='Sales',
    aggfunc='sum',
    margins=True
)
```

👉 Adds:

Row total

Column total

🧠 5. Pivot vs GroupBy (IMPORTANT)


Feature  ||	pivot_table	 ||  groupby

Output shape   ||	Table format ||	Series/DataFrame

Handles missing	 ||	Yes	||	No

Multi-dimension	 ||	Easy   ||	Slightly complex

👉 Equivalent groupby:

`df.groupby(['Region', 'Product'])['Sales'].sum().unstack()`

⚠️ 6. Things to Keep in Mind (VERY IMPORTANT)

**🔴 1. Default aggregation = mean**

👉 If you don’t specify:

`aggfunc='mean'`

**🔴 2. Duplicate combinations**

👉 pivot_table handles duplicates using aggregation

👉 `pivot()` will FAIL

**🔴 3. Missing values**

👉 Always use:

`fill_value=0`

**🔴 4. MultiIndex output**

👉 You may get:

* Multi-level rows
* Multi-level columns

Fix:

`.reset_index()`

or

`.columns = ['col1', 'col2']`

**🔴 5. Data types matter**

👉 Aggregation works only on numeric columns

-------

**Real Interview Questions**

**✅ Q1: Total sales per region per product**

```
pd.pivot_table(
    df,
    index='Region',
    columns='Product',
    values='Sales',
    aggfunc='sum'
)
```

✅ Q2: Average order value per customer

```
pd.pivot_table(
    df,
    index='customer_id',
    values='order_amount',
    aggfunc='mean'
)
```

✅ Q3: Count of orders per region

```
pd.pivot_table(
    df,
    index='Region',
    values='order_id',
    aggfunc='count'
)
```

✅ Q4: Multi-level pivot

```
pd.pivot_table(
    df,
    index=['Region', 'Customer'],
    columns='Product',
    values='Sales',
    aggfunc='sum'
)
```

🚀 8. Advanced Tricks

🔹 Flatten column names

`pivot.columns = pivot.columns.map(str)`

🔹 Rename columns

`pivot = pivot.rename(columns={'A': 'Product_A'})`

🔹 Convert to normal dataframe

`pivot = pivot.reset_index()`