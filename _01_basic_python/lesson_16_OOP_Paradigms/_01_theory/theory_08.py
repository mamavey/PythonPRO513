from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


if __name__ == '__main__':
    circle = Circle(5)
    print(round(circle.calculate_area(), 2))
    print()

    rectangle = Rectangle(6, 4)
    print(rectangle.calculate_area())
    print(rectangle.calculate_perimeter())
