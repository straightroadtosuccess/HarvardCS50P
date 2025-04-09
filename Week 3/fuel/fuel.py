def main():
    while True:
        try:
            # Ask the awesome user!
            fraction = input("Fraction: ")

            # Convert into usuable numbers for math operations
            x, y = fraction.split("/")
            x, y = int(x), int(y)

            # Raise these errors for edge cases
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            # Convert from decimal to whole number for percentage
            percentage = (x / y) * 100

            # Handle the E and F and print the result
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")

            # Loop end
            break

        # Handle these errors gracefully
        except (ValueError, ZeroDivisionError):
            pass

# Run the program
main()
