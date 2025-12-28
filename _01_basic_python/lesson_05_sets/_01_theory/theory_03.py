# # Объединение (union или |)
# # Возвращает множество, содержащее все уникальные элементы обоих множеств
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# list_b = [4, 5, 6, 7, 8]
#
# set_union_01 = set_a.union(set_b)
# set_union_02 = set_a | set_b
# print(set_union_01)
# print(set_union_02)
#
# set_union_03 = set_a.union(list_b)
# print(set_union_03)


# # Пересечение (intersection или &)
# # Возвращает элементы, которые есть в обоих множествах:
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# set_c = {1, 2, 4, 7, 8}
# set_intersection_01 = set_a.intersection(set_b)
# set_intersection_02 = set_a & set_b
# set_intersection_03 = set_a & set_c
# print(set_intersection_01)
# print(set_intersection_02)
# print(set_intersection_03)

# # Разность (difference или -)
# # Возвращает элементы, которые есть в одном множестве, но отсутствуют в другом:
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
#
# print(set_a.difference(set_b))
# print(set_b.difference(set_a))
#
# print(set_a - set_b)
# print(set_b - set_a)

# Симметрическая разность (symmetric_difference или ^)
# Возвращает элементы, которые есть только в одном из множеств:
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)

