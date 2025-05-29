import sys
from PIL import Image, ImageOps


def main():
    # Not enough args
    if len(sys.argv) < 3:
        print("Too few command-line arguments ")
        sys.exit(1)
    # Too many args
    elif len(sys.argv) > 3:
        print("Too many command-line arguments ")
        sys.exit(1)

    # Assign a variable for filename
    filename = sys.argv[1]

    # Assign a variable for new file
    new_file = sys.argv[2]

    # Assing a variable for input extension
    input = filename.split(".")[-1].lower()
    
    # Assing a variable for output extension
    output = new_file.split(".")[-1].lower()

    # File handling, only accept certain extensions
    if not filename.endswith((".jpeg", ".jpg"," .png")):
        print("Invalid input ")
        sys.exit(1)

    # Error for different extensions
    if input != output:
        print("Input and output have different extensions ")
        sys.exit(1)

    try:
        # Open the picture file
        with Image.open(filename) as file:
            # Open shirt picture
            with Image.open("shirt.png") as shirt:
                # Fit before picture to shirt size
                file = ImageOps.fit(file, shirt.size)

                # Fit shirt on top of picture
                file.paste(shirt, (0, 0), shirt)

                # Save the result
                file.save(new_file)

    # File not found error handling
    except FileNotFoundError:
        print("Input does not exist ")
        sys.exit(1)


if __name__ == "__main__":
    main()
