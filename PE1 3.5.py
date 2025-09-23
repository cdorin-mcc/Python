#Prompt the user to enter 5 names & store them in a list.
names = []
for i in range(5):
    name = input("Enter a name: ")
    names.append(name);

#Sort the list using the Bubble Sort algorithm.
for i in range(len(names)):
    for l in range(0, len(names)-i-1):
        if names[l] > names[l+1]:
            names[l], names[l+1] = names[l+1], names[l];

#Reverse the sorted list using a Python list method.
names.reverse()
print(names);

#Display both lists to the user.
print("Sorted Names: ", names);
print("Reversed Names: ", names);

