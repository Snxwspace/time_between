import datetime
import main

def change_datetime(cur_datetime: datetime.datetime) -> datetime.datetime:
    # Choose between datetime of calculation, a specified datetime, or cancellation
    string = "\nChoose one of the following options for choosing the new date and time.\n"
    string += "Current date and time: "
    if isinstance(cur_datetime, datetime.datetime):
        string += cur_datetime.strftime("%b %d %Y, %I:%M:%S %p")
    else:
        string += cur_datetime
    string += "\n\n"
    string += "1. Choose a date and time\n"
    string += "2. The current time\n"
    string += "3. Cancel\n"
    print(string)
    choice = input("> ")

    try:
        if int(choice) == 3:
            return cur_datetime
        elif int(choice) == 2:
            return "now"
        elif int(choice) == 1:
            new = choose_new_datetime()
            if new != None:
                return new
    except ValueError:
        print("Please input an integer from the list.")

def choose_new_datetime() -> datetime.datetime:
    # Make sure a proper year is selected
    while True:
        while True:
            string = "What year is this in?\n"
            string += "Must be an integer between 0 and 9999 inclusive.\n"
            string += "You can type 'cancel' to cancel the "

            print(string)
            choice = input("> ")

            try:
                if int(choice) <= 9999 and int(choice) >= 0:
                    string = "The chosen year is " + choice + ".\n"
                    string += "Is this what you want? y/n\n"
                    confirm = main.ask_yes_or_no(string)
                    if confirm:
                        year = choice
                        break
                else:
                    print("It has to be between 0 and 9999.\n")
            except ValueError:
                print("Select an integer.\n")

    # Give a 1-12 list of months that can be selected
        while True:
            string = "What month of the year is this?\n"
            string += "Choose "



    
    # Make sure a valid day is selected
        # MAKE SURE TO DO LEAP DAY HANDLING
        # Leap days are when the year is evenly divisible by 4 and not by 100, or when evenly divisible by 400
    

    # Make sure a valid hour, minute, and second is selected in 24-hour format
        # Allow floats for the seconds category, truncate it to 6 digits for microseconds

if __name__ == '__main__':
    change_datetime(datetime.datetime(2024, 4, 16))