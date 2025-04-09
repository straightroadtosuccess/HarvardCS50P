def main():
    # Dict to store items and amounts
    grocery_list = {}

    # Start the loop
    while True:
        try:
            # Get input from awesome user
            item = input().strip().lower()

            # Add item to dict or update count
            grocery_list[item] = grocery_list.get(item, 0) + 1

        except KeyError:
            pass  # Catch and ignore

        # Finish grocery list when Ctrl+D is pressed
        except EOFError:
            break  # End the loop

    # Sort dict items alphabetically
    for item in sorted(grocery_list.keys()):
        # Print the item count and name in uppercase
        print(f"{grocery_list[item]} {item.upper()}")


# Run the program
main()
