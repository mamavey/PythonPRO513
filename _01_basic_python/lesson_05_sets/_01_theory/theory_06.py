math_students = {"Alice", "Bob", "Charlie"}
physics_students = {"Bob", "Dave", "Eve"}

# Студенты записавшиеся на оба курса
both_courses = math_students.intersection(physics_students)
print(f'Оба курса: {both_courses}')
# both_courses = math_students & physics_students

# Студенты записавшиеся только на математику
only_math = math_students.difference(physics_students)
print(f'Только математика: {only_math}')
# only_math = math_students - physics_students

# Студенты хотя бы на 1 курс
any_course = math_students.union(physics_students)
print(f'Хотя бы 1 курс: {any_course}')
print(f'Хотя бы 1 курс: {', '.join(any_course)}.')
# any_course = math_students | physics_students


