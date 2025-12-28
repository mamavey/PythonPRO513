"""
Тип ошибки 2: Бесконечный цикл в сортировке
Ошибка происходит, когда в алгоритме пузырьковой сортировки забыть уменьшать количество итераций,
что приведёт к бесконечному циклу.
Пример ошибки:
"""

# def bubble_sort(lst):
#     n = len(lst)
#     while True:  # Ошибка: Условие выхода из цикла отсутствует
#         for i in range(n - 1):
#             # print(i)
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#     return lst
#
#
# print(bubble_sort([10, 40, 20, 30]))


"""
Решение:

Добавьте правильное условие выхода из цикла.
"""


def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


print(bubble_sort([10, 40, 20, 30]))
