import sys


def main():
    # Not enough args
    if len(sys.argv) < 2:
        print("Too few command-line arguments ")
        sys.exit(1)
    # Too many args
    elif len(sys.argv) > 2:
        print("Too many command-line arguments ")
        sys.exit(1)

    # Define a variable for filename
    filename = sys.argv[1]

    # File handling
    if not filename.endswith(".py"):
        print("Not a python file ")
        sys.exit(1)

    try:
        # Open the file
        with open(filename, "r") as file:

            # Counter for lines of substance
            counter = 0

            # Remove whitespace from start and end
            for raw_line in file:
                stripped = raw_line.strip()

                # Skip air and comments
                if not stripped or stripped.startswith("#"):
                    continue

                # Add to the counter
                counter += 1

            # Print the amount of lines
            print(counter)

    # File not found error handling
    except FileNotFoundError:
        print("File does not exist ")
        sys.exit(1)


if __name__ == "__main__":
    main()
