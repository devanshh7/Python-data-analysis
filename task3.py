# 3  Lists & Loops
'''
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
'''
# all products with sales above ₹50,000

sales_data = [
    ["Product A", 45000], ["Product B", 72000], ["Product C", 31000],
    ["Product D", 89000], ["Product E", 15000], ["Product F", 62000],
    ["Product G", 55000], ["Product H", 23000]
]
a=[]
for i in sales_data:
    if i[1]>50000:
        a.append(i[0])
print("Products above 50k :" , ", ".join(a))

print("-----------------------------------")
#2 total sales across all products
total_sales= sum(i[1] for i in sales_data)
print("Total sales across all products:", total_sales)

print("-----------------------------------")

#3 product with the highest and lowest sales
highest=max(sales_data, key=lambda x: x[1])
lowest=min(sales_data, key=lambda x: x[1])
print("Highest:", highest[0], "(", highest[1], ")", "|", "Lowest:", lowest[0], "(", lowest[1], ")")

print("-----------------------------------")
#4 average sales

average_sales= total_sales/len(sales_data)
print("Average sales:", average_sales)

print("-----------------------------------")
#5 classify each product as "High" (>60k), "Medium" (30k-60k), or "Low" (<30k)



"""for i in sales_data:
    if i[1]>60000:
        print(i[0],"- High")
    elif i[1]>=30000:
        print(i[0],"- Medium")
    else:
        print(i[0],"- Low")"""
result = []

for i in sales_data:
    if i[1] > 60000:
        result.append(f"{i[0]} - High")
    elif i[1] >= 30000:
        result.append(f"{i[0]} - Medium")
    else:
        result.append(f"{i[0]} - Low")

print(" | ".join(result))
        
# To make the output looks like Product A → Medium | Product B → High .....

# We can make a empty list and append the to it and then print the list and then we can use join to print the list in the desired format
print("-----------------------------------")

#6 create a new list with only products that are above average

a=[]
for i in sales_data:
    if i[1]>average_sales:
        a.append([i[0], i[1]])
print("Above Average Products:", a)

print("-----------------------------------")

#7 sort products by sales in descending order

"""sorted_sales= sales_data.sort(key=lambda x: x[1], reverse=True)"""

# list.sort() method sorts the list in place and returns None, so we should use sorted() function instead to get a new sorted list

sorted_sales= sorted(sales_data, key=lambda x: x[1], reverse=True)
print ("sorted :",sorted_sales)