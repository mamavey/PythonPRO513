"""
Тип ошибки 3: Пропущенный базовый случай в рекурсии — RecursionError

В сортировке слиянием (и других рекурсивных алгоритмах)
важно указать базовый случай, чтобы остановить рекурсию.

Пример ошибки:
"""

# def merge_sort(lst):
#     mid = len(lst) // 2
#     left = merge_sort(lst[:mid])  # Рекурсия без базового случая
#     right = merge_sort(lst[mid:])
#     return left + right
#
#
# numbers = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(numbers)
# # RecursionError: maximum recursion depth exceeded

"""
Решение:

Добавьте базовый случай для остановки рекурсии:
"""


def merge_sort(lst):
    if len(lst) <= 1:  # Базовый случай: список длиной 1 уже отсортирован
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


numbers = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(numbers))
