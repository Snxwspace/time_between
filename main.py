import calculation
from datetime import datetime

def main(first_datetime_override: datetime = None, second_datetime_override: datetime = None, precision_override: str = None) -> None:
    """
    The main function for calculating time between two arbitrary dates.
    
    The override inputs override the initial settings for each of their categories.
    If you know how to use Python, you can set it up to calculate it without the need for the prompts.

    Returns nothing, but prints the result of the calculation once you confirm it.
    """
    # Setting things up
    first_datetime = first_datetime_override
    second_datetime = second_datetime_override
    precision = precision_override
    pre_run()

    # Main loop 
    while True:
        print_options(first_datetime, second_datetime, precision)
        choice = input("> ")
        try:
            if int(choice) == 5:
                break
            elif int(choice) == 4:
                # Proofchecking all inputs
                if first_datetime == None:
                    print("You need to set the starting datetime.")
                    continue
                if second_datetime == None:
                    print("You need to set the ending datetime.")
                    continue
                if precision == None:
                    print("You need to set the precision.")
                    continue
                if first_datetime == second_datetime:
                    print("The starting and ending datetimes must be different.")
                    continue
                
                # Make sure all of the "now"s are properly handled
                if first_datetime == "now":
                    first_datetime = datetime.now()
                elif second_datetime == "now":
                    second_datetime = datetime.now()
                
                calculation.calculate_time_between(first_datetime, second_datetime, precision)

                # Ask if they want to continue
                cont = ask_yes_or_no("Would you like to calculate another date? y/n")

                if cont:
                    first_datetime = None
                    second_datetime = None
                    precision = None
                    continue
                else:
                    break
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
    """Prints the options for controlling the first prompt of the program."""
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
    """Controls changing the precision, taking in the old precision and returning a new one."""
    while True:
        string = "\nHow precise do you want the result to be?\n"
        string += "Note that the more precise you choose, the more space the output takes up.\n"
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
            string = "Would you like to change the precision to "
            if int(choice) == 1:
                new_precision = "years"
                string += f"\'{new_precision}\'? y/n\n"
                if ask_yes_or_no(string):
                    return new_precision
            elif int(choice) == 2:
                new_precision = "months"
                string += f"\'{new_precision}\'? y/n\n"
                if ask_yes_or_no(string):
                    return new_precision
            elif int(choice) == 3:
                print("I'm sorry, we don't quite support a weeks-based precision. Maybe soon!")
                print("Choose again.\n")
            elif int(choice) == 4:
                new_precision = "days"
                string += f"\'{new_precision}\'? y/n\n"
                if ask_yes_or_no(string):
                    return new_precision
            elif int(choice) == 5:
                new_precision = "hours"
                string += f"\'{new_precision}\'? y/n\n"
                if ask_yes_or_no(string):
                    return new_precision
            elif int(choice) == 6:
                new_precision = "minutes"
                string += f"\'{new_precision}\'? y/n\n"
                if ask_yes_or_no(string):
                    return new_precision
            elif int(choice) == 7:
                new_precision = "seconds"
                string += f"\'{new_precision}\'? y/n\n"
                if ask_yes_or_no(string):
                    return new_precision
            elif int(choice) == 8:
                new_precision = old_precision
                string = "Would you like to cancel this operation? y/n\n"
                if ask_yes_or_no(string):
                    return new_precision
            else:
                print("Invalid input: pick one of the list items.")
        except ValueError:
            print("Invalid input: type a whole number.")


def ask_yes_or_no(question: str) -> bool:
    """Asks a yes or no *question*, and returns a True/False boolean with the choice."""
    while True:
        print(question)
        choice = input("> ")
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("Answer with a \'y\' or an \'n\'.\n\n")


if __name__ == '__main__':
    main()
    # change_precision(None)
    # print(round(2763.123456789, 6))
    pass