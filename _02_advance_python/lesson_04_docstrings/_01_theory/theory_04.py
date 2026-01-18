from typing import List, Dict


def find_max(numbers: List[int]) -> int:
    """
    Находит максимальное значение в списке:

    Аргументы:
        numbers (List[int]): список целых чисел

    Возвращает:
        int: максимальное значение из списка
    """
    return max(numbers)


def find_max1(numbers: list[int]) -> int:
    """
    Находит максимальное значение в списке:

    Аргументы:
        numbers (list[int]): список целых чисел

    Возвращает:
        int: максимальное значение из списка
    """
    return max(numbers)


def get_value(data: Dict[str:str], key: str) -> str:
    return data[key]
