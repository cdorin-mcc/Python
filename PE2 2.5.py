
import random

WORD_LIST = ("Dog", "Cat", "Mouse", "Elephant", "Giraffe", "Tiger", "Lion", "Bear", "Monkey", "Zebra", "Kangaroo", "Panda", "Alligator", "Crocodile", "Hippopotamus")


def game(answer, display):
    wrong = 0
    right = 0

    print("Welcome to Code of Fortune")
    print("You will guess letters until you have the word")
    print("If you have 5 wrong guesses you will lose!")

    guessed_letters = []
    
    

    while True:
        for item in display:
            print(item, end=" ")

        print("\n\n")
        guess = input("Please enter a letter: ").upper()

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            print("You have", 5 - wrong, "guesses left.")
            continue
        else:
            guessed_letters.append(guess)

        bad_guess = True
        for i in range(len(answer)):
            if guess == answer[i]:
                display[i] = guess
                right += 1
                bad_guess = False

        if bad_guess:
            print("Wrong!")
            print("You have", 5 - wrong, "guesses left.")
            wrong += 1
            if wrong > 5:
                print("You Lose!")
                print("The correct word was:", answer)
                break

        if right == len(answer):
            print("You Win!")
            print("The word was:", answer)
            break


def main():
    answer = random.choice(WORD_LIST)
    display = ["_"] * len(answer)
    game(answer, display)


main()