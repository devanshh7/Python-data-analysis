#8 Task 8 — Error Handling


'''
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
Use try/except/finally blocks properly.'''

