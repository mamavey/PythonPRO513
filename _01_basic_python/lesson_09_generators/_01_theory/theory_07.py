import time

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


if __name__ == '__main__':
    for number in fibonacci(15):
        print(number)
    print()

    for line in read_file('students.txt'):
        print(line)
        time.sleep(0.5)
