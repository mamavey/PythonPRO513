from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    pass

    @abstractmethod
    def area(self):
        pass

    @classmethod
    def get_area(cls, shape_obj):
        print(f'Это {shape_obj}')
        return shape_obj.area()


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f'Круг с радиусом: {self.radius}'


class Square(Shape):

    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2

    def perimeter(self):
        return self.width * 4

    def __str__(self):
        return f'Квадрат со стороной: {self.width}'


if __name__ == '__main__':
    circle = Circle(5)
    print(f'Площадь круга: {circle.area():.2f}')

    square = Square(10)
    print(f'Площадь квадрата: {square.area():.2f}')
    print(f'Периметр квадрата: {square.perimeter():.2f}')

    print(f'Площадь переданной фигуры: {Shape.get_area(circle):.2f}')
    print(f'Площадь переданной фигуры: {Shape.get_area(square):.2f}')
