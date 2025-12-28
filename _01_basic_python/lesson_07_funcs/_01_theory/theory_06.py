# Плохой пример: f, func, function
def f(x):
    return x * x


# Хорошие примеры
def calculate_square(number):
    return number * number


def square_number(number):
    return number * number


if __name__ == '__main__':
    print(f(5))
    print(calculate_square(5))
    print(square_number(5))
