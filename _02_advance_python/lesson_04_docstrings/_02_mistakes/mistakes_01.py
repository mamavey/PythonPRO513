"""
Тип ошибки 1: Функция принимает любой тип, помимо указанного в аннотации

Возникает, когда разработчик указывает определённый тип данных в параметрах функции,
но не применяет строгую типизацию.
В связи с этим функция может вести себя не так, как это задумывалось разработчиком.

Пример ошибки:
"""


def addition(a: int, b: int) -> int:
    return a + b


print(addition(3, 5))  # 8
print(addition("3", "5"))  # "35"
print(addition("ab", "cd"))  # "abcd"

"""
Решение: используем строгую типизацию.
"""


def addition(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError(
            f'Тип ожидаемых данных для a: int, для: b int. Получено a: {type(a).__name__} b: {type(b).__name__}')


print(addition(3, 5))  # 8
print(addition(3, "5"))  # "35"
