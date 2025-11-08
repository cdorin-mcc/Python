#Definition of a Pet class
class Pet:
    
    def __init__(self, name, kind, breed):
        self.name = name
        self.kind = kind
        self.breed = breed
    #Getter for pet's name
    def get_name(self):
        return self.name
    #Getter for pet's kind
    def get_kind(self):
        return self.kind
    #Getter for pet's breed
    def get_breed(self):
        return self.breed
    #Setter for pet's name
    def set_name(self, name):
        self.name = name
    #Setter for pet's kind
    def set_kind(self, kind):
        self.kind = kind
    #Setter for pet's breed
    def set_breed(self, breed):
        self.breed = breed
    #Add a method called print_details that prints the pet's details
    def print_details(self):
        return f"Pet Name: {self.name}\nPet Kind: {self.kind}\nPet Breed: {self.breed}"
    
#Creating instances of Pet class
pet1 = Pet("Carlos", "Dog", "Golden Retriever")
pet2 = Pet("Katrina", "Cat", "Siamese")
pet3 = Pet("Nemo", "Fish", "Clownfish")

#Printing details of each pet
print(pet1.print_details())
print(pet2.print_details())
print(pet3.print_details())
print()

#Display the name of the class
print("Class Name:", Pet.__name__)

#Display the name of the module
print("Module Name:", Pet.__module__)

#Display the base classes of the class
print("Base Classes:", Pet.__bases__)

