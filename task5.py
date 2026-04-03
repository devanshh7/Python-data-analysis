# Task 5 — Lists and Tuples

'''Build the following functions:

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

Test each function with at least 3 different inputs.'''
# growth percentage
# formula= growth= ((new_val-old_val)/0ld_value )* 100


#print("-------------------------------------")
def growth_perct(current, previous):
   if (previous == 0):
      #print ("Cannot determine % growth as prev year is 0")
      return None
   growth= ((current-previous)/previous )* 100
   print("Growth Percentage(%)", growth)
   
   

#a = int(input("Enter this year growth : "))
#b = int(input("Enter previous year growth : "))
#result =growth_perct(a,b)
'''
if result is None:
    print("Growth percentage cannot be calculated (previous value is 0).")
else:
    print("Growth Percentage (%):", result)
   ''' 
   
#print ("-------------------------------")
#2. classify_customer(purchase_amount)
'''   → "Platinum" if > 100000
   → "Gold" if > 50000
   → "Silver" if > 20000
   → "Bronze" otherwise
'''
def classify_cust(pur_amount):
   if pur_amount > 100000:
      return "Platinum"
   if pur_amount > 50000:
      return "Gold"
   if pur_amount > 20000:
      return "Silver"
   else:
      return "Bronze"

#x= int(input("Enter the purchase amount : "))

#print(classify_cust(a))

#print ("-------------------------------")

#3. format_indian_currency(amount)
#  → Returns ₹1,50,000 format (Indian number system)

def format_indian_currency(amount):
   amt= str(amount)
   if len(amt) <=3:
      return "Rs" + amt
   last3= amt[-3:]
   rem=amt[:-3]
   
   parts= []
   while len(rem)>2:
      parts.insert(0, rem[-2:])
      rem= rem[:-2]
      
   if rem:
      parts.insert(0,rem)
   return "Rs "+ ",".join(parts)+ "," + last3

#p= int(input("Enter the amount : "))

#print(format_indian_currency(p))


#print ("-------------------------------")

def get_quarter(month_number):
    if 1 <= month_number <= 3:
        return "Q1"
    elif 4 <= month_number <= 6:
        return "Q2"
    elif 7 <= month_number <= 9:
        return "Q3"
    elif 10 <= month_number <= 12:
        return "Q4"
    else:
        return "Invalid month"

#r= int(input("Enter the month number : "))
#print(get_quarter(r))

#print ("-------------------------------")

def calculate_kpi(target, achieved):
    if target == 0:
        return None, "Invalid target"
    
    percent = (achieved / target) * 100
    
    if percent >= 100:
        status = "Met"
    elif percent >= 90:
        status = "Near Miss"
    else:
        status = "Missed"
    
    return f"{percent} % , {status}"

#tr= int(input("Enter the Target number  : "))
#rr= int(input("Enter the number achieved : "))

#print(calculate_kpi(tr,rr))

#print("----------------------------")
def run_function(choice):
   
   if choice == 1:
      p= int(input("Enter the amount : "))

      print(format_indian_currency(p))
    
   elif choice == 2:
       
      r= int(input("Enter the month number : "))
      print(get_quarter(r))
    
   elif choice == 3:
      tr= int(input("Enter the Target number  : "))
      rr= int(input("Enter the number achieved : "))

      print(calculate_kpi(tr,rr))
   
   elif choice == 4:
      a = int(input("Enter this year growth : "))
      b = int(input("Enter previous year growth : "))
      result =growth_perct(a,b)

      if result is None:
         print("Growth percentage cannot be calculated (previous value is 0).")
      else:
         print("Growth Percentage (%):", result)
    
   elif choice == 5:
      x= int(input("Enter the purchase amount : "))
      print(classify_cust(a))
   else:
      print("Invalid choice")

print("WHICH FUNCTION DO YOU WANT TO RUN??")
print("1. Format Currency")
print("2. Get Quarter")
print("3. Calculate KPI")
print("4. Growth Percentage(%)")
print("5. Classify Customer")

choice = int(input("Enter your choice: "))
run_function(choice)

