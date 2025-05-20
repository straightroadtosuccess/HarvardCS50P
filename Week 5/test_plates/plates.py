import sys


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
        sys.exit(0)
    else:
        print("Invalid")
        sys.exit(1)


def is_valid(s):
    # Check length is between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check that first 2 characters are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Must be alphanumeric no symbols
    if not s.isalnum()
        return False

    # Numbers only allowed at the end, number not encountered yet
    has_number = False
    for i in range(len(s)):
        if s[i].isdigit():
            # First number cannot be "0"
            if s[i] == '0' and not has_number:
                return False
            # First number found
            has_number = True
        # A letter cannot come after
        elif has_number:
            return False

    # All passed as True
    return True


if __name__ == "__main__":
    main()
