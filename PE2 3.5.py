#Employee Class
class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    #Subclass that inherits from the Employee class.
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

    #Getter and setter methods for each attribute.
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_number(self):
        return self.number
    def set_number(self, number):
        self.number = number
    def get_shift_number(self):
        return self.shift_number
    def set_shift_number(self, shift_number):
        self.shift_number = shift_number
    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate

    #Script to create an instance of the ProductionWorker class, prompt the user for each attribute, and then display the data stored in the object.
def main():
    name = input("Enter employee name: ")
    number = input("Enter employee number: ")
    shift_number = int(input("Enter shift number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))

    worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)

    print("\nEmployee Information:")
    print(f"Name: {worker.get_name()}")
    print(f"Number: {worker.get_number()}")
    print(f"Shift Number: {worker.get_shift_number()}")
    print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")

if __name__ == "__main__":
    main()
