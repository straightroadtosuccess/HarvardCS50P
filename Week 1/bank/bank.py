# Get input from the wonderful user!
greeting = input("Greeting: ")

# If greeting starts with Hello, pay $0
if greeting.startswith("Hello"):
    # print the finale!
    print("$0")
# If greeting starts with H, pay $20
elif greeting.startswith("H"):
    # print the finale!
    print("$20")
# If greeting starts with anything else, pay $100
else:
    # print the finale!
    print("$100")
