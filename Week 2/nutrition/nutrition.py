# Get input from the awesome user!
fruit = input("What is it: ").strip().lower()

# Dict mapping fruits to calories from FDA nutrition information
food = {
    "apple": 130,
    "banana": 110,
    "pear": 100,
    "sweet cherries": 100,
    "grapes": 90,
    "kiwifruit": 90,
    "orange": 80,
    "watermelon": 80,
    "plums": 70,
    "grapefruit": 60,
    "nectarine": 60,
    "peach": 60,
    "avocado": 50,
    "cantaloupe": 50,
    "honeydew melon": 50,
    "pineapple": 50,
    "strawberries": 50,
    "tangerine": 50,
    "lime": 20,
    "lemon": 15
}

# Check if the fruit is in the dict and print it's calories
if fruit in food:
    print("Calories:", food[fruit])
