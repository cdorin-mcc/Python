#Ask the user their age.
age = int(input("What is your age: "))

#Check to see if they're old enough to drive.
if age >= 16:
    print("You are old enough to drive a car.")
else:
    print("You are not old enough to drive a car.")

#Check to see if the user can vote.
if age >= 18:
    print("You are old enough to vote in the United States.")
else:
    print("You are not old enough to vote in the United States.")

#Check to see if the user can legally buy alcohol.
if age >= 21:
    print("You are old enough to buy alcohol in the United States.")
else:
    print("You are not old enough to buy alcohol in the United States.")

#Check to see if the user is eligible for a senior discount.
if age >= 65:
    print("You are eligible fo a senior discount.")
else:
    print("You are not eligible for a senior discount.")