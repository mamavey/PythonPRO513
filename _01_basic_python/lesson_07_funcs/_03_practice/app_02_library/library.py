"""
Задача 2: Создание программы для управления списком книг

Ситуация: мы хотим создать программу для работы с книгами в библиотеке.
Каждая книга имеет название и автора.
Программа должна предоставлять функционал для добавления новых книг,
удаления их по названию и вывода текущего списка книг.

Задача: написать функцию library_manager, которая предоставляет следующие возможности:

1) Добавление книги.
2) Удаление книги по названию.
3) Просмотр текущего списка книг.
Создайте модуль library.py с функциями для этих операций,
а затем реализуйте основную программу, которая будет использовать этот модуль.
"""


def add_book(library, title, author):
    if title in library:
        return f'Книга уже существует'
    library[title] = author
    return f'Книга: {title}. Автор: {author} >> добавлена.'


def remove_book(library, title):
    if title in library:
        del library[title]
        return f'Книга {title} удалена!'
    return f'Книга {title} не найдена'


def get_books_list(library):
    if library:
        library_list = []
        for title, author in library.items():
            book_info = f'{title} - {author}'
            library_list.append(book_info)
        return '\n'.join(library_list)
    return 'Библиотека пуста!'
