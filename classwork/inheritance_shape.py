class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



my_rectangle = Rectangle(4, 8)
my_triangle = Triangle(2, 6)


print("area of the rectangle:", my_rectangle.area())
print("area of the triangle:", my_triangle.area())



