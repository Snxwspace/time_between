import datetime
import main

DAYS_PER_MONTH = {
    "January": 31,
    "Febuary": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

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

def choose_new_datetime() -> datetime.datetime: # Break this into year, month, day, and hour/minute/second/microsecond functions
    while True:
        # Make sure a proper year is selected
        while True:
            string = "What year is this in?\n"
            string += "Must be an integer between 0 and 9999 inclusive.\n"
            string += "You can('t) type 'cancel' to cancel the operation"

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
            string += "Choose a month by number.\n"
            string += "1. January\n"
            string += "2. Febuary\n"
            string += "3. March\n"
            string += "4. April\n"
            string += "5. May\n"
            string += "6. June\n"
            string += "7. July\n"
            string += "8. August\n"
            string += "9. September\n"
            string += "10. October\n"
            string += "11. November\n"
            string += "12. December\n"

            print(string)
            input("> ")

            try:
                string = "Would you like to set the month to "
                if int(choice) == 1:
                    month = "January"
                    string += f"\'{month}\'? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 2:
                    month = "Febuary"
                    string += f"\'{month}\'? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 3:
                    month = "March"
                    string += f"\'{month}\'? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 4:
                    month = "April"
                    string += f"\'{month}\'? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 5:
                    month = "May"
                    string += f"\'{month}\'? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 6:
                    month = "June"
                    string += f"\'{month}\'? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 7:
                    month = "July"
                    string += f"\'{month}\'? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 8:
                    month = "August"
                    string = "Would you like to cancel this operation? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 9:
                    month = "September"
                    string = "Would you like to cancel this operation? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 10:
                    month = "October"
                    string = "Would you like to cancel this operation? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 11:
                    month = "November"
                    string = "Would you like to cancel this operation? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                elif int(choice) == 12:
                    month = "December"
                    string = "Would you like to cancel this operation? y/n\n"
                    if main.ask_yes_or_no(string):
                        break
                else:
                    print("Invalid input: pick one of the list items.")
            except ValueError:
                print("Invalid input: type a whole number.")

        while True:
            # Make sure a valid day is selected
                # MAKE SURE TO DO LEAP DAY HANDLING
                # Leap days are when the year is evenly divisible by 4 and not by 100, or when evenly divisible by 400
            day_maximum = DAYS_PER_MONTH[month]
            
            # Leap day handling
            if day_maximum == 28 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
                day_maximum = 29
            
            # Actual part of the function
            string = "What day of the month is it?\n"
            string += f"The month is {month}, which has {day_maximum} days.\n\n"

            print(string)
            choice = input("> ")

            try:
                if int(choice) <= day_maximum and int(choice) > 0:
                    string = "The chosen day is " + choice + ".\n"
                    string += "Is this what you want? y/n\n"
                    confirm = main.ask_yes_or_no(string)
                    if confirm:
                        day = choice
                        break
                else:
                    print(f"It has to be between 1 and {day_maximum}.\n")
            except ValueError:
                print("Invalid input: type a whole number.")

        # Make sure a valid hour, minute, and second is selected in 24-hour format
            # Allow floats for the seconds category, truncate it to 6 digits for microseconds
        while True:
            string = "What time is it?\n"
            string += "Use 24-hour format, with seconds optional.\n"
            string += "Use colons (:) to split the hours, minutes, and seconds.\n"
            string += "You can use a decimal to represent up to microseconds.\n\n"
            
            print(string)
            choice = input("> ")

            time_list = choice.split(":") # Confirm with winikka that .split() won't error when the string is missing the splitter token
            
            # hour/minute proofchecking
            try:
                time_list[1]
            except IndexError:
                print("You need to put a \':\' token to seperate hours, minutes, and seconds.\n")
                continue
            
            # seconds avaliable?
            try:
                time_list[2]
                seconds = -1
            except IndexError:
                seconds = 0
            
            # Check hour
            try:
                if int(time_list[0]) <= 24 and int(time_list[0]) >= 0:
                    hours = time_list[0] % 24
                else:
                    print("There are only 24 hours a day.\n")
                    continue
            except ValueError:
                print("The hours need to be an integer.\n")
                continue
            
            # Check minutes
            try:
                if int(time_list[1]) < 60 and int(time_list[1]) >= 0:
                    minutes = time_list[1]
                else:
                    print("There are only 60 minutes in an hour.\n")
                    continue
            except ValueError:
                print("The minutes need to be an integer.\n")
                continue
            
            # Check seconds and microseconds


if __name__ == '__main__':
    change_datetime(datetime.datetime(2024, 4, 16))