class SedanCar:
    wheels = 4
    doors = 4
    cars = []

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        SedanCar.cars.append(self)

    def drive(self):
        print(f'{self.brand} {self.color} едет!')

    @classmethod
    def describe(cls):
        print(f'Все машины данного класса {SedanCar.__name__} имеют: {cls.wheels} колеса и {cls.doors} двери')

    @classmethod
    def display_all_cars(cls):
        print(f'Все автомобили данного класса:')
        for car in cls.cars:
            print(car.brand, car.color)

    @staticmethod
    def general_info():
        print('Машины это транспортные средства.')


if __name__ == '__main__':
    SedanCar.general_info()
    car1 = SedanCar('Toyota', 'red')
    car2 = SedanCar('Honda', 'black')
    SedanCar.display_all_cars()
