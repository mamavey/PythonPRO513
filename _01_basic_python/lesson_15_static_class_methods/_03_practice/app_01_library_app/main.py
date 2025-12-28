from classes.ClassLibrary import LibraryBook


if __name__ == '__main__':
    book1 = LibraryBook('Мастер и Маргарита')
    book2 = LibraryBook('1984')

    if LibraryBook.is_available(book1):
        print('Доступна')
    else:
        print('Недоступна')

    new_status = 'В аренде'.strip().capitalize()
    if LibraryBook.is_correct_status(new_status):
        book1.change_status('В аренде')
    else:
        print('Неверный статус. Возможные статусы: доступна/в аренде/на реставрации')

    if LibraryBook.is_available(book1):
        print('Доступна')
    else:
        print('Недоступна')
    print()

    print(LibraryBook.get_total_books())
    LibraryBook.display_all_books()
    LibraryBook.remove_book(book1)
    print()
    print(LibraryBook.get_total_books())
    LibraryBook.display_all_books()

