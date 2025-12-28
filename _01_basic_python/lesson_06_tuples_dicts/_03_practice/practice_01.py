"""
Задача1: Управление базой данных сотрудников

Ситуация: мы создаем систему для управления информацией о сотрудниках в компании.
Каждый сотрудник имеет уникальный ID, имя, должность и набор навыков.

Задача: используйте словарь для хранения информации о каждом сотруднике,
где ключом будет кортеж, содержащий ID и имя, а значением — словарь с должностью и множеством навыков.
"""

# employees = {
#     (1, 'Alice'): {'position': 'Manager', 'skills': {'leadership', 'communication'}},
#     (2, 'Bob'): {'position': 'Developer', 'skills': {'python', 'databases'}}
# }
employees = {}
employees[(1, 'Alice')] = {'position': "Manager", 'skills': {'leadership', 'communication'}}
employees[(2, 'Bob')] = {'position': "Developer", 'skills': {'python', 'databases'}}
print(employees)

for (emp_id, name), info in employees.items():
    print(f'Сотрудник {emp_id}: {name}')
    print(f'Должность: {info['position']}')
    print(f'Навыки: {', '.join(info['skills'])}')
    print()
