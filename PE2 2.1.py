#Convert a character to its ASCII value using the ord() function, then convert it back to the character using chr(). Use a main() function to organize the code.
def main():
    char = input("Enter a single character: ")
    if len(char) != 1:
        print("Please enter exactly one character.")
        return

    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is: {ascii_value}")

#Prompt the user to enter an ASCII value between 32 and 127.
    try:
        ascii_input = int(input("Enter an ASCII value between (32-127): "))
        if 32 <= ascii_input <= 127:
            character = chr(ascii_input)
            print(f"The character for ASCII value {ascii_input} is: '{character}'")
        else:
            print("Please enter a value within the range of 32 to 127.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

#Call the main function to execute the program.
if __name__ == "__main__":
    main()
