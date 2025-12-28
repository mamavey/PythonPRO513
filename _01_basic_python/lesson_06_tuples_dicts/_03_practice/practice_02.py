"""
Задача 2: Управление списком проектов

Ситуация: мы разрабатываем систему для управления проектами в компании.
Каждый проект имеет уникальный номер, название, список участников и их роли в проекте.

Задача: используйте словарь для организации информации о проектах,
где ключом будет кортеж с номером и названием проекта,
а значением — словарь с множеством участников и их ролями.
"""

projects = {}
projects[(101, "Project Alpha")] = {"participants": {"Alice": "Lead", "Bob": "Developer"}}
projects[(102, "Project Beta")] = {"participants": {"Charlie": "Manager", "Dave": "Analyst"}}
# print(projects)

for proj, details in projects.items():
    # print(proj)
    proj_id, proj_name = proj
    print(f'Проект {proj_id}: {proj_name}')
    # print(details)
    participants = details['participants']
    for name, role in participants.items():
        print(f'{name} - {role}.')
    print()


# for proj, details in projects.items():
#     proj_id, proj_name = proj
#     print(f'Проект {proj_id}: {proj_name}')
#     for name, role in details['participants'].items():
#         print(f'{name} - {role}')
#     print()
