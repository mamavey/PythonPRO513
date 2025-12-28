def binary_search(lst, target):
    left = 0  # Начальный индекс
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2  # Середина списка
        if lst[mid] == target:
            return f'Элемент {target} найден его индекс: {mid}'
        elif lst[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине

    return f'Элемент: {target} не найден!'


# Важно: Бинарный поиск работает только с отсортированными списками!
# Если данные не отсортированы, их сначала нужно упорядочить.

if __name__ == '__main__':
    numbers = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(numbers, 7))
    print(binary_search(numbers, 11))
    print(binary_search(numbers, 3))
    print(binary_search(numbers, 4))
