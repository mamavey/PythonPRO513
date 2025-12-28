class SedanCar:
    wheels = 4
    doors = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f'{self.brand} {self.color} едет!')

    @classmethod
    def describe(cls):
        print(f'Все машины данного класса {SedanCar.__name__} имеют: {cls.wheels} колеса и {cls.doors} двери')


if __name__ == '__main__':
    # car = SedanCar('Toyota', 'red')
    # car.drive()
    # car.describe()  # технически возможно, но безграмотно.
    SedanCar.describe()
