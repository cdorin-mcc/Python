#Construct a dictionary named nato_alphabet, where each key is a letter of the alphabet and its corresponding value is the NATO phonetic alphabet word for that letter.
nato_alphabet = {
    'A': 'Alfa',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

#Write a program with a main() function that prompts the user to enter a word and then displays the corresponding NATO phonetic alphabet words for each letter in the word.
def main():
    user_input = input("Enter a word: ").upper()
    try:
        nato_translation = [nato_alphabet[letter] for letter in user_input if letter in nato_alphabet]
        print("NATO Phonetic Alphabet Translation:")
        print(" ".join(nato_translation))
    except KeyError as e:
        print(f"Character '{e.args[0]}' is not in the NATO alphabet.")

#Calling the main function
if __name__ == "__main__":
    main()
