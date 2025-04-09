# Get input from the awesome user! Convert to lowercase and strip spaces
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().lstrip(' ').rstrip(' ')

# If the answers range from these do this
if answer == "42" or answer == "forty two" or answer == "forty-two":
    # Print the finale!
    print("Yes")
else:
    # Print the finale!
    print("No")
