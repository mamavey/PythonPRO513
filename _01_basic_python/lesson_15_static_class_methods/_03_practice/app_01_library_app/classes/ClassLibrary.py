"""
Задача 1: Управление книгами в библиотеке

Ситуация: мы управляем библиотекой и хотим добавить автоматизацию в работу с книгами.
Каждая книга может быть либо «доступна», либо «в аренде».
Для управления состоянием книг нам необходимо добавить метод класса,
который будет отслеживать общее количество книг в библиотеке, и статический метод, который проверяет,
находится ли книга в библиотеке.

Задача: создайте программу, которая позволяет:

Добавлять книги в библиотеку.
Менять статус книги (например, с «доступна» на «в аренде»).
Проверять, доступна ли книга.
Узнавать общее количество книг в библиотеке.

Ожидаемый результат:
Пользователь может добавлять книги.
Пользователь видит общий список книг.
Книга отображается как доступная или в аренде в зависимости от её статуса.
"""


class LibraryBook:
    total_books = 0
    books = []

    def __init__(self, title, status='доступна'):
        self.title = title
        self.status = status
        LibraryBook.total_books += 1
        LibraryBook.books.append(self)

    @classmethod
    def get_total_books(cls):
        return f'Всего книг в библиотеке: {cls.total_books}'
        # return f'Всего книг в библиотеке: {len(cls.books)}'  # только если нет счетчика книг

    @classmethod
    def display_all_books(cls):
        if cls.books:
            print(f'Все книги библиотеки:')
            for book in cls.books:
                print(f'Название: {book.title}/Статус: {book.status}')
        else:
            print('Библиотека пуста')

    @classmethod
    def remove_book(cls, book_obj):
        if isinstance(book_obj, cls):
            if book_obj in cls.books:
                LibraryBook.total_books -= 1
                cls.books.remove(book_obj)
                print(f'Книга {book_obj.title} удалена.')
            else:
                print(f'Книги {book_obj.title} нет в библиотеке.')
        else:
            print(f'Это не книга!')

    @staticmethod
    def is_available(book_obj):
        # if status == 'доступна':
        #     return True
        # return False
        return book_obj.status == 'доступна'

    @staticmethod
    def is_correct_status(new_status):
        return new_status in ['Доступна', 'В аренде', 'На реставрации']

    def change_status(self, new_status):
        self.status = new_status
