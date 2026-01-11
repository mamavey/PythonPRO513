"""
Задание 2. Список сотрудников

Ситуация: мы работаем в HR-отделе и собираем данные о сотрудниках. У нас есть три списка:
1) Имена сотрудников.
2) Их должности.
3) Зарплата.

Нам нужно объединить эти данные в одну строку формата «Имя-Должность-Зарплата» для каждого сотрудника.

Задача — реализовать функцию combine_employee_data(names, positions, salaries),
которая принимает три списка одинаковой длины и возвращает список строк.
Используем функцию zip для объединения данных и map для формирования строк.

Шаги реализации:

1) С помощью zip объединим три списка.
2) Используем map и лямбда-функцию для преобразования данных в нужный формат.
3) Вернём список строк.
"""


def combine_employees_data(names, positions, salaries):
    combined = zip(names, positions, salaries)
    return list(map(lambda info: f'Имя: {info[0]}. Должность: {info[1]}. Зарплата: {info[2]}', combined))


if __name__ == '__main__':
    emp_names = ['Hannah', 'Boris', 'Victoria']
    emp_positions = ['Manager', 'Developer', 'QA-Engineer']
    emp_salaries = [80000, 120000, 90000]

    for emp_info in combine_employees_data(emp_names, emp_positions, emp_salaries):
        print(emp_info)
    print()

    emp_list = list(combine_employees_data(emp_names, emp_positions, emp_salaries))
    print(emp_list)
