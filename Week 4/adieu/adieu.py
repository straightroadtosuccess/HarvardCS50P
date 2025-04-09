import inflect

# Initialise inflect
n = inflect.engine()

# Initialize empty list to store names
names = []

# Get input from user until EOF (CTRL+D)
try:
    while True:
        name = input("Name: ")
        # store name in list
        names.append(name)
# Handle EOF
except EOFError:
    pass

# Use inflect for the farewell message and auto add and
goodbye = n.join(names)

print("Adieu, adieu, to", goodbye)
