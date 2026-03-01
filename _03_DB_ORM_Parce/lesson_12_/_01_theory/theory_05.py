"""
Агрегация
"""


class Body:
    def __init__(self, body_type):
        self.body_type = body_type

    def display_body_type(self):
        print(f'Материал корпуса: {self.body_type}')

    def check(self):
        return f'Корпус из {self.body_type} готов!'

    def __str__(self):
        return self.body_type


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def display_engine_type(self):
        print(f'Тип двигателя: {self.engine_type}')

    def check(self):
        return f'Двигатель тип: {self.engine_type} готов!'

    def __str__(self):
        return self.engine_type


class Wheels:
    def __init__(self, wheels_type):
        self.wheels_type = wheels_type

    def display_wheels_type(self):
        print(f'Шасси самолета: {self.wheels_type}')

    def check(self):
        return f'Шасси тип: {self.wheels_type} готовы!'

    def __str__(self):
        return self.wheels_type


class Plane:
    def __init__(self, body, engine, wheels):
        self.body = body
        self.engine = engine
        self.wheels = wheels

    def display_plane(self):
        print(self.body)
        print(self.engine)
        print(self.wheels)

    def check_all(self):
        print(self.body.check())
        print(self.engine.check())
        print(self.wheels.check())


if __name__ == '__main__':
    plane_body = Body('Пластик')
    plane_engine = Engine('Электро')
    plane_wheels = Wheels('Резиновые')

    plane = Plane(plane_body, plane_engine, plane_wheels)
    plane.display_plane()
    print()
    plane.check_all()
