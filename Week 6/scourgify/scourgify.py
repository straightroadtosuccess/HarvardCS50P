import sys
import csv
import os


def main():
    # Not enough args
    if len(sys.argv) < 3:
        print("Too few command-line arguments ")
        sys.exit(1)
    # Too many args
    elif len(sys.argv) > 3:
        print("Too many command-line arguments ")
        sys.exit(1)

    # Define a variable for filename
    filename = sys.argv[1]

    # File handling
    if not filename.endswith(".csv"):
        print("Not a CSV file ")
        sys.exit(1)

    # If file is empty
    if os.stat(filename).st_size == 0:
        print("Could not read 1.csv")
        sys.exit(1)

    try:
        # Initialize an empty list to store students
        students = []

        # Open the file
        with open(filename) as file:
            # Assign csv Dict Reader as variable for use
            reader = csv.DictReader(file)
            # For each row
            for row in reader:
                # Strip puncuation off of dict keys
                last, first = row["name"].split(", ")
                # Append the name and house of students
                students.append({"first": first, "last": last, "house": row["house"]})

        # Assign a variable for new file
        new_file = sys.argv[2]

        # Write or overwrite a new file
        with open(new_file, "w") as file:
            # Assign a variable to Dict Writer for use
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            # Write the CSV header
            writer.writeheader()
            # For each student stored in list of students
            for student in students:
                # Write student in each row
                writer.writerow(student)

    # File not found error handling
    except FileNotFoundError:
        print("File does not exist ")
        sys.exit(1)


if __name__ == "__main__":
    main()
