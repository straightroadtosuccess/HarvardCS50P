def main():
    # Dict with food items and prices
    food = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Total order cost
    total = 0

    while True:
        try:
            # Take the order of the awesome user!
            item = input("Item: ").title()

            # Check if item is in menu, if not, reprompt
            if item not in food:
                continue

            # Add item price to total
            total += food[item]

            # Print the total
            print(f"Total: ${total:.2f}")

        # Catch a KeyError
        except KeyError:
            pass

        # Complete order with CTRL+D
        except EOFError:
            # End the loop
            break

main()
