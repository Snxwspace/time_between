import calculation
from datetime import datetime

def main() -> None:
    pre_run()
    


def pre_run() -> None:
    """A disclaimer before starting the program."""
    print("The output can get long, so I would suggest expanding the output terminal.\n")
    input("Press enter when you're ready to begin.")


def print_options(cur_first: datetime = None, cur_second: datetime = None, cur_precision: str = None) -> None:
    if isinstance(cur_first, datetime):
        format_first = cur_first.strftime("%b %d %Y, %I:%M:%S %p")
    else:
        format_first = cur_first
    
    if isinstance(cur_second, datetime):
        format_second = cur_second.strftime("%b %d %Y, %I:%M:%S %p")
    else:
        format_second = cur_second
    
    string = f"1. Start Date ({format_first})\n"
    string += f"2. End Date ({format_second})\n"
    string += f"3. Precision ({cur_precision})\n"
    string += f"4. Confirm\n"
    string += f"5. Cancel\n"

    print(string)


# 1. First time/date
# 2. Second time/date
# 3. Precision (Y/Mo/W/D/H/Mi/S)
# 4. Confirm
# 5. Cancel
    

if __name__ == '__main__':
    date1 = datetime(2024, 2, 29, 12, 13, 14, 567890)
    date2 = datetime(2000, 1, 1, 0, 0, 0, 0)
    print_options(date2, date1, "Month")