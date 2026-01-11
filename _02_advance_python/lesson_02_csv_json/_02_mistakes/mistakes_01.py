"""
Тип ошибки 1: Ошибка в кодировке при чтении файла
Возникает, когда мы не указываем кодировку при чтении файла.
"""
import csv

with open('csv_files/data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print()

"""
Решение: указывать параметр encoding='utf-8' как при чтении так и при записи
"""
with open('csv_files/data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
