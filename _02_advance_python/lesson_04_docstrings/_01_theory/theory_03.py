name: str = 'Ivan'
print(name)


def multiply(a: int, b: (int, float) = 1) -> (int, float):
    return a * b


if __name__ == '__main__':
    print(multiply(3, 5))
    print(multiply(3, 5.5))
