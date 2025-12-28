class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f'{self.brand} едет!')

    def stop(self):
        print(f'{self.brand} остановился!')

    def repaint(self, new_color):
        self.color = new_color
        print(f'Автомобиль: {self.brand} теперь в цвете: {self.color}')


if __name__ == '__main__':
    my_car1 = Car('Toyota', 'red')
    my_car2 = Car('Ford', 'blue')

    my_car1.drive()
    my_car1.stop()
    print()

    my_car2.drive()
    my_car2.stop()
    print()

    print(my_car1.color)
    my_car1.repaint('black')
    print(my_car1.color)
