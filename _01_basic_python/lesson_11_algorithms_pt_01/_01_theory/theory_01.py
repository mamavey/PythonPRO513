# линейный поиск

def linear_search(lst, target):
    for index, value in enumerate(lst):  # Перебираем элементы списка с их индексами
        if target == value:  # Если элемент совпадает с тем, что мы ищем
            return f'Элемент {target} найден, его индекс: {index}'  # Сообщаем, где нашли элемент
    return f'Элемент {target} не найден'  # Если элемент не найден, возвращаем сообщение


if __name__ == '__main__':
    surnames = ['Иванов', 'Петров', 'Сидоров', 'Жуков', 'Климов']
    print(linear_search(surnames, 'Жуков'))
    print(linear_search(surnames, 'Толбухин'))
