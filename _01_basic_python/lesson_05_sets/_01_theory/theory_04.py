set_a = {1, 2, 3}  # для set_b - подмножество (subset)
set_b = {1, 2, 3, 4, 5}  # для set_a - надмножество (superset)

print(set_a.issubset(set_b))
print(set_a <= set_b)
print()
print(set_b.issuperset(set_a))
print(set_b >= set_a)
print()

set_c = {1, 2, 3}
print(set_a == set_c)
