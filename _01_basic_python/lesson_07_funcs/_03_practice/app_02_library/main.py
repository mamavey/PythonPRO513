from library import add_book, remove_book, get_books_list

if __name__ == '__main__':

    library = {}

    while True:
        command = input("Введите команду (1 - add, 2 - remove, 3 - list, 4 - exit): ").strip().lower()

        if command == "1":
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            print(add_book(library, title, author))

        elif command == "2":
            title = input("Введите название книги для удаления: ").strip()
            print(remove_book(library, title))

        elif command == "3":
            print("Список книг:")
            print(get_books_list(library))

        elif command == "4":
            print("Выход из программы.")
            break

        else:
            print("Неизвестная команда.")
