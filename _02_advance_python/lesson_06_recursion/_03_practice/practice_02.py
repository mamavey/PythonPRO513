"""
Задание 2. Обход дерева задач с подсчётом

Ситуация: мы разрабатываем систему управления проектами,
где задачи организованы в виде дерева — каждая задача может иметь подзадачи,
а подзадачи, в свою очередь, могут содержать свои подзадачи.
Наша цель — подсчитать общее количество задач, включая все подзадачи.

Задача — реализовать функцию count_tasks(task_tree),
которая принимает дерево задач в виде словаря.
В каждой задаче хранятся подзадачи в списке под ключом subtasks.
Нужно использовать рекурсию и Counter для подсчёта.

task_tree = {
    "name": "Main Task",
    "subtasks": [
        {"name": "Subtask 1", "subtasks": []},
        {"name": "Subtask 2", "subtasks": [
            {"name": "Sub-subtask 1", "subtasks": []},
            {"name": "Sub-subtask 2", "subtasks": []}
        ]}
    ]
}
"""


def count_tasks(task_tree):
    if not task_tree.get('subtasks'):
        return 1
    return 1 + sum(count_tasks(subtask) for subtask in task_tree['subtasks'])


if __name__ == '__main__':
    my_task_tree = {
        "name": "Main Task",
        "subtasks": [
            {"name": "Subtask 1", "subtasks": []},
            {"name": "Subtask 2", "subtasks": [
                {"name": "Sub-subtask 1", "subtasks": []},
                {"name": "Sub-subtask 2", "subtasks": []}
            ]}
        ]
    }
    print(count_tasks(task_tree=my_task_tree))
    # my_task_tree = {
    #     "name": "Main Task"
    # }
    # print(count_tasks(task_tree=my_task_tree))
