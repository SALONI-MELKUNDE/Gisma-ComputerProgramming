class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


rect = Rectangle(5, 10)


area = rect.calculate_area()
perimeter = rect.calculate_perimeter()


print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

