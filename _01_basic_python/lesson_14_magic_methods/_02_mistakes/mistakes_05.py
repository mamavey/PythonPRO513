"""
Тип ошибки 5: Метод __len__ возвращает неправильное значение
Возникает, когда метод __len__ возвращает нецелое число.
"""


# class Group:
#     def __init__(self, members):
#         self.members = members
#
#     def __len__(self):
#         return len(self.members) / 2  # Ошибка: возвращается дробное значение.
#
#
# if __name__ == '__main__':
#     group_members = ['Иван', "Мария", "Петр", "Павел"]
#     group = Group(group_members)
#     print(len(group))


"""
Решение:
Метод __len__ должен возвращать целое число.
"""

class Group:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)