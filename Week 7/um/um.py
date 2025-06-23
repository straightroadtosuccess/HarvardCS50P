import re
import sys


def main():
    # Get input from user, also print the result returned by function
    print(count(input("Text: ")))


def count(s):
    # Force lowercase for input
    s = s.lower()

    # Find all words in input
    words = re.findall(r"\w+", s)

    # Count and return amount of ums
    return words.count("um")


if __name__ == "__main__":
    main()
