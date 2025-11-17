#Creates a program that uses a generator function to produce all possible two-letter combinations from the letters A, B, C, D, and E.
def two_letter_combinations():
    letters = ['A', 'B', 'C', 'D', 'E']
# Generates all possible two-letter combinations using nested loops
    for first in letters:
        for second in letters:
            yield first + second
#Iterates through the generator and prints each combination
for combination in two_letter_combinations():
    print(combination)
