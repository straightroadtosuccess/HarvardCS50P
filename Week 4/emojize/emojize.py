import emoji


def main():
    # Get input from the awesome user!
    code = input("Input: ")

    # Convert it to an emoji and print the
    emote = emoji.emojize(code, language="alias")

    # Print the result!
    print(emote)


if __name__ == "__main__":
    main()
