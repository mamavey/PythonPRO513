def my_generator():
    for i in range(1, 11):
        yield i


if __name__ == '__main__':
    gen1 = my_generator()
    print(next(gen1))
    print(next(gen1))
    print(next(gen1))
    print(next(gen1))
    print(next(gen1))
    print(next(gen1))
