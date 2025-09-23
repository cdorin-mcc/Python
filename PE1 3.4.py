#Creating a list named days that includes all seven days of the week.
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#Creating an empty list named steps to store the number of steps taken each day.
steps = []

#Using a loop, ask the user to enter the number of steps they took for each day. Then append to the steps list.
for day in days:
    steps_counted = int(input(f"How many steps did you take on {day}?"))
    steps.append(steps_counted)

#Show the user the number of steps taken each day.
for i in range(len(days)):
    print(f"On {days[i]}, you took {steps[i]} steps.")

#Calculate and display the total number of steps taken during each week.
total_steps = sum(steps)
print(f"You took a total of {total_steps} steps this week.")

#Calculate and display the average number of steps taken per day.
average_steps = total_steps / len(days)
print(f"Your average number of steps taken per day is {average_steps} .")

