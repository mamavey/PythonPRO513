class Car:

    def __init__(self, brand, color):
        self.brand = brand
        # my_car1.brand
        self.color = color


if __name__ == '__main__':
    my_car1 = Car('Toyota', 'red')
    my_car2 = Car('Ford', 'blue')
    print(my_car1.brand)
    print(my_car1.color)

    print(my_car2.brand)
    print(my_car2.color)
