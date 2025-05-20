def main():
    # Input from user
    phrase = input("What's the input ")
    output = shorten(phrase)
    print(f"{output}")


def shorten(phrase):
    # Initialize to a converted phrase
    output = ""

    # Define both lowercase and uppercase vowels
    vowels = "aeiouAEIOU"

    # Check for each letter in phrase
    for l in phrase:
        # If letter isn't a vowel
        if l not in vowels:
            # Append to output
            output += l

    # Return the output
    return output


if __name__ == "__main__":
    main()
