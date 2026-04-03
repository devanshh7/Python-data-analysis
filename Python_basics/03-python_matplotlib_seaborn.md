# 📈 Python Data Visualization — Matplotlib & Seaborn Practice

> **Goal:** Create business-ready charts and visual reports using Python.
> **Level:** Fresher | **Uses:** Same e-commerce dataset from Pandas file (02_Python_Pandas.md)
> **Real-World Context:** BAs use these to build visual reports when Excel isn't enough
>   and to automate chart generation from large datasets.

---

## 📋 Progress Tracker

| Task | Topic | Library | Status | 
|------|-------|---------|--------|
| Task 1 | Setup & Your First Chart | Matplotlib | ⬜ |
| Task 2 | Bar Charts (Sales Comparison) | Matplotlib | ⬜ |
| Task 3 | Line Charts (Trends Over Time) | Matplotlib | ⬜ |
| Task 4 | Pie & Donut Charts | Matplotlib | ⬜ |
| Task 5 | Histograms & Distributions | Seaborn | ⬜ |
| Task 6 | Box Plots (Outlier Detection) | Seaborn | ⬜ |
| Task 7 | Heatmaps (Correlation & Pivot) | Seaborn | ⬜ |
| Task 8 | Scatter Plots (Relationship Analysis) | Seaborn | ⬜ |
| Task 9 | Subplots (Multi-chart Dashboard) | Matplotlib | ⬜ |
| Task 10 | Full Visual Report (End-to-End) | Both | ⬜ |
---

## 🔧 Setup — Install & Import

```python
pip install matplotlib seaborn pandas numpy
```

```python
# Standard imports — put this at the top of every file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# Styling — makes charts look professional
plt.rcParams['figure.figsize'] = (10, 6)      # default chart size
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.spines.top'] = False        # remove top border
plt.rcParams['axes.spines.right'] = False      # remove right border
sns.set_theme(style="whitegrid")               # seaborn default theme

print("Libraries loaded ✅")
```

---

## 🗂️ Dataset — Recreate From Pandas File

```python
# Run this block to create your working dataset
# (Same as 02_Python_Pandas.md — skip if already created)

data = {
    'order_id':    ['O001','O002','O003','O004','O005','O006','O007','O008',
                    'O009','O010','O011','O012','O013','O014','O015','O016',
                    'O017','O018','O019','O020'],
    'customer_id': ['C01','C02','C01','C03','C04','C02','C05','C03','C06',
                    'C01','C04','C07','C05','C08','C06','C02','C09','C07','C08','C10'],
    'product':     ['Laptop','Phone','Tablet','Laptop','Phone','Headphones','Tablet',
                    'Phone','Laptop','Headphones','Tablet','Phone','Laptop','Tablet',
                    'Phone','Laptop','Headphones','Tablet','Phone','Laptop'],
    'category':    ['Electronics','Electronics','Electronics','Electronics','Electronics',
                    'Accessories','Electronics','Electronics','Electronics','Accessories',
                    'Electronics','Electronics','Electronics','Electronics','Electronics',
                    'Electronics','Accessories','Electronics','Electronics','Electronics'],
    'amount':      [75000,25000,35000,80000,22000,3500,32000,27000,78000,4200,
                    33000,24000,82000,36000,26000,79000,3800,31000,23000,85000],
    'quantity':    [1,2,1,1,3,2,1,2,1,3,1,1,1,2,2,1,4,1,1,1],
    'order_date':  pd.date_range(start='2024-01-05', periods=20, freq='6D'),
    'region':      ['North','South','East','West','North','South','East','West',
                    'North','South','East','West','North','South','East','West',
                    'North','South','East','West'],
    'salesperson': ['Amit','Priya','Ravi','Sneha','Amit','Priya','Ravi','Sneha',
                    'Amit','Priya','Ravi','Sneha','Amit','Priya','Ravi','Sneha',
                    'Amit','Priya','Ravi','Sneha'],
    'discount':    [0,5,10,0,5,0,10,5,0,0,10,5,0,10,5,0,0,10,5,0],
    'status':      ['Delivered','Delivered','Shipped','Delivered','Pending',
                    'Delivered','Shipped','Delivered','Delivered','Pending',
                    'Delivered','Shipped','Delivered','Delivered','Pending',
                    'Delivered','Shipped','Delivered','Delivered','Pending']
}

df = pd.DataFrame(data)
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.strftime('%b')   # Jan, Feb, Mar...
df['month_num'] = df['order_date'].dt.month
df['net_amount'] = df['amount'] * (1 - df['discount']/100)

print("Dataset ready ✅  Shape:", df.shape)
print(df.head(3))
```

