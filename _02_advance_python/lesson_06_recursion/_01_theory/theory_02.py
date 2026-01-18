# решение через цикл
def calc_sum(n):
    res = 0
    while True:
        if n == 0:
            break
        res += n
        n -= 1
    return res


def calc_sum_recursive(n):
    if n == 1:
        return 1
    return n + calc_sum_recursive(n - 1)


"""
1) 5 + calc_sum_recursive(4)
2) 5 + (4 + calc_sum_recursive(3))
3) 5 + (4 + (3 + calc_sum_recursive(2))
4) 5 + (4 + (3 + (2 + calc_sum_recursive(1))
5) 5 + (4 + (3 + (2 + (1)))
6) 15 # возвращаем сумму: 5 + 4 + 3 + 2 + 1 = 15
"""

if __name__ == '__main__':
    print(calc_sum(5))
    print(calc_sum_recursive(5))
