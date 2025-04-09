# Get input from awesome user!
name = input("What's the name: ")

# Initialize variable to save converted name
converted_name = ""

# Loop through each character
for c in name:
    # Look for uppercase
    if c in name.isupper():
        # Replace with underscore and add a lowercase version of itself after
        converted_name += "_" + c.lower()
    else:
        # If it is not uppcase, keep it unchanged
        converted_name += c

# Print the result!
print(converted_name)
