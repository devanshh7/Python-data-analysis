# Task 2 — String Operations 
# Real-World Context: You get messy customer names and emails from a CRM export. Clean and standardize them.

'''
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
'''

names = ["  john DOE  ", "MARY smith", "alex KUMAR  ", " priya SINGH"]
emails = ["John.Doe@Company.COM", "MARY.smith@Gmail.com", "Alex.kumar@outlook.COM"]

## 1. Clean all names: remove spaces, convert to Title Case (e.g., "John Doe")

#clean= names.strip()
#print(clean)

clean_names= [name.strip().title() for name in names]
print(clean_names)

#2 Standardize all emails to lowercase
clean_emails = [email.lower() for email in emails]
print(clean_emails)

#3 Extract the domain from each email (e.g., "company.com")
domains= [email.split("@")[1] for email in clean_emails]
print(domains)

#4 Check if any name contains "kumar" (case-insensitive)

contains_kumar= any("kumar" in name.lower() for name in clean_names)
print("Any name contains 'kumar':", contains_kumar)

#5 Create a formatted ID for each customer: first 3 letters of first name + last 3 of last name

ids=[]
for name in clean_names:
    first, last= name.split()
    ids.append(first[:3].lower() + last[-3:].lower())
print(ids)

#6 Count how many customers are from Gmail

g_count= sum(1 for d in domains if d=="gmail.com")
print("Number of customers from Gmail:", g_count)