def main():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    while True:
        try:
            # Get input from awesome user!
            date = input("Date: ").strip()

            # Check if the input is in MM/DD/YYYY format
            if "/" in date:
                mm, dd, yyyy = date.split("/")
                # Make sure month, day, and year are numbers
                if mm.isdigit() and dd.isdigit() and yyyy.isdigit():
                    # Convert month and day to an integer
                    mm = int(mm)
                    dd = int(dd)
                    # Check if month is equal or less than 12 and day is less or equal to 31
                    if mm <= 12 and dd <= 31:
                        print(f"{yyyy}-{mm:02}-{dd:02}")
                        return

            # Check if Month DD, YYYY
            if "," in date:
                # Splits date into a list of words
                parts = date.split()
                # Ensures second part ends in ","
                if len(parts) == 3 and parts[1][-1] == ",":
                    # First word is the month name
                    month_name = parts[0]
                    # Removes "," from the day
                    day = parts[1][:-1]
                    # Third part is the year
                    yyyy = parts[2]

                    if month_name in months and day.isdigit() and yyyy.isdigit():
                        # Find month number (1-based)
                        month = months.index(month_name) + 1
                        # Convert day to an integer
                        day = int(day)
                        # Check if day is equal or less than 31
                        if day <= 31:
                            print(f"{yyyy}-{month:02}-{int(day):02}")
                            return

            # Reject input with error message
            else:
                print("Date format is invalid. Please use month/day/year")

        # Handle ValueError gracefully
        except ValueError:
            pass


# Call the function
main()
