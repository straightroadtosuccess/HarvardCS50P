from tabulate import tabulate
import sys
import csv


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
    if not filename.endswith(".csv"):
        print("Not a CSV file ")
        sys.exit(1)

    try:
        # Open the file
        with open(filename, "r") as file:
            # Assign csv reader a variable for tabulate to understand
            reader = csv.reader(file)
            # Print the result in tabulate grid with variable headers
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))

    # File not found error handling
    except FileNotFoundError:
        print("File does not exist ")
        sys.exit(1)


if __name__ == "__main__":
    main()
