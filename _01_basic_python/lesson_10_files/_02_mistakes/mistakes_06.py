"""
Тип ошибки 6: Чтение больших файлов целиком — MemoryError
Ошибка возникает при попытке загрузить большой файл в память с помощью read().
Пример ошибки:
"""
# with open("bigfile.txt", "r", encoding='utf-8') as file:
#     content = file.read()  # Потенциальное переполнение памяти


"""
Решение:
Используйте построчное чтение с помощью цикла.
Исправленный код:
"""

# with open("bigfile.txt", "r") as file:
#     for line in file:
#         print(line.strip())
