def main():
    while True:
        try:
            # Get user input
            fraction = input("Fraction: ")
            # Convert from function address to value
            percentage = convert(fraction)
            # Print the result!
            print(gauge(percentage))
            # End the loop
            break

        # Handle errors gracefully and silently
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    # Convert into usuable numbers for math operations
    x, y = fraction.split("/")
    x, y = int(x), int(y)

    # Raise these errors for edge cases
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    # Return 1st value we are working with
    return round((x / y) * 100)


def gauge(percentage):
    # Handle the E at 0-1
    if percentage <= 1:
        return "E"
    # Handle F at 99-100
    elif percentage >= 99:
        return "F"
    else:
        # Return the 2nd value we are working with, if not for the strings
        return f"{percentage}%"


if __name__ == "__main__":
    main()
