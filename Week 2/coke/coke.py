# Determine price of a coke
amount_due = 50
# Use list to store valid coins for input
valid_coins = [25, 10, 5]

# while loop for greater than 0
while amount_due > 0:
    # print amount that is due
    print("Amount Due:", amount_due)
    # Get input from awesome user!
    coin = int(input("Insert Coin: "))
    # Check if coin is valid from array
    if coin in valid_coins:
        # Subtract the value of the coin from amount_due
        amount_due -= coin

# Print the change owed, goal is balance of 0
print("Change Owed:", abs(amount_due))
