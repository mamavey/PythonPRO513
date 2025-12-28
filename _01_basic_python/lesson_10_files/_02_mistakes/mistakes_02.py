"""
Тип ошибки 2: Неправильный режим работы с файлом — UnsupportedOperation
Ошибка возникает при попытке записать данные в файл, открытый в режиме чтения («r»).
"""
# file = open("example.txt", "r")
# file.write("Новый текст")  # UnsupportedOperation
# file.close()

"""
Решение:
Используйте правильный режим («w» или «a») для записи данных.
Исправленный код:
"""
with open("example.txt", "w", encoding='utf-8') as file:
    file.write("Новый текст\n")
