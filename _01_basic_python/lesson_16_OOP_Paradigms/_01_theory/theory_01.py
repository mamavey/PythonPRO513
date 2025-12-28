class Animal:
    def __init__(self, name, paws):
        self.name = name
        self.paws = paws

    def speak(self):
        return f'Я животное {self.name} я издаю звук'

    def walk(self):
        return f'Я животное {self.name} я хожу на {self.paws}-x лапах'


class Dog(Animal):

    def __init__(self, name, paws, age):
        super().__init__(name, paws)
        self.age = age

    def speak(self):
        animal_sound = super().speak()
        return f'{animal_sound}\nЯ собака: {self.name}. Гав-Гав!'

    def walk(self):
        return f'Я собака по кличке: {self.name} я хожу на {self.paws}-х лапах!'


class Cat(Animal):
    def speak(self):
        return f'Я кот по кличке: {self.name}. Мяу-Мяу!'


if __name__ == '__main__':
    animal = Animal('Кличка', 4)
    print(animal.speak())
    print(animal.walk())
    print()

    dog = Dog("Шарик", 4, 5)
    print(dog.speak())
    print(dog.walk())
    print()

    cat = Cat('Мурзик', 3)
    print(cat.speak())
    print(cat.walk())

