#Create a Python application that allows users 
# to input their total budget and the amount spent 
# in various categories. The program will then 
# calculate and display the percentage of the total 
# budget each category represents.

#Defining my variables.
net_monthly_income = float(input("What is your net monthly income?: "))
housing = float(input("How much do you spend on housing costs?: "))
groceries = float(input("Any idea how much you spend on groceries?: "))
transportation = float(input("And how much is spent on transportation costs?: "))
utilities = float(input("How much do you spend on utility costs?: "))
debt_payments = float(input("Enter any debt payments you schedule: "))
healthcare = float(input("How much do you spend on healthcare?: "))
miscellaneous = float(input("Enter any additional fees not already mentioned: "))

#Calculating the user's expenses.
housing_costs = (housing / net_monthly_income) 
groceries_costs = (groceries / net_monthly_income)
transportation_costs = (transportation / net_monthly_income)
utilities_costs = (utilities / net_monthly_income)
debt_payments_costs = (debt_payments / net_monthly_income)
healthcare_costs = (healthcare / net_monthly_income)
miscellaneous_costs = (miscellaneous / net_monthly_income)

#Telling the user how much, and how much is left.
print("Housing costs are: ", housing_costs * 100, "% of your total monthly budget.")
print("Grocery costs are: ", groceries_costs * 100, "% of your total monthly budget.")
print("Transportation costs are: ", transportation_costs * 100, "% of your total monthly budget.")
print("Utility costs are: ", utilities_costs * 100, "% of your total monthly budget.")
print("Debt payments are: ", debt_payments_costs * 100, "% of your total monthly budget.")
print("Healthcare costs are: ", healthcare_costs * 100, "% of your total monthly budget.")
print("Miscellaneous costs are: ", miscellaneous_costs * 100, "% of your total monthly budget.")

#Spent total and how much is left. Telling the user.
total_expenses = (housing + groceries + transportation + utilities + debt_payments + healthcare + miscellaneous)
print("Your total expenses are: $", total_expenses)
remaining_income = (net_monthly_income - total_expenses)
print("Your remaining monthly income is: $", remaining_income)