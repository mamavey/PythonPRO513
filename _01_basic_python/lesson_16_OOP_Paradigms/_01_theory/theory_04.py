class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} >> Мяу!'


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} >> Гав!'


if __name__ == '__main__':
    animals = [Cat('Мурзик'), Dog('Шарик')]

    for animal in animals:
        print(animal.speak())

