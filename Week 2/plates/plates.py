def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Check that first 2 characters are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Numbers only allowed at the end
    has_number = False  # Number not encountered yet
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0" and not has_number:  # First number cannot be "0"
                return False
            has_number = True  # First number found
        elif has_number:  # A letter cannot come after
            return False

    # No symbols
    if not s.isalnum():
        return False

    # All passed as True
    return True


main()
