greeting = "Hello world!"
monty_python = "I like 'Monty Python'"
print(monty_python)
monty_python1 = 'I like "Monty Python"'
print(monty_python1)
monty_python2 = "I like's \"Monty Python\""
print(monty_python2)

multiple_string = """
Это "многострочная" строка,
    которая 'переносится'
        на несколько строк
"""
print(multiple_string)

def add(a, b):
    """
    Функция складывает значения a и b
    :param a:
        int/float - значение параметра a
    :param b:
        int/float - значение параметра b
    :return:
        int/float - сумма значений a и b
    """
    return a + b