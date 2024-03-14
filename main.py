import calculation
from datetime import datetime

def main() -> None:
    # Setting things up
    first_datetime = None
    second_datetime = None
    precision = None
    pre_run()

    # Main loop 
    while True:
        print_options(first_datetime, second_datetime, precision)
        choice = input("> ")
        try:
            # ERROR: ValueError: "invalid literal for int() with base 10" 
            # Happens with any float I type
            if int(choice) == 5:
                pass
            elif int(choice) == 4:
                # Run all inputs by a function to check for valid inputs
                # Calculate everything
                # Print the results
                # Ask if they want to calculate another thing
                pass    
            elif int(choice) == 3:
                precision = change_precision(precision)
            elif int(choice) == 2:
                second_datetime = calculation.change_datetime(second_datetime)
            elif int(choice) == 1:
                first_datetime = calculation.change_datetime(first_datetime)
            else:
                print("Invalid input: pick one of the list items.")
        except ValueError:
            print("Invalid input: type a whole number.")
    
    print("Thank you for using this program!")


def pre_run() -> None:
    """A disclaimer before starting the program."""
    print("The output can get long, so I would suggest expanding the output terminal if you need to.\n")
    input("Press enter when you're ready to begin.")
    print()


def print_options(cur_first: datetime = None, cur_second: datetime = None, cur_precision: str = None) -> None:
    """Prints the options for controlling the program."""
    if isinstance(cur_first, datetime):
        format_first = cur_first.strftime("%b %d %Y, %I:%M:%S %p")
    else:
        format_first = cur_first
    
    if isinstance(cur_second, datetime):
        format_second = cur_second.strftime("%b %d %Y, %I:%M:%S %p")
    else:
        format_second = cur_second
    
    string = "\nWhat would you like to edit? Type the number of the list item you want to choose.\n"
    string += "Make sure to set everything before confirming.\n\n"
    string += f"1. Start Date ({format_first})\n"
    string += f"2. End Date ({format_second})\n"
    string += f"3. Precision ({cur_precision})\n"
    string += f"4. Confirm\n"
    string += f"5. Cancel\n"

    print(string)


def change_precision(old_precision: str) -> str:
    while True:
        string = "\nprecision.selector.dialogue\n"
        string += "Type the number of the option that you would like to select.\n\n"
        string += "1. Years\n"
        string += "2. Months\n"
        string += "3. Weeks\n"
        string += "4. Days\n"
        string += "5. Hours\n"
        string += "6. Minutes\n"
        string += "7. Seconds\n"
        string += "8. Cancel\n"
        print(string)

        choice = input("> ")

        try:
            if int(choice) == 1:
                return "years"
            elif int(choice) == 2:
                return "months"
            elif int(choice) == 3:
                return "weeks"
            elif int(choice) == 4:
                return "days"
            elif int(choice) == 5:
                return "hours"
            elif int(choice) == 6:
                return "minutes"
            elif int(choice) == 7:
                return "seconds"
            elif int(choice) == 8:
                return old_precision
            else:
                print("Invalid input: pick one of the list items.")
        except ValueError:
            print("Invalid input: type a whole number.")


if __name__ == '__main__':
    # print_options()
    main()
    pass