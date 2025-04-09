def main():
    # Get input from the awesome user!
    time = input("What time is it? ")

    # Call the convert(time function)
    result = convert(time)

    # Print the result! Mainly for testing, may disable
    # print(result)

    # If time is between 7:00 and 8:00, it's breakfast time!
    if 7.0 <= result <= 8.0:
        # Print the finale!
        print("breakfast time ")
    # If time is between 12:00 and 13:00, it's lunch time!
    elif 12.0 <= result <= 13.0:
        # Print the finale!
        print("lunch time ")
    # If time is between 18:00 and 19:00, it's dinner time!
    elif 18.0 <= result <= 19.0:
        # Print the finale!
        print("dinner time ")
    # If the time is outside of these time windows
    else:
        # Print a message showing no output
        print("")


def convert(time):
    # Count time as 2 parameters, hours and minutes and split to replace the colon with a space, creating the space for 2 parameters
    hours, minutes = time.split(":")

    # Convert hours and minutes into numbers and convert minutes to decimal and return to the main function for use
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()
