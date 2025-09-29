#Write a python program that includes two functions - one to calculate the area of a square, and another for the area of a circle.
#Defining square function
def square():
    side = float(input("Enter a length of the side of the square: "))
    area = side * side
    print(f"The area of the square {area} square units.")
#Defining circle function
def circle():
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius * radius
    print(f"The area of the circle is {area} square units")
#Calling the defined functions
square()
circle()
