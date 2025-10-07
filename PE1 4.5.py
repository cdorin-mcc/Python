#Write a python program using a recursive function to calculate the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return n * factorial(n - 1)
    else:
        return "Factorial is not defined for negative numbers."

#Prompts the user for a non-negative integer input and call factorial, printing the results.
prompt = int(input("Enter a non-negative integer to find its factorial: "))
result = factorial(prompt)
print(f"The factorial of {prompt} is: {result}")
