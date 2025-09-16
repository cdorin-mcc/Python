#Assignment Prompt: Accept a numeric grade from the user and display the letter grade.

#Asks the user for their grade in numeric form.
grade = float(input("What is the grade you earned out of 100: "))

#Checks to see what letter grade that would be.
if grade <= 100 and grade >= 90:
    print("The letter grade is: A")
elif grade <= 89 and grade >= 80:
    print("The letter grade is: B")
elif grade <= 79 and grade >= 70:
    print("The letter grade is: C")
elif grade <= 69 and grade >= 60:
    print("The letter grade is: D")
elif grade <= 59:
    print("The letter grade is: F")