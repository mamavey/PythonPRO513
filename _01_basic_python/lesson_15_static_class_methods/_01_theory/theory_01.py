class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f'{self.brand} {self.color} едет!')


if __name__ == '__main__':
    car = Car('Toyota', 'red')
    car.drive()

