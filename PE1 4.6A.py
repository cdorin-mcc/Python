#Create a tuple named programming_classes with 6 classes.
programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials", "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")

#Write a program that uses a for loop to display each class in the tuple.
for course in programming_classes:
    print(course)

#Use the len function to print how many courses are in the tuple.
print(f"\nTotal number of programming classes: {len(programming_classes)}")
