"""
Задача 2: Автоматизация работы библиотеки

Ситуация: представьте, что управляете небольшой библиотекой и хотите автоматизировать её работу.
Нам нужно создать программу, которая позволит добавлять книги в библиотеку,
изменять их статусы (например, «выдана» или «в наличии») и просматривать список всех книг.

Задача: создайте программу, которая позволяет:

Добавлять книги в библиотеку.
Изменять статус книги (например, «выдана» или «в наличии»).
Просматривать список всех книг с их статусами.
"""


class Book:
    def __init__(self, title, author, status='в наличи'):
        self.title = title
        self.author = author
        self.status = status


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            return True
        raise TypeError('Объект не относится к классу: Book')

    def change_status(self, title, new_status):
        for book in self.books:
            if book.title == title:
                book.status = new_status
                return f'Статус книги "{title}" изменен на "{new_status}"'
        return f'Книга "{title}" не найдена'

    def show_books(self):
        if not self.books:
            print("Библиотека пуста!")
        else:
            print(f'Список книг в библиотеке: ')
            for book in self.books:
                print(f'{book.title} ({book.author}) - {book.status}')
