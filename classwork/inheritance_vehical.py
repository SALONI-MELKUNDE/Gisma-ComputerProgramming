class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"



car = Car("Toyota", "BMW", 2020)
motorcycle = Motorcycle("Yamaha", "R1", 2021)


print(car.get_info())  
print(motorcycle.get_info())  

