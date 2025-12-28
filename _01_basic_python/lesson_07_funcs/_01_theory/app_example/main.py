from utilities.utilities import greet, introduce


def add():
    pass


if __name__ == '__main__':
    greet('Петр')
    introduce('Дмитрий', 37)
    print(greet)
    print(add.__module__)
    print(greet.__module__)
