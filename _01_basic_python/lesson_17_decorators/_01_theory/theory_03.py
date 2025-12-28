def decorator(func):
    def wrapper():
        print('До вызова функции')
        func()
        print('После вызова функции')

    return wrapper


@decorator
def say_hello():
    print('Hello world!')


if __name__ == '__main__':
    say_hello()
