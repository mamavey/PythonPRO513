"""
Задача 1: Анализ гостей на мероприятиях

Ситуация: нам нужно организовать два мероприятия и мы хотим определить,
кто из гостей присутствовал на обоих мероприятиях, кто пришёл только на первое,
а кто только на второе.

Задача: напишите программу, которая:

Принимает два списка гостей (для двух разных мероприятий).
Выводит:
Гостей, которые посетили оба мероприятия.
Гостей, которые были только на первом мероприятии.
Гостей, которые были только на втором мероприятии.
"""

# Списки гостей
event1_guests = ["Alice", "Bob", "Charlie", "David"]
event2_guests = ["Charlie", "Eve", "Alice", "Frank"]

# Преобразование в множества
event1_guests_set = set(event1_guests)
event2_guests_set = set(event2_guests)

# Анализ
both_events = event1_guests_set.intersection(event2_guests_set)
only_event1 = event1_guests_set.difference(event2_guests_set)
only_event2 = event2_guests_set.difference(event1_guests)

# Вывод результатов
print(f'Посетили оба мероприятия: {', '.join(both_events)}')
print(f'Посетили только первое: {', '.join(only_event1)}')
print(f'Посетили только второе: {', '.join(only_event2)}')

