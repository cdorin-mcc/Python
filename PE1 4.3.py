#Write a python function named calculate_interest that computes and returns simple interest based on given parameters.
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

#Prompts user for input values.
principal_amount = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate in percentage (%): "))
time_period = float(input("Enter the time period in years: "))

#Calls the function & displays calculated interest.
simple_interest = calculate_interest(principal_amount, annual_rate, time_period)
print(f"The simple interest for a principal amount of {principal_amount} at an annual rate of {annual_rate}% over {time_period} years is: {simple_interest}")
