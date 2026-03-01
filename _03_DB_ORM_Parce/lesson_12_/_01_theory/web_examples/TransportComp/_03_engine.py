class Engine:
    def __init__(self):
        print('Engine', end=' ')


class ElectricEngine(Engine):
    def __init__(self):
        super().__init__()
        print(f'Electric')


class CombustionEngine(Engine):
    def __init__(self):
        super().__init__()
        print(f'Combustion')