---

## Task 1 — Setup & Your First Chart

**Real-World Context:** Understanding the anatomy of a matplotlib figure before building complex charts.

### Question
```python
# Q1. Create a simple vertical bar chart of total sales per product
# Use this summarized data:
product_sales = df.groupby('product')['amount'].sum().sort_values(ascending=False)

# Build a bar chart with:
# - Title: "Total Sales by Product"
# - X-axis label: "Product"
# - Y-axis label: "Total Sales (₹)"
# - Bar color: steelblue
# - Add value labels ON TOP of each bar (annotate)
# - Save it as "chart_01_product_sales.png"

# Q2. Change bar color to a custom hex code (#2E86AB) and observe the difference

# Q3. Add a horizontal red dashed line showing the AVERAGE sales
#     Label it "Avg: ₹XX,XXX"
#     Use: plt.axhline(y=avg, color='red', linestyle='--', label='Average')

# Q4. Add a legend. Then call plt.tight_layout() before saving — see what it does.

# Q5. UNDERSTAND THIS OUTPUT:
#     Print what type 'fig' and 'ax' are after:
fig, ax = plt.subplots()
#     Why do we use fig, ax = plt.subplots() instead of just plt.bar()?
#     Answer in a comment in your code.
```

### Key Concepts to Learn
```python
# Anatomy of a matplotlib chart:
fig, ax = plt.subplots(figsize=(10, 6))   # fig = whole canvas, ax = one chart area

ax.bar(x, y)                   # draw bars
ax.set_title("Title")          # chart title
ax.set_xlabel("X label")       # x axis label
ax.set_ylabel("Y label")       # y axis label
ax.legend()                    # show legend
plt.tight_layout()             # auto-adjust spacing
plt.savefig("chart.png", dpi=150, bbox_inches='tight')  # save
plt.show()                     # display
```

---

## Task 2 — Bar Charts (Sales Comparison)

**Real-World Context:** Comparing performance across categories, regions, or time periods.

### Questions
```python
# Q1. HORIZONTAL BAR CHART — Salesperson total revenue
#     (horizontal is better when labels are long)
#     Sort bars from highest to lowest (descending on y-axis = ascending for barh)
#     Add value labels at end of each bar
#     Color: use a different color per bar using a colormap

# Q2. GROUPED BAR CHART — Sales by Region AND Category side by side
#     Hint: use df.groupby(['region','category'])['amount'].sum().unstack()
#     Then call .plot(kind='bar') on the result
#     Add legend, title, rotate x-axis labels by 45 degrees

# Q3. STACKED BAR CHART — Same data as Q2 but stacked
#     Change: .plot(kind='bar', stacked=True)
#     When is stacked better than grouped? Add your answer as a comment.

# Q4. Add formatted Y-axis tick labels showing ₹ symbol and K/L suffix
#     e.g., 75000 → "₹75K"
#     Hint: use ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'₹{x/1000:.0f}K'))

# Q5. SEABORN BAR CHART — Reproduce Q1 using seaborn
#     sns.barplot(data=df, x='salesperson', y='amount', estimator='sum', ci=None)
#     Compare: what does seaborn give you that matplotlib doesn't by default?
#     (Answer: confidence intervals, better default styling, less code)
```

### Hint
```python
# Grouped bar chart
pivot = df.groupby(['region','category'])['amount'].sum().unstack(fill_value=0)
pivot.plot(kind='bar', figsize=(10,6), colormap='Set2')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Adding value labels on bars
for bar in ax.patches:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 500,
            f'₹{bar.get_height():,.0f}',
            ha='center', va='bottom', fontsize=9)
```

---

## Task 3 — Line Charts (Trends Over Time)

**Real-World Context:** Showing sales trends over months — the most common BA chart type.

