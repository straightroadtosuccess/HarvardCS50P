import re


def main():
    # Get input from the user, print the result
    print(convert(input("Hours: ")))


def convert(s):
    # Match address format
    match = re.match(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s)

    # Error for invalid input format
    if not match:
        raise ValueError

    # Groups defined
    h1, m1, p1, h2, m2, p2 = match.groups()

    # Hours defined as integers
    h1, h2 = int(h1), int(h2)

    # Minutes defined as integers, if no minutes typed default to zero minutes
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    # If the numbers are outside of the valid range, raise error
    if not valid_time(h1, m1) or not valid_time(h2, m2):
        raise ValueError

    # Return the time to be converted
    return f"{to_24(h1, m1, p1)} to {to_24(h2, m2, p2)}"


def to_24(h, m, p):
    # If hours is 12 AM below, do nothing
    if p == "AM" and h == 12:
        h = 0
    # Else if hours are above 12 PM, add 12
    elif p == "PM" and h != 12:
        h += 12
    # Add the :00s
    return f"{h:02}:{m:02}"


def valid_time(h, m):
    # Ensure time in proper range, not 13 AM or 5:60 PM or other invalid times
    return 1 <= h <= 12 and 0 <= m < 60


if __name__ == "__main__":
    main()
