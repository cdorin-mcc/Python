#Class definition for a Person
class Person:
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    #Method to get person's information as a formatted string
    def get_info(self):
        return f"Name: {self.name}\nAddress: {self.address}\nAge: {self.age}\nPhone: {self.phone}"
    
    #Getter for name
    def get_name(self):
        return self.name
    
    #Getter for address
    def get_address(self):
        return self.address
    
    #Getter for age
    def get_age(self):
        return self.age
    
    #Getter for phone
    def get_phone(self):
        return self.phone
    
    #Setter for name
    def set_name(self, name):
        self.name = name

    #Setter for address
    def set_address(self, address):
        self.address = address
    
    #Setter for age
    def set_age(self, age):
        self.age = age

    #Setter for phone
    def set_phone(self, phone):
        self.phone = phone

    #Creating instances of Person class
person1 = Person("Chris Dorin", "123 Northbridge Dr, Huuntley, IL", 30, "534-1235")
person2 = Person("Jane Dorin", "456 South St, Springfield, IL", 25, "987-6543")
person3 = Person("Joe Zombo", "789 East Ave, Chicago, IL", 40, "555-7890")

#Printing information of each person
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())


