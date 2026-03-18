"""
Проблема ромбов при множественном наследовании
"""


class A:
    def __init__(self):
        print('class - A')


class B(A):
    def __init__(self):
        print('class - B from')
        super().__init__()


class C(A):
    def __init__(self):
        print('class - C from')
        super().__init__()


class DB(B):
    def __init__(self):
        print('class - DB from')
        super().__init__()


class DC(C):
    def __init__(self):
        print('class - DC from')
        super().__init__()


class BC(C, B):
    def __init__(self):
        print('class - BC from')
        super().__init__()


class AB(A, B):
    def __init__(self):
        print('class - AB from')
        super().__init__()


if __name__ == '__main__':
    b = B()
    print()
    c = C()
    print()
    db = DB()
    print()
    dc = DC()
    print()
    bc = BC()
    print()
    ab = AB()
