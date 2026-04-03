# Task 4 — Dictionaries

'''employees = [
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
6. Find total salary cost per department'''

print("=====COde STARTED!!!=====")

employees = [
    {"id": "E001", "name": "Ravi Kumar", "dept": "Sales", "salary": 45000, "years": 3},
    {"id": "E002", "name": "Sneha Patel", "dept": "IT", "salary": 72000, "years": 5},
    {"id": "E003", "name": "Arjun Mehta", "dept": "Sales", "salary": 38000, "years": 2},
    {"id": "E004", "name": "Divya Nair", "dept": "HR", "salary": 52000, "years": 4},
    {"id": "E005", "name": "Karan Singh", "dept": "IT", "salary": 68000, "years": 6},
]
#print(employees)
#1 1. Print all employees in the IT department

for i in employees:
    #print(i["salary"])
    if i["dept"]=="Sales":
        print(i["name"],",",i["dept"])
        
print("--------------------------------------")

#2. Calculate average salary department-wise
dep_sal={}
dep_count={}

for e in employees:
    dep= e["dept"]
    sal= e["salary"]
    
    if dep in dep_sal:
        dep_sal[dep] += sal
        dep_count[dep]+=1
    else:
        dep_sal[dep]= sal
        dep_count[dep]=1
        


# avg sales
for dep in dep_sal:
    avg= dep_sal[dep]/dep_count[dep]
    print(f"Average sales of {dep} is: {avg}")
    
#print(dep_sal, dep_count)

print("----------------------------------------")

# 3. Find all employees with more than 4 years of experience
for e in employees:
    if e["years"] > 4:
        print(f"Employee with >4 yrs exp are : {e["name"]}")

print("----------------------------------------")

# 4. Give a 10% salary hike to employees in Sales — update the dictionary

for e in employees:
    #employees[e]["salary"]=employees[e]["salary"]*0.10
    e["salary"]+=e["salary"]*0.10
print(employees)


print("----------------------------------------")
# 5. Add a new key "appraisal" to each employee:
'''   - "Excellent" if years >= 5
   - "Good" if years >= 3
   - "Average" otherwise
'''

for e in employees:
    if e["years"] >=5:
        e["appraisal"] ="Excellent" 
    elif e["years"] >=3 and e["years"]<5:
        e["appraisal"] ="Good"
    else:
        e["appraisal"] ="Average"
print(employees)

print("----------------------------------------")

#6 Find total salary cost per department
for dep in dep_sal: 
    print(dep,":" ,dep_sal[dep])