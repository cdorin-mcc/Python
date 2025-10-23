def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterate through the string:")
    for char in example_string:
        print(char)


    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    min_char = min(example_string, key=lambda c: ord(c))
    print(min_char)



    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with max ASCII value:")
    max_char = max(example_string, key=lambda c: ord(c))
    print(max_char)



    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    index_o = example_string.find('o')
    print(index_o)


    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    char_list = list(example_string)
    print(char_list)


    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    print("\nCount of 'o' in the string:")
    print(example_string.count('o'))


main()
