class Driver:
    def __init__(self):
        print(f'Driver', end=' ')


class RobotDriver(Driver):
    def __init__(self):
        super().__init__()
        print('Robot')


class HumanDriver(Driver):
    def __init__(self):
        super().__init__()
        print('Human')
