# Get input from the awesome user!
phrase = input("What's the input: ")

# Initialize a converted phrase
converted_phrase = ""
# Define both lowercase and uppercase vowels
vowel = "aeiouAEIOU"

# Check each character in phrase
for c in phrase:
    # If there is a vowel
    if c in vowel:
        # Convert vowel to blank
        converted_phrase += ""
    else:
        # Otherwise don't change anything but continue to append
        converted_phrase += c

# Print the output!
print(converted_phrase)
