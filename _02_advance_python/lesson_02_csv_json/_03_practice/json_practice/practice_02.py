"""
Задание 2. Формирование отчёта

Ситуация: мы работаем в IT-компании, и нам нужно обработать данные с задачами сотрудников.
Данные хранятся в JSON-файле, где каждая задача содержит название, исполнителя и статус (выполнено или нет).

Задача — необходимо сформировать отчёт, в котором указано, сколько задач выполнил каждый сотрудник.

Реализуем функцию generate_report(json_file_path), которая:

1) Читает данные из JSON-файла.
2) Подсчитывает количество выполненных задач для каждого сотрудника.
3) Возвращает отчёт в виде словаря.
"""

import json
from collections import defaultdict


def generate_report(json_file_path):
    report = defaultdict(int)

    with open(json_file_path, 'r', encoding='utf-8') as fp:
        tasks = json.load(fp)
        for task in tasks:
            if task['status'] == 'completed':
                report[task['assignee']] += 1

    return dict(report)


if __name__ == '__main__':
    tasks_report = generate_report(r'files\emp_tasks.json')
    print(tasks_report)
