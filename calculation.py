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
    """Controls the first prompt for changing one of the datetimes. Takes in the original datetime and returns the new datetime."""
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
    """Creates a new datetime to replace an existing choice."""
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
    """Chooses a year for a datetime, returns as an integer."""
    # Make sure a proper year is selected
    while True:
        string = "What year is this in?\n"
        string += "Must be an integer between 0 and 9999 inclusive.\n"
        # string += "You can('t) type 'cancel' to cancel the operation" 

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
    """Chooses a month for a datetime, returns as a string of the month, capitalized."""
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
    """
    Chooses a day for a datetime.

    Inputs:
    year: Chosen year, for determining leap years.
    month: Chosen month, for determining the number of days avaliable

    Outputs:
    day: Integer for the day of the month chosen.
    """
    while True:
        # Make sure a valid day is selected
            # MAKE SURE TO DO LEAP DAY HANDLING
            # Leap days are when the year is evenly divisible by 4 and not by 100, 
            #                                     or when evenly divisible by 400
        day_maximum = DAYS_PER_MONTH[month]
        
        # Leap day handling
        if month == "Febuary" and is_leapyear(year):
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
    """Chooses a time for a datetime, returns as a tuple of integers."""
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
        ): # i dont feel like doing it the easy way
    """
    Calculates the difference between two different datetimes with a specified precision limit.
    
    Inputs:
        datetime_start (datetime): The starting datetime for the calculation.
        datetime_end (datetime): The ending datetime for the calculation.
        precision (string): How precise the return needs to be.
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
    if comparison_list.count("+") == 0:
        comparison_list.append("+") # hopefully doesnt cause problems
    if comparison_list.index("+") < comparison_list.index("-"):
        negate_delta = True
        temp = datetime_start
        datetime_start = datetime_end
        datetime_end = temp

    # LONG SUBTRACTION
    carry = False
    delta_useconds = datetime_end.microsecond - datetime_start.microsecond
    # uSeconds are microseconds
    if delta_useconds != abs(delta_useconds): 
        delta_useconds += 1000000
        carry = True
    
    delta_seconds = datetime_end.second - datetime_start.second
    if carry:
        delta_seconds -= 1
        carry = False
    if delta_seconds != abs(delta_seconds): 
        delta_seconds += 60
        carry = True
    
    delta_minutes = datetime_end.minute - datetime_start.minute
    if carry:
        delta_minutes -= 1
        carry = False
    if delta_minutes != abs(delta_minutes):
        delta_minutes += 60
        carry = True
    
    delta_hours = datetime_end.hour - datetime_start.hour
    if carry:
        delta_hours -= 1
        carry = False
    if delta_hours != abs(delta_hours):
        delta_hours += 24
        carry = True

    delta_days = datetime_end.day - datetime_start.day
    if carry:
        delta_days -= 1
        carry = False
    if delta_days != abs(delta_days):
        days_add = DAYS_PER_MONTH[datetime_end.strftime("%B")]
        # Check for leap year
        if datetime_end.month == 2:
            if is_leapyear(datetime_end.year):
                days_add += 1
        delta_days += days_add
        carry = True
        
    
    delta_months = datetime_end.month - datetime_start.month
    if carry:
        delta_months -= 1
        carry = False
    if delta_months != abs(delta_months):
        delta_months += 12
        carry = True
    
    delta_years = datetime_end.year - datetime_start.year
    if carry:
        delta_years -= 1
        carry = False
    # No need to check for negative years, I covered that already
    
    if negate_delta:
        # format the first positive number to display negative
        if delta_years != 0:
            delta_years *= -1
        elif delta_months != 0:
            delta_months *= -1
        elif delta_days != 0:
            delta_days *= -1
        elif delta_hours != 0:
            delta_hours *= -1
        elif delta_minutes != 0:
            delta_minutes *= -1
        elif delta_seconds != 0:
            delta_seconds *= -1
        elif delta_useconds != 0:
            delta_useconds *= -1
        # format datetime variables in reverse to make up for the inversion I did
        datetime_start_str = datetime_end.strftime("%A, %B %d, %Y at %I:%M:%S.%f %p")
        datetime_end_str = datetime_start.strftime("%A, %B %d, %Y at %I:%M:%S.%f %p")
    else:
        datetime_start_str = datetime_start.strftime("%A, %B %d, %Y at %I:%M:%S.%f %p")
        datetime_end_str = datetime_end.strftime("%A, %B %d, %Y at %I:%M:%S.%f %p")
    
    print(results_formatting(datetime_start_str, datetime_end_str, precision, delta_years, delta_months,
                             delta_days, delta_hours, delta_minutes, delta_seconds, delta_useconds))


def results_formatting(
        datetime_start: str,
        datetime_end: str,
        precision: str,

        delta_years: int,
        delta_months: int,
        delta_days: int,
        delta_hours: int,
        delta_minutes: int,
        delta_seconds: int,
        delta_useconds: int
        ) -> str:
    """
    Formats the calculation results for printing.
    
    Inputs:
        datetime_start: A string that represents the first datetime used.
        datetime_end: A string that represents the second datetime used.
        precision: A string representing the maximum precision for the results.
            Can only be years, months, days, hours, minutes, seconds, or microseconds, case sensitive.
        delta_xxxx: An integer representing the difference in the datetimes for the specified time unit.

    Output:
        A print-ready string containing the results in a tidy format.
    """
    string = "The time between "
    string += f"{datetime_start} and {datetime_end} is "
    if precision != "years":
        string += f"{delta_years} years, "
    else:
        string += f"{delta_years} years."
        return string
    
    if precision != "months":
        string += f"{delta_months} months, "
    else:
        string += f"and {delta_months} months."
        return string
    
    if precision != "days":
        string += f"{delta_days} days, "
    else: 
        string += f"and {delta_days} days."
        return string
    
    if precision != "hours":
        string += f"{delta_hours} hours, "
    else:
        string += f"and {delta_hours} hours."
        return string
    
    if precision != "minutes":
        string += f"{delta_minutes} minutes, "
    else:
        string += f"and {delta_minutes} minutes."
        return string
    
    if precision != "seconds":
        string += f"{delta_seconds} seconds, "
    else:
        string += f"and {delta_seconds} seconds."
        return string
    
    if precision != "microseconds":
        # Not supposed to happen, indicates problem with code
        raise ValueError("Precision not in valid set.")
    else:
        string += f"and {delta_useconds} microseconds."
        return string
    

def is_leapyear(year: int) -> bool:
    """Calculates whether it's a leapyear. Returns True if it is, and returns False if it isnt."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False



if __name__ == '__main__':
    calculate_time_between(datetime.datetime.now(), datetime.datetime(2024, 4, 16, 15, 30), "minutes")
    calculate_time_between(datetime.datetime.now(), datetime.datetime(2024, 6, 13, 12, 30), "minutes")
    calculate_time_between(datetime.datetime.now(), datetime.datetime(2025, 6, 5, 15, 30), "minutes")