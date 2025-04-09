import random


def main():
    level = get_level()

    # List to store score
    score = 0

    # 10 questions
    for i in range(10):
        # Integers bases on difficulty level, calculate answer to determine correct answer
        x, y = generate_integer(level), generate_integer(level)
        answer = x + y

        # List to store attempts
        attempts = 0

        # Ask 3 times loop
        while attempts < 3:
            try:
                # Input for answer, store to score value, correct answer break out of loop, move to next question
                if int(input(f"{x} + {y} = ")) == answer:
                    score += 1
                    break
            # Handle errors such as non int
            except ValueError:
                pass
            # Print EEE for incorrect answer, store the attempt value
            print("EEE")
            attempts += 1

        # After 3 attempts, show the answer
        if attempts == 3:
            print(f"{x} + {y} = {answer}")

    # Print score
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            # Input for difficulty
            level = int(input("Level: "))
            # Send difficulty
            if level in (1, 2, 3):
                return level
            # Don't accept other than 1, 2, 3, handle error gracefully
        except ValueError:
            pass


def generate_integer(level):
    # Level ranges for difficulty
    ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
    return random.randint(*ranges[level])


if __name__ == "__main__":
    main()
