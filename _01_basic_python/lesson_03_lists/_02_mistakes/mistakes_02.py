"""
Тип ошибки 2: Изменение списка во время итерации — RuntimeError: list changed size during iteration
Изменение списка во время его перебора может привести к неожиданным результатам или ошибкам.
Пример ошибки:
"""

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     if fruit == "banana":
#         fruits.append(fruit)
#         print(fruit)            # Небезопасное изменение списка во время итерации

"""
Решение:
Используйте копию списка для безопасного перебора элементов при необходимости изменения исходного списка.
"""

fruits = ["apple", "banana", "cherry"]
for fruit in fruits[:]:  # Итерация по копии списка
    if fruit == "banana":
        fruits.append(fruit)
        print(fruit)
print(fruits)
