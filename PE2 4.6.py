#Custom Calendar Assignment
#Imports modules
import calendar
import datetime

def main():
    # Gets the current year
    current_year = datetime.datetime.now().year
    
    # Gets month input from user
    month_input = input("Please enter a month (1-12): ")
    
    # Validates input
    try:
        month = int(month_input)
        if month < 1 or month > 12:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 12.")
        return
    
    # Prints the calendar for the specified month and current year
    print(calendar.month(current_year, month))
if __name__ == "__main__":
    main()
