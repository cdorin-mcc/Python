#Write the program 99 Bottles of Beer on the Wall using a while loop.
bottles = 99
while bottles > 1:
    print(bottles, "bottles of beer on the wall,", bottles, "bottles of beer.")
    bottles -= 1
    print("Take one down, pass it around,", bottles, "bottles of beer on the wall.\n")
    continue
print("1 bottle of beer on the wall, 1 bottle of beer.")
print("Take one down, pass it around, no more bottles of beer on the wall.\n")