### Questions
```python
# Q1. BASIC LINE CHART — Monthly total sales over time
#     X-axis: Month | Y-axis: Total Sales
#     Add circular markers at each data point
#     Add data labels above each point

# Q2. MULTI-LINE CHART — Monthly sales for each salesperson on same chart
#     Each salesperson = one line with different color
#     Add legend showing who is who
#     Hint: groupby(['month_num','salesperson'])['amount'].sum().unstack()

# Q3. Add a shaded area under the total sales line (fill_between)
#     This visually emphasizes the trend
#     ax.fill_between(x, y, alpha=0.15, color='steelblue')

# Q4. DUAL AXIS LINE CHART — 
#     Left Y-axis: Total Sales (line, blue)
#     Right Y-axis: Number of Orders (line, orange, dashed)
#     Use: ax2 = ax.twinx()
#     This is called a secondary axis — very commonly asked in interviews

# Q5. Add vertical reference lines for important events:
#     Add a vertical dashed line at February with label "New Campaign Launch"
#     ax.axvline(x=feb_position, color='green', linestyle=':', label='Campaign')
```

### Hint
```python
monthly = df.groupby('month_num')['amount'].sum().reset_index()
monthly = monthly.sort_values('month_num')

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(monthly['month_num'], monthly['amount'],
        marker='o', linewidth=2.5, color='#2E86AB', markersize=8)

# Label each point
for _, row in monthly.iterrows():
    ax.annotate(f"₹{row['amount']/1000:.0f}K",
                xy=(row['month_num'], row['amount']),
                xytext=(0, 10), textcoords='offset points',
                ha='center', fontsize=9)
```

---

## Task 4 — Pie & Donut Charts

**Real-World Context:** Showing proportions — used carefully (pie charts are often misused!).

### Questions
```python
# Q1. PIE CHART — Sales share by Category
#     Show percentage labels inside slices
#     Explode (pull out) the largest slice slightly
#     Add a title and legend

# Q2. DONUT CHART — Same data as Q1 but as a donut
#     Add total sales in the center of the donut
#     Hint: draw a white circle on top of a pie chart
#     fig, ax = plt.subplots()
#     ax.pie(sizes, ...)
#     center_circle = plt.Circle((0,0), 0.65, color='white')
#     ax.add_artist(center_circle)

# Q3. SEABORN alternative — Seaborn doesn't have pie charts natively
#     Recreate Q1 using a horizontal bar chart instead
#     This is actually considered BETTER practice than pie charts — why?
#     (Answer in a comment: pie charts are hard to compare slices,
#      bar charts make comparison immediate)

# Q4. Regional share pie chart:
#     Show each region's % of total revenue
#     Color the slices using a custom color list: ['#264653','#2a9d8f','#e9c46a','#e76f51']

# Q5. Side-by-side pies — fig with 2 subplots:
#     Left: Sales by Category | Right: Orders by Status
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
```

---

## Task 5 — Histograms & Distributions

**Real-World Context:** Understanding how data is distributed — used in outlier detection and pricing analysis.

### Questions
```python
# Q1. HISTOGRAM — Distribution of order amounts
#     bins=10, color='steelblue', edgecolor='white'
#     What does the shape tell you? (right-skewed = most orders are low value)
#     Add mean and median as vertical lines

# Q2. Change bins to 5, then 20 — observe how shape perception changes
#     Which bin count gives the most honest view?

# Q3. SEABORN HISTPLOT — Reproduce Q1 with seaborn
#     sns.histplot(df['amount'], bins=10, kde=True)
#     What does kde=True add? (kernel density estimate = smooth curve)

# Q4. DISTRIBUTION BY GROUP — Show amount distribution for each category
#     sns.histplot(data=df, x='amount', hue='category', bins=8, alpha=0.6)
#     hue separates by category with different colors

# Q5. KDE PLOT (Kernel Density Estimate) — Smooth distribution curve
#     sns.kdeplot(data=df, x='amount', hue='salesperson', fill=True, alpha=0.3)
#     Which salesperson handles mostly high-value orders?

# Q6. ECDF (Empirical Cumulative Distribution) — Business use:
#     "What % of orders are below ₹30,000?"
#     sns.ecdfplot(data=df, x='amount')
#     Read the chart: at x=30000, what is the y value?
```

---

## Task 6 — Box Plots (Outlier Detection)

**Real-World Context:** Identifying outliers in sales data — used in fraud detection and quality analysis.

