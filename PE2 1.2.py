#Use the random module to generate a random number. 
import random

#Implement a while loop to allow continuous guessing until the correct number is guessed.
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    print("Welcome to 'Guess the Number'! Try to guess the number between 1 and 100.")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            if user_guess < 1 or user_guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue

            difference = abs(number_to_guess - user_guess)

            if user_guess == number_to_guess:
                print(f"Congratulations! You've guessed the correct number: {number_to_guess}")
                break
            elif difference <= 5:
                print("Very hot!")
            elif difference <= 15:
                print("Hot!")
            elif difference <= 25:
                print("Cold!")
            else:
                print("Far off, try again!")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
#Calls the function to start the game.
guess_the_number()
#End.