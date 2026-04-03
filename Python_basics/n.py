# Get starting and ending numbers from the user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

# Loop through the range and create files
for i in range(start, end + 1):
    filename = f"task{i}.py"  # file name with .txt extension
    with open(filename, "w") as f:
        f.write(f"This is {filename}\n")  # optional content
    print(f"Created file: {filename}")

print("All files created successfully!")