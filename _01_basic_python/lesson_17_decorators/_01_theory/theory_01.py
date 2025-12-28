def apply_function(func, value):
    return func(value)


def square(x):
    return x * x


if __name__ == '__main__':
    result = apply_function(square, 5)
    print(result)
