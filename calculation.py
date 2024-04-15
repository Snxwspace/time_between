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

MONTH_INDEX = {
    "January": 1,
    "Febuary": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def change_datetime(cur_datetime: datetime.datetime) -> datetime.datetime:
    # Choose between datetime of calculation, a specified datetime, or cancellation
    while True:
        string = "\nChoose one of the following options for choosing the new date and time.\n"
        string += "Current date and time: "
        if isinstance(cur_datetime, datetime.datetime):
            string += cur_datetime.strftime("%b %d %Y, %I:%M:%S %p")
        else:
            string += str(cur_datetime)
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
    while True:
        year = change_year()
        month = change_month()
        day = change_day(year, month)
        time = change_time()
        hours, minutes, seconds, microseconds = time
        
        chosen_datetime = datetime.datetime(year, MONTH_INDEX[month], int(day), int(hours), 
                                            int(minutes), int(seconds), int(microseconds))
        strf_datetime = chosen_datetime.strftime("%b %d %Y, %I:%M:%S %p")
        string = f"The chosen time is {strf_datetime}.\n"
        string += "Do you want to change the time to this? y/n"
        choice = main.ask_yes_or_no(string)

        if choice:
            return chosen_datetime


def change_year() -> int:
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
                    year = int(choice)
                    return year
            else:
                print("It has to be between 0 and 9999.\n")
        except ValueError:
            print("Select an integer.\n")


def change_month() -> str:
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
        choice = input("> ")

        try:
            string = "Would you like to set the month to "
            if int(choice) == 1:
                month = "January"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 2:
                month = "Febuary"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 3:
                month = "March"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 4:
                month = "April"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 5:
                month = "May"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 6:
                month = "June"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 7:
                month = "July"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 8:
                month = "August"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 9:
                month = "September"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 10:
                month = "October"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 11:
                month = "November"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            elif int(choice) == 12:
                month = "December"
                string += f"\'{month}\'? y/n\n"
                if main.ask_yes_or_no(string):
                    return month
            else:
                print("Invalid input: pick one of the list items.\n")
        except ValueError:
            print("Invalid input: type a whole number.\n")


def change_day(year: int, month: str) -> int:
    while True:
        # Make sure a valid day is selected
            # MAKE SURE TO DO LEAP DAY HANDLING
            # Leap days are when the year is evenly divisible by 4 and not by 100, 
            #                                     or when evenly divisible by 400
        day_maximum = DAYS_PER_MONTH[month]
        
        # Leap day handling
        if day_maximum == 28 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            day_maximum = 29
        
        # Actual part of the function
        string = "\n\nWhat day of the month is it?\n"
        string += f"The month is {month}, which has {day_maximum} days.\n\n"

        print(string)
        choice = input("> ")

        try:
            if int(choice) <= day_maximum and int(choice) > 0:
                string = "The chosen day is " + choice + ".\n"
                string += "Is this what you want? y/n\n"
                confirm = main.ask_yes_or_no(string)
                if confirm:
                    day = int(choice)
                    return day
            else:
                print(f"It has to be between 1 and {day_maximum}.\n")
        except ValueError:
            print("Invalid input: type a whole number.")


def change_time() -> tuple[int]:
    # Make sure a valid hour, minute, and second is selected in 24-hour format
        # Allow floats for the seconds category, round it to 6 digits for microseconds
    while True:
        string = "What time is it?\n"
        string += "Use 24-hour format, with seconds optional.\n"
        string += "Use colons (:) to split the hours, minutes, and seconds.\n"
        string += "You can use a decimal to represent up to microseconds.\n\n"
        
        print(string)
        choice = input("> ")

        time_list = choice.split(":")
        
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
            microseconds = 0

        # 4 value proofchecking
        try:
            time_list[3]
            print("Only two colons are allowed.")
            continue
        except IndexError:
            pass
        
        # Check hour
        try:
            if int(time_list[0]) <= 24 and int(time_list[0]) >= 0:
                hours = int(time_list[0]) % 24
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
        if seconds == -1:
            try:
                if float(time_list[2]) < 60 and float(time_list[2]) >= 0:
                    seconds = round(float(time_list[2]), 6)
                    seconds_string = str(seconds)
                    seconds_string = seconds_string.split('.')
                    seconds = seconds_string[0]
                    if len(seconds_string) == 1:
                        microseconds = 0
                    elif len(seconds_string) > 2:
                        print("you're not supposed to get this error")
                        continue
                    else:
                        microseconds = seconds_string[1]
                else:
                    print("There are only 60 seconds in a minute.")
                    continue
            except ValueError:
                print("The seconds need to be a number.")
                continue
        
        # Format minutes and seconds with a leading 0
        if len(minutes) == 1:
            minutes = "0" + minutes
        if len(str(seconds)) == 1:
            seconds = "0" + str(seconds)

        string = "Do you want to set the time to "
        string += f"{hours}:{minutes}:{seconds}.{microseconds}? y/n\n"
        choice = main.ask_yes_or_no(string)
        if choice:
            return (int(hours), int(minutes), int(seconds), int(microseconds))
        else:
            continue
        

def calculate_time_between(
        datetime_start: datetime.datetime, 
        datetime_end: datetime.datetime, 
        precision: str
        ) -> bool: # i dont feel like doing it the easy way
    """
    Calculates the difference between two different datetimes with a specified precision limit.
    
    Inputs:
        datetime_start (datetime): The starting datetime for the calculation.
        datetime_end (datetime): The ending datetime for the calculation.
        precision (string): How precise the return needs to be.
    
    Outputs:
        status (boolean): A boolean indicating whether it was successful or not.
    """
    
    # Add every property to a list
    start_list = [datetime_start.year, datetime_start.month, datetime_start.day, datetime_start.hour,
                  datetime_start.minute, datetime_start.second, datetime_start.microsecond]
    end_list = [datetime_end.year, datetime_end.month, datetime_end.day, datetime_end.hour,
                  datetime_end.minute, datetime_end.second, datetime_end.microsecond]
    
    # compare the lists and add the comparisons to a new list
    comparison_list = []
    for i in range(len(start_list)):
        if start_list[i] > end_list[i]:
            comparison_list.append("+")
        elif start_list[i] < end_list[i]:
            comparison_list.append("-")
        else:
            comparison_list.append("=")

    # Smaller datetime goes first! (Error protection)
    negate_delta = False
    if comparison_list.index("+") < comparison_list.index("-"):
        negate_delta = True
        temp = datetime_start
        datetime_start = datetime_end
        datetime_end = temp

    # LONG SUBTRACTION -- MILLISECONDS
    carry = False
    delta_microseconds = datetime_end.microsecond - datetime_start.microsecond
    if delta_microseconds != abs(delta_microseconds): # REPLACE WITH A sign() CALL
        delta_microseconds + 1000000
        carry = True
    
    delta_seconds = datetime_end.second - datetime_start.second
    if carry:
        delta_seconds -= 1
        carry = False
    if delta_seconds != abs(delta_seconds): # REPLACE WITH A sign() CALL
        delta_seconds + 60
        carry = True
    
    delta_minutes = datetime_end.minute - datetime_start.minute
    if carry:
        delta_minutes -= 1
        carry = False
    if delta_minutes != abs(delta_minutes): # REPLACE WITH A sign() CALL
        delta_minutes + 60
        carry = True
    
    delta_hours = datetime_end.hour - datetime_start.hour
    if carry:
        delta_hours -= 1
        carry = False
    if delta_hours != abs(delta_hours): # REPLACE WITH A sign() CALL
        delta_hours + 24
        carry = True


if __name__ == '__main__':
    calculate_time_between(datetime.datetime.now(), datetime.datetime(2024, 4, 16, 15, 30), "Minutes")