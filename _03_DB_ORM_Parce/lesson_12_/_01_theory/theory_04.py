"""
Множественное наследование корректное
"""


class Body:
    def __init__(self, body_type):
        self.body_type = body_type

    def display_body_type(self):
        print(f'Материал корпуса: {self.body_type}')


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def display_engine_type(self):
        print(f'Тип двигателя: {self.engine_type}')


class Wheels:
    def __init__(self, wheels_type):
        self.wheels_type = wheels_type

    def display_wheels_type(self):
        print(f'Шасси самолета: {self.wheels_type}')


class Plane(Body, Engine, Wheels):
    def __init__(self, body_type, engine_type, wheels_type):
        Body.__init__(self, body_type)
        Engine.__init__(self, engine_type)
        Wheels.__init__(self, wheels_type)


if __name__ == '__main__':
    plane = Plane('Пластик', 'Электро', 'Резиновые')
    plane.display_body_type()
    plane.display_engine_type()
    plane.display_wheels_type()
