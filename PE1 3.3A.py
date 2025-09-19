#Create a program that prompts the user for two integer inputs, then demonstrate the use of operators.

#Prompts the user for inputs.
num1 = int(input("Enter a whole number: "))
num2 = int(input("Enter another whole number: "))

#AND Comparisons
if num1 > 0 and num2 > 0:
    print("Both numbers are positive: True")
else:
    print("Both numbers are positive: False")

if num1 > 20 and num2 < 80:
    print("These two numbers are within the range of 20 and 80: True")
else:
    print("These two numbers are within the range of 20 and 80: False")

#OR Comparisons
if num1 < 0 or num2 < 0:
    print("One of the numbers is negative: True")
else:
    print("One of the numbers is negative: False")

if num1 + num2 != 100 or num1 - num2 != 100:
    print("The sum or difference of these two numbers equals 100: False")
else:
    print("The sum or difference of these two numbers equals 100: True")

#NOT Comparisons
if not(num1 == num2):
    print("These numbers are equal: False")
else:
    print("These numbers are equal: True")

if num1 != 0 and num2 !=0:
    print("Neither number is zero: True")
else:
    print("Neither number is zero: False")