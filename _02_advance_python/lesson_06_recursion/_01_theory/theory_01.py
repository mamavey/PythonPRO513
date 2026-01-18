def calculate_factorial_rec(n):
    # базовый случай
    if n == 1:
        return 1
    # рекурсивный случай
    return n * calculate_factorial_rec(n - 1)
    """
    1) 5 * calculate_factorial_rec(4)
    2) 5 * (4 * calculate_factorial_rec(3))
    3) 5 * (4 * (3 * calculate_factorial_rec(2)))
    4) 5 * (4 * (3 * (2 * (calculate_factorial_rec(1))))
    4) 5 * (4 * (3 * (2 * (1))))
                                       _________________
    5) 120 # возвращаем произведение: |5 * 4 * 3 * 2 * 1 << идем с конца
                                       -----------------
    """


if __name__ == '__main__':
    print(calculate_factorial_rec(5))
