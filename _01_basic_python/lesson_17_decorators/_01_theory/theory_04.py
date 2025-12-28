def decorator1(func):
    def wrapper(name):
        print('Декоратор1 начало')
        func(name)
        print('Декоратор1 конец')

    return wrapper


def decorator2(func):
    def wrapper(name):
        print('Декоратор2 начало')
        func(name)
        print('Декоратор2 конец')

    return wrapper


@decorator1  # 1>func>1
@decorator2  # 1>2>func>2>1
def say_hello(name):
    print(f'Hello {name}')


if __name__ == '__main__':
    say_hello('Alice')
