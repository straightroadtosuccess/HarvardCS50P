from datetime import datetime, date
import sys
import inflect


# Custom object, birthday
class Birthday:
    def __init__(self, birth_input):
        try:
            # If not correct YYYY-MM-DD format
            self.birthday = datetime.strptime(birth_input, "%Y-%m-%d").date()
        except ValueError:
            # Sys exit with an error
            sys.exit("Invalid date")

    # Calculate number of minutes
    def minutes_old(self):
        # Get today's date for current day in reality, define as "today"
        today = date.today()
        # Calculate the number of days between "today" and user input "my_birthday"
        days_old = (today - self.birthday).days
        # 24 hours in a day multiplied by 60 minutes to convert days to minutes
        return days_old * 24 * 60

    # Convert number of minutes to english words
    def words_for_minutes(self):
        # Create inflect engine instance to convert minutes to words
        p = inflect.engine()
        # Get number of "minutes_old"
        minutes = self.minutes_old()
        # Convert number to words and remove " and " from them
        words = p.number_to_words(minutes, andword="")
        # Capitalize first letter
        return words.capitalize()

    # Print the result!
    def show_age_in_minutes(self):
        # Add minutes to the end for minutes message
        print(f"{self.words_for_minutes()} minutes")


# Get input from user
def main():
    user_input = input("Date of Birth: ")
    # Make a new my_birthday object instance
    my_birthday = Birthday(user_input)
    # Call method to print the result of my_birthday's age
    my_birthday.show_age_in_minutes()


if __name__ == "__main__":
    main()
