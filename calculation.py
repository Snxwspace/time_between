import datetime

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
    string += "3. Cancel"
    print(string)
    
    # Make sure a proper year is selected


    # Give a 1-12 list of months that can be selected



    
    # Make sure a valid day is selected
        # MAKE SURE TO DO LEAP DAY HANDLING
        # Leap days are when the year is evenly divisible by 4 and not by 100, or when evenly divisible by 400
    

    # Make sure a valid hour, minute, and second is selected in 24-hour format
        # Allow floats for the seconds category, truncate it to 6 digits for microseconds

    pass