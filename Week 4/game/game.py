import random


def main():
    # Get input from the awesome user!
    while True:
        try:
            # Input here
            n = int(input("Level: "))
            # must not be 0 or negative
            if n > 0:
                break
            # Handle ValueError
        except ValueError:
            pass
        # Ask for valid
        print("Try again by inputting number")

    # Generate random number
    number = random.randint(1, n)

    # Guessing loop
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            elif guess == number:
                print("Just right! ")
                # Exit loop when guess is correct
                break
        except ValueError:
            # Ask for valid
            print("Try again by inputting number")


if __name__ == "__main__":
    main()
