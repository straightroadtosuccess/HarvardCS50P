# Get input from the awesome user!
x, y, z = input("Expression like 1 + 1: ").split(" ")

# Convert x and z to floats
x = float(x)
z = float(z)

# Convert operator functions
if y == "+":
    # Compute in the for of an equation
    answer = x + z
# Convert operator functions
elif y == "-":
    answer = x - z
# Convert operator functions
elif y == "*":
    answer = x * z
# Convert operator functions
elif y == "/":
    answer = x / z
# Message for anything else in place of y
else:
    answer = "Invalid operator"

# Print the finale!
print("Equals: ", answer)
