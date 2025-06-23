import validators

# Get input from user
email = input("What's you email address? ")

# Check format of input to valid email format
if validators.email(email):
    # Print the valid result
    print("Valid ")
else:
    # Print the invalid result
    print("Invalid ")