### Questions
```python
# Q1. BASIC BOX PLOT — Distribution of order amounts
#     sns.boxplot(y=df['amount'])
#     Identify: median line, IQR box, whiskers, outlier dots

# Q2. Box plot by category — Compare amount distributions across regions
#     sns.boxplot(data=df, x='region', y='amount', palette='Set2')
#     Which region has the widest spread? Which has outliers?

# Q3. BOX PLOT + STRIP PLOT OVERLAY — Show actual data points ON the box plot
#     First: sns.boxplot(..., showfliers=False)   # hide default outlier dots
#     Then: sns.stripplot(data=df, x='region', y='amount', color='black', alpha=0.5, size=5)
#     This gives a richer view than box alone

# Q4. VIOLIN PLOT — More detailed than box plot (shows full distribution shape)
#     sns.violinplot(data=df, x='salesperson', y='amount', palette='muted')
#     When is violin better than box? (when distribution shape matters)

# Q5. MATPLOTLIB BOX PLOT — Create a box plot with custom styling:
#     - Box color: lightblue
#     - Median line: red
#     - Outlier dots: orange diamonds
#     fig, ax = plt.subplots()
#     bp = ax.boxplot(df['amount'], patch_artist=True,
#                     medianprops=dict(color='red', linewidth=2),
#                     flierprops=dict(marker='D', color='orange'))
#     bp['boxes'][0].set_facecolor('lightblue')
```

---

## Task 7 — Heatmaps (Correlation & Pivot Visualization)

**Real-World Context:** Spotting patterns across two dimensions — used in market basket analysis and performance matrices.

### Questions
```python
# Q1. PIVOT HEATMAP — Sales by Region × Product
#     Step 1: create pivot table
pivot = df.pivot_table(values='amount', index='region',
                        columns='product', aggfunc='sum', fill_value=0)
#     Step 2: plot heatmap
#     sns.heatmap(pivot, annot=True, fmt=',', cmap='YlOrRd')
#     annot=True shows values in each cell
#     fmt=',' adds comma formatting to numbers

# Q2. Customize the heatmap:
#     - Change colormap to 'Blues'
#     - Add a title
#     - Rotate x-axis labels 45 degrees
#     - Change annotation font size to 8

# Q3. CORRELATION HEATMAP — Do numeric columns correlate?
#     numeric_cols = df[['amount','quantity','discount','net_amount']]
#     corr = numeric_cols.corr()
#     sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
#                 vmin=-1, vmax=1, center=0, square=True)
#     Interpret: which columns are positively/negatively correlated?

# Q4. MONTHLY × SALESPERSON heatmap:
#     Rows: Month | Columns: Salesperson | Values: Total Revenue
#     Which salesperson had a bad month? Which had a great one?

# Q5. Mask the upper triangle of the correlation heatmap (remove redundancy):
#     import numpy as np
#     mask = np.triu(np.ones_like(corr, dtype=bool))
#     sns.heatmap(corr, mask=mask, annot=True, ...)
#     This is a professional touch that impresses interviewers
```

---

## Task 8 — Scatter Plots (Relationship Analysis)

**Real-World Context:** Exploring relationships between two variables — e.g., "Does discount increase sales volume?"

### Questions
```python
# Q1. BASIC SCATTER — Amount vs Quantity
#     Does ordering more quantity mean higher total amount?
#     plt.scatter(df['quantity'], df['amount'], alpha=0.6, color='steelblue')
#     Add a trend line using np.polyfit

# Q2. COLORED SCATTER — Same chart but color each point by category
#     sns.scatterplot(data=df, x='quantity', y='amount',
#                     hue='category', palette='Set1', s=100)
#     s=100 sets marker size

# Q3. SIZE-ENCODED SCATTER (Bubble Chart) — Add a 3rd dimension via dot size
#     sns.scatterplot(data=df, x='quantity', y='amount',
#                     hue='region', size='discount',
#                     sizes=(50, 400), palette='Set2')
#     Size = discount level. Which orders had both high discount and high amount?

# Q4. ADD REGRESSION LINE — seaborn makes this easy
#     sns.regplot(data=df, x='discount', y='amount',
#                 scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
#     Does giving more discount correlate with higher order value? Interpret.

# Q5. SEABORN PAIRPLOT — Check ALL numeric column relationships at once
#     numeric_df = df[['amount','quantity','discount','net_amount']]
#     sns.pairplot(numeric_df, diag_kind='kde', plot_kws={'alpha':0.5})
#     This creates a grid of scatter plots — very useful for quick EDA
#     EDA = Exploratory Data Analysis (term to know for interviews!)
```

