def main():
    # Input from user
    greeting = input("Greeting: ")

    # Adjust output to print value instead of memory address of function
    output = value(greeting)
    print(output)


def value(greeting):
    # Make it universally accepted input
    greeting = greeting.lower()

    # If greeting starts with hello, pay $0
    if greeting.startswith("hello"):
        # Add 0
        return 0
    # If greeting starts with h, pay $20
    elif greeting.startswith("h"):
        # Add 20
        return 20
    # If greeting starts with anything else, pay $100
    else:
        # Add 100
        return 100


if __name__ == "__main__":
    main()
