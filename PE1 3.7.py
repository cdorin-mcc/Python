#Create a python script to track heart rate readings and calculate the average heart rate.

#Defining time_slots as a list with times of day

time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

#Defining heart_rates as an empty list to store heart rate readings

heart_rates = []

#Prompting the user to enter heart rate readings for each time slot

for slot in time_slots:
    while True:
        try:
            rate = int(input(f"Enter your heart rate for {slot} (in bpm): "))
            if rate <= 0:
                print("Please enter a positive integer for heart rate.")
            else:
                heart_rates.append(rate)
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

#Calculating the average heart rate

if heart_rates:
    average_heart_rate = sum(heart_rates) / len(heart_rates)
    print(f"Your average heart rate for today is: {average_heart_rate:.2f} bpm")
else:
    print("Enter your heart rate to calculate the average.")