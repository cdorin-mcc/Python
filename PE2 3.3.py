#Class definition for a Pet
class Pet:
    #Class Variable
    vet_name = "Doctor Doodles"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type = 'Dog'):
        #Instance Variables):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    #Getter for owner's first name
    def get_owner_first_name(self):
        return self.__owner_first_name
    #Getter for owner's last name
    def get_owner_last_name(self):
        return self.__owner_last_name
    #Getter for pet ID
    def get_pet_id(self):
        return self.__pet_id
    #Getter for pet name
    def get_pet_name(self):
        return self.__pet_name
    #Getter for pet type
    def get_pet_type(self):
        return self.__pet_type
    
    #Setter for owner's first name
    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name
    #Setter for owner's last name
    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name
    #Setter for pet ID
    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id
    #Setter for pet name
    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name
    #Setter for pet type
    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type
    
    #Method to display pet and owner information
    def display_info(self):
        return (f"Owner: {self.__owner_first_name} {self.__owner_last_name}\n"
                f"Pet ID: {self.__pet_id}\n"
                f"Pet Name: {self.__pet_name}\n"
                f"Pet Type: {self.__pet_type}\n"
                f"Veterinarian: {Pet.vet_name}")
    
#Create pet objects
pet1 = Pet("John", "Doe", "P001", "Buddy", "Dog")
pet2 = Pet("Bob", "Johnson", "P002", "Whiskers", "Cat")
pet3 = Pet("Carl", "Brown", "P003", "Goldie", "Fish")

#Create a pet instance using set
pet4 = Pet("", "", "", "", "")
pet4.set_owner_first_name("Alice")
pet4.set_owner_last_name("Smith")
pet4.set_pet_id("P004")
pet4.set_pet_name("Rex")
pet4.set_pet_type("Dog")

#Use check_property to verify attribute existence three times
check_property = Pet("Test", "User", "P000", "TestPet", "Dog")
pet = check_property
print(hasattr(pet, "_owner_first_name"))  # True
print(hasattr(pet, "_owner_last_name"))   # True
print(hasattr(pet, "_pet_id"))            # True

#Display information of each pet
print(pet1.display_info())
print(pet2.display_info())
print(pet3.display_info())
print(pet4.display_info())