---

## Task 9 — Subplots (Multi-Chart Dashboard)

**Real-World Context:** Combining multiple charts into a single figure — used when creating automated reports.

### Questions
```python
# Q1. 2×2 SUBPLOT GRID — 4 charts in one figure
#     fig, axes = plt.subplots(2, 2, figsize=(14, 10))
#     Top-left:     Bar — Sales by Region         (axes[0,0])
#     Top-right:    Line — Monthly Sales Trend    (axes[0,1])
#     Bottom-left:  Pie — Category Share          (axes[1,0])
#     Bottom-right: Box — Amount by Salesperson   (axes[1,1])
#     Add fig.suptitle("Sales Dashboard", fontsize=16, fontweight='bold')

# Q2. UNEQUAL SUBPLOT SIZES using gridspec
#     import matplotlib.gridspec as gridspec
#     fig = plt.figure(figsize=(14, 10))
#     gs = gridspec.GridSpec(2, 3)         # 2 rows, 3 columns
#     ax1 = fig.add_subplot(gs[0, :2])     # top-left: spans 2 columns (wide chart)
#     ax2 = fig.add_subplot(gs[0, 2])      # top-right: 1 column
#     ax3 = fig.add_subplot(gs[1, :])      # bottom: full width
#     This layout is common in executive dashboards

# Q3. SHARED AXES — Two line charts sharing the same x-axis (time)
#     fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))
#     ax1: Total Sales over months
#     ax2: Order count over months
#     sharex=True keeps them in sync when you zoom

# Q4. SEABORN FACETGRID — Automatically create one chart per group
#     g = sns.FacetGrid(df, col='region', col_wrap=2, height=4)
#     g.map(sns.barplot, 'product', 'amount', estimator=sum, ci=None)
#     g.set_xticklabels(rotation=45)
#     This creates one bar chart per region automatically — very powerful!

# Q5. MIXED CHART TYPES in subplots:
#     Left: sns.heatmap (region × product sales)
#     Right: sns.boxplot (amount by salesperson)
#     Note: seaborn charts need ax= parameter when used in subplots
#     sns.heatmap(pivot, ax=axes[0], ...)
#     sns.boxplot(data=df, x='salesperson', y='amount', ax=axes[1])
```

---

## Task 10 — Full Visual Report (End-to-End)

**Real-World Context:** Automated visual report generation — a skill that can set you apart from other freshers.

### Goal
```
Build a complete "Monthly Sales Visual Report" saved as a single PNG file.

The figure should have this layout (3 rows, 2-3 columns):

┌─────────────────────────────────────────────────────┐
│          📊 SALES PERFORMANCE REPORT — 2024          │
│          Generated: {today's date}                   │
├─────────────────────┬───────────────────────────────┤
│  Bar: Sales by      │  Line: Monthly Sales Trend    │
│  Salesperson        │  (with order count secondary) │
├─────────────────────┬───────────────────────────────┤
│  Heatmap: Region ×  │  Box: Amount Distribution     │
│  Product Revenue    │  by Region                    │
├─────────────────────┴───────────────────────────────┤
│  Stacked Bar: Product sales by Region (full width)  │
└─────────────────────────────────────────────────────┘
```

