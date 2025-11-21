#Creates a program that asks the user for their birthday and converts it to a datetime object.
from datetime import datetime #Imports datetime from datetime module

def main(): #Defines main function
   
    print("\n\n") #Prints new lines for spacing
    try: #Starts try block
        today = datetime.today()
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 
        # calculate the difference between today and birthday
        delta = today - birthday
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.2425 # average year length accounting for leap years
        delta_months = delta.days // 30.44 # average month length
        delta_hours = delta.days * 24 # hours in a day
        delta_minutes = delta_hours * 60 # minutes in an hour
        print(f'You are {delta_years} years old')
        print(f'You are {delta_months} months old')
        print(f'You are {delta_hours} hours old')
        print(f'You are {delta_minutes} minutes old')
       
      
    except Exception as e: #Catches any exceptions that occur
        print(f"ooooops!!!:  {e}") 
        main()
    print("\n\n")
main() #Calls main function to run the program
