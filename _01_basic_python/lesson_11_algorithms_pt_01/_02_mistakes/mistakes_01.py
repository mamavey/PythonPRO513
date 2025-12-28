"""
Тип ошибки 1: Изменение списка во время итерации — RuntimeError

Ошибка возникает, когда при выполнении сортировки или поиска попытаться изменить список,
по которому в данный момент выполняется итерация.
"""

# numbers = [10, 20, 30, 40]
# for num in numbers:
#     if num % 20 == 0:
#         numbers.append(num)  # RuntimeError: list changed size during iteration
#     print(numbers)
# print(numbers)

"""
Решение:
Используйте копию списка для итерации
Создайте копию списка и выполняйте изменения в исходном списке.
"""

numbers = [10, 20, 30, 40]
for num in numbers[:]:  # Итерация по копии списка
    if num % 20 == 0:
        numbers.append(num)
print(numbers)
