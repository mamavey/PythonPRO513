"""
Тип ошибки 3: Невозможность закрыть файл
Ошибка возникает, если мы забыли закрыть файл. Это может привести к утечке памяти или повреждению файла.
"""
# file = open("example.txt", "r", encoding='utf-8')
# content = file.read()
# print(content)


"""
Решение:
Используйте конструкцию with, чтобы Python автоматически закрыл файл.
Исправленный код:
"""

with open("example.txt", "r", encoding='utf-8') as file:
    content = file.read()

print(content)