### Implementation Steps
```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import pandas as pd
from datetime import date

# STEP 1: Prepare all aggregated data
salesperson_sales = df.groupby('salesperson')['amount'].sum().sort_values()
monthly_sales = df.groupby('month_num')['amount'].sum()
monthly_orders = df.groupby('month_num')['order_id'].count()
region_product = df.pivot_table('amount','region','product',aggfunc='sum',fill_value=0)
stacked_data = df.groupby(['product','region'])['amount'].sum().unstack(fill_value=0)

# STEP 2: Create figure with gridspec
fig = plt.figure(figsize=(16, 14))
fig.patch.set_facecolor('#F8F9FA')          # light grey background
gs = gridspec.GridSpec(3, 2, figure=fig,
                        hspace=0.45, wspace=0.35)

ax1 = fig.add_subplot(gs[0, 0])   # Salesperson bar
ax2 = fig.add_subplot(gs[0, 1])   # Monthly line
ax3 = fig.add_subplot(gs[1, 0])   # Heatmap
ax4 = fig.add_subplot(gs[1, 1])   # Box plot
ax5 = fig.add_subplot(gs[2, :])   # Full-width stacked bar

# STEP 3: Plot each chart on its axis
# (You write the plotting code here using skills from Tasks 1–9)
# Chart 1 → ax1: Horizontal bar (salesperson sales)
# Chart 2 → ax2: Line with dual axis (monthly sales + order count)
# Chart 3 → ax3: Heatmap (region × product)
# Chart 4 → ax4: Box plot (amount by region)
# Chart 5 → ax5: Stacked bar (product by region)

# STEP 4: Add main title and metadata
fig.suptitle('📊 Sales Performance Report — 2024',
             fontsize=18, fontweight='bold', y=0.98)
fig.text(0.99, 0.01, f'Generated: {date.today()}',
         ha='right', fontsize=9, color='grey')

# STEP 5: Save
plt.savefig('sales_visual_report.png', dpi=150,
            bbox_inches='tight', facecolor=fig.get_facecolor())
print("Report saved as sales_visual_report.png ✅")
plt.show()
```

### Bonus Challenges
```python
# BONUS 1: Export to PDF (multi-page report)
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('sales_report.pdf') as pdf:
    # Page 1: Overview charts
    fig1 = create_overview_charts(df)
    pdf.savefig(fig1)

    # Page 2: Detailed breakdown
    fig2 = create_detail_charts(df)
    pdf.savefig(fig2)

print("PDF report saved ✅")

# BONUS 2: Add company logo to your chart
from matplotlib.image import imread
logo = imread('logo.png')
fig.figimage(logo, xo=10, yo=fig.bbox.ymax - 60, alpha=0.6)

# BONUS 3: Annotate insights automatically
# Find and highlight the top performing month
best_month = monthly_sales.idxmax()
best_val = monthly_sales.max()
ax2.annotate(f'Peak: ₹{best_val:,.0f}',
             xy=(best_month, best_val),
             xytext=(best_month+0.5, best_val*0.95),
             arrowprops=dict(arrowstyle='->', color='red'),
             color='red', fontsize=9)
```

---

## 🆚 Matplotlib vs Seaborn — Quick Reference

| Feature | Matplotlib | Seaborn |
|---|---|---|
| Control | Maximum (customize everything) | Limited (but easier) |
| Code length | More lines | Fewer lines |
| Default styling | Plain | Beautiful |
| Statistical plots | Manual | Built-in (regression, CI, KDE) |
| Heatmaps | Manual | sns.heatmap() |
| Best for | Final polish, layouts | Exploration, EDA |
| Learning curve | Steeper | Gentle |
| **BA usage** | Dashboards, reports | EDA, quick analysis |

> 💡 **Rule of thumb:** Use **Seaborn** to explore and understand data quickly.
> Use **Matplotlib** to finalize and polish charts for presentations.
> They work perfectly together — seaborn *is* built on matplotlib.

---

## 📚 Resources

| Resource | Link |
|---|---|
| Matplotlib Gallery | [https://matplotlib.org/stable/gallery](https://matplotlib.org/stable/gallery) |
| Seaborn Gallery | [https://seaborn.pydata.org/examples](https://seaborn.pydata.org/examples) |
| Python Graph Gallery | [https://python-graph-gallery.com](https://python-graph-gallery.com) |
| Choosing Chart Types | [https://www.data-to-viz.com](https://www.data-to-viz.com) |
| Color Palettes | [https://colorbrewer2.org](https://colorbrewer2.org) |

---

## 🎤 Common Interview Questions on Visualization

```
1. What is the difference between Matplotlib and Seaborn?
2. When would you use a bar chart vs a line chart?
3. What is a box plot and what does it tell you about data?
4. How do you add a secondary Y-axis in Matplotlib?
5. What does a heatmap show and when would you use one?
6. What is EDA (Exploratory Data Analysis)?
7. How do you save a matplotlib chart as a file?
8. Why is a violin plot better than a box plot sometimes?
9. What is the purpose of plt.tight_layout()?
10. How would you create multiple charts in one figure?
```

---

*Update your status column daily. Mark ✅ when done, 🔄 when in progress.*
