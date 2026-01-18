"""
Тип ошибки 2: Глубина рекурсии слишком велика

Возникает, когда рекурсия имеет слишком большую глубину.
"""

# def calculate_factorial_rec(n):
#     # базовый случай
#     if n == 1:
#         return 1
#     # рекурсивный случай
#     return n * calculate_factorial_rec(n - 1)

# print(calculate_factorial_rec(1000))

"""
Python имеет ограничение на глубину рекурсии (обычно 1000 вызовов).
Решение:
увеличить глубину рекурсии с помощью sys.setrecursionlimit.
"""

import sys

sys.setrecursionlimit(2000)
sys.set_int_max_str_digits(10000)


def calculate_factorial_rec(n):
    # базовый случай
    if n == 1:
        return 1
    # рекурсивный случай
    return n * calculate_factorial_rec(n - 1)


if __name__ == '__main__':
    number = int(input("Значение факториала какого числа вы хотите получить: "))
    print(calculate_factorial_rec(number))
