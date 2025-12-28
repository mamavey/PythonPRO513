class Student:
    def __init__(self, name, age):
        self.name = name  # Атрибут name (имя)
        self.age = age  # Атрибут age (возраст)

    def __str__(self):
        """
        __str__ — отвечает за отображение объекта для пользователя.
        """
        return f'Студента зовут {self.name}. Ему {self.age} лет'

    def __repr__(self):
        """
        __repr__ — предназначен для разработчиков, чтобы показывать более подробное описание объекта.
        """
        return f'Student("{self.name}", {self.age})'


if __name__ == '__main__':
    student = Student("Peter", 16)
    print(student.name)
    print(student.age)
    print(student)
    print(repr(student))
    print(student.__repr__())