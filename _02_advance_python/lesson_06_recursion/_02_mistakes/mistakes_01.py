"""
Тип ошибки 1: Бесконечная рекурсия

Возникает, когда функция вызывает саму себя бесконечно.
"""


# def calculate_factorial_rec(n):
#     # рекурсивный случай
#     return n * calculate_factorial_rec(n - 1)
#
#
# print(calculate_factorial_rec(5))


"""
Решение:

всегда добавляем базовый случай, который завершает рекурсию.
"""

def calculate_factorial_rec(n):
    # базовый случай
    if n == 1:
        return 1
    # рекурсивный случай
    return n * calculate_factorial_rec(n - 1)


if __name__ == '__main__':
    print(calculate_factorial_rec(5))
    # 5!
    # factorial_5 = 1 * 2 * 3 * 4 * 5
