class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        __add__ — перегрузка оператора «+»
        """
        if not isinstance(other, Vector):
            raise TypeError('Оба объекта должны относится к классу: Vector')
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Вектор с координатами: x = {self.x}, y = {self.y}'


if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    # print(v3)
