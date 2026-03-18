class Transport:

    def __init__(self, engine, driver):
        self.engine = engine
        self.driver = driver
        print('Transport', end=' ')


class Truck(Transport):
    def __init__(self, engine, driver):
        super().__init__(engine, driver)
        print(f'Truck')


class Car(Transport):
    def __init__(self, engine, driver):
        super().__init__(engine, driver)
        print(f'Car')


class Boat(Transport):
    def __init__(self, engine, driver):
        super().__init__(engine, driver)
        print(f'Boat')
