from abc import ABC, abstractmethod


class Person(ABC):

    @property
    @abstractmethod
    def name(self):
        pass


class Student(Person):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise TypeError(f'Тип данных неверен, ожидаемый тип данных >> строка')


if __name__ == '__main__':
    student = Student('Ivan')
    print(student.name)
    student.name = "Peter"
    print(student.name)
    # student.name = 1
