"""
Уровень 3: Продвинутый

Задача: напишите функцию-генератор filter_and_square(numbers, threshold),
которая принимает список чисел и пороговое значение threshold.
Генератор должен возвращать квадраты только тех чисел, которые больше threshold.
В основной программе запросите у пользователя список чисел и порог, а затем выведите результаты.

"""


def filter_and_square(numbers, threshold):
    for num in numbers:
        if num > threshold:
            yield num ** 2


if __name__ == '__main__':
    user_nums = list(
        map(int, input('Введите числа через пробел: ').split()))  # "1 2 3 4 5" >> ["1", "2", "3","4","5"]
    user_threshold = int(input('Введите пороговое значение: '))
    print(f'Квадраты чисел, превышающих порог >> {user_threshold}:')
    for square in filter_and_square(user_nums, user_threshold):
        print(square, end=', ')
