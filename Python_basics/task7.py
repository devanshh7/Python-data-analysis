#7 Task 7 — File Handling (CSV)


'''1. Create a CSV file "sales_report.csv" with this data:
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

5. Write a new filtered CSV with only rows where Achievement > 100%'''

#----------------------------------------------------

import csv

# Task 1 & 2: Create file and calculate Achievement% while writing
data = [
    ["Month", "Region", "Sales", "Target", "Achievement%"],
    ["January", "North", 450000, 500000],
    ["February", "South", 620000, 600000],
    ["March", "East", 380000, 400000],
    ["April", "West", 710000, 700000]
]

with open('C:\\Users\\DEVANSH\\OneDrive\\Desktop\\Python-Data-Analysis\\Python_basics\\sales_report.csv', mode='w', newline='') as file:
   writer= csv.writer(file)
   writer.writerow(data[0])  # Write header
   for row in data[1:]:
      # Task 2: (Sales/Target) * 100
       achievement = (row[2] / row[3]) * 100  # Calculate Achievement%
       writer.writerow(row + [achievement])  # Write row with Achievement%

# Task 3: Read and Analyze
print("---Analysis---")
missed_targets = []
best_sales=0
total_sales = 0
total_target=0
best_region=""

with open('C:\\Users\\DEVANSH\\OneDrive\\Desktop\\Python-Data-Analysis\\Python_basics\\sales_report.csv', mode='r') as file:
   reader = csv.DictReader(file)
   for row in reader:
       sales = int(row["Sales"])
       target = int(row["Target"])
       achievement = float(row["Achievement%"])
       
       
       if achievement < 100:
           missed_targets.append(row["Month"])
       
       if sales > best_sales:
           best_sales = sales
           best_region = row["Region"]
       total_sales += sales
       total_target += target

print("Months where target was missed:", missed_targets)
print("Best performing region:", best_region)  
print("Overall Achievement%:", (total_sales/total_target)*100)

# Task 4: Append May Data
new_row = ["May", "West", 550000, 600000]
achievement = (new_row[2] / new_row[3]) * 100
new_row.append(achievement)

with open('C:\\Users\\DEVANSH\\OneDrive\\Desktop\\Python-Data-Analysis\\Python_basics\\sales_report.csv', mode='a', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(new_row)
   
# Task 5: Write filtered CSV

with open('C:\\Users\\DEVANSH\\OneDrive\\Desktop\\Python-Data-Analysis\\Python_basics\\sales_report.csv', mode='r') as file:
   reader = csv.DictReader(file)
   filtered_data = [row for row in reader if float(row["Achievement%"]) > 100]

with open('C:\\Users\\DEVANSH\\OneDrive\\Desktop\\Python-Data-Analysis\\Python_basics\\filtered_sales_report.csv', mode='w', newline='') as file:
   writer = csv.DictWriter(file, fieldnames=filtered_data[0].keys())
   writer.writeheader()
   writer.writerows(filtered_data)