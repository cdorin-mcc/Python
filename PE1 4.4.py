#Create a BMI calculator that takes a user's weight and height, calculates their BMI, and categorizes it as underweight, normal weight, overweight, or obese.
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

#Prompts user for height and weight in pounds and inches
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

#Converts weight to kg and height to meters
weight_kg = weight * 0.453592
height_m = height * 0.0254

#Calculates BMI and categorizes it
bmi = calculate_bmi(weight_kg, height_m)
category = categorize_bmi(bmi)

#Displays the BMI and its assigned category
print(f"Your BMI is: {bmi:.2f} which is considered {category}.")
print(f"Weight in kg: {weight_kg:.2f}, Height in meters: {height_m:.2f}")