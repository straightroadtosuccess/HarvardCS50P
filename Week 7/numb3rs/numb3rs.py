import re


def main():
    # Get input from User
    ip = input("IPv4 Address: ")
    # Print the result
    if validate(ip):
        print("True ")
    else:
        print("False ")
        # Exit with code
        sys.exit(1)


def validate(ip):
    # Regex address format for IP Address, times 3 dot decimals
    address = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"

    # Match the full address to the input
    if re.fullmatch(address, ip):
        # Return boolean values, True or False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
