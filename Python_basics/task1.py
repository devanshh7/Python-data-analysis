# Task 1 — Variables & Data Types  

#Question:
'''
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
'''
# assigning values to variables

Company_name= "RetailCorp"
Total_Sales= 1500000
Sales_Growth= 12.5
Target_Achieved= True
Region= None

#2 type of each variable
print("Company Name:", Company_name, "Data Type:", type(Company_name))
print("Total Sales:", Total_Sales, "Data Type:", type(Total_Sales))
print("Sales Growth:", Sales_Growth, "Data Type:", type(Sales_Growth))
print("Target Achieved:", Target_Achieved, "Data Type:", type(Target_Achieved))
print("Region:", Region, "Data Type:", type(Region))

print("-----------------------------------")
#3 calculating actual sales amount last month

actual_sales= Total_Sales *(1 + Sales_Growth/100)

print("Actual Sales Amount last month:", actual_sales)

print("-----------------------------------")

#4 formatting and printing summary line

print (f" {Company_name} achieved sales of ${Total_Sales:,} with {Sales_Growth}% growth. Target met: {Target_Achieved}")