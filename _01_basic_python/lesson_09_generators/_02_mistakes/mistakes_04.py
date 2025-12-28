"""
Тип ошибки 4: Ошибка в бесконечном генераторе
Бесконечный генератор без ограничения может зависнуть, если не указать условие выхода.
Пример ошибки:
"""


def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1


gen = infinite_numbers()
for n in gen:
    print(n)  # Никогда не завершится