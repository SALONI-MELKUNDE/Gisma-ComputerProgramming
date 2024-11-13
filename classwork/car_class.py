class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f"{self.year} {self.make} {self.model}")


my_car = Car("Toyota", "BMW", 2020)


my_car.description()
