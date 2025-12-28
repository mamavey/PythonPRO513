from utils.utils import check_file, add_participants, show_participants

if __name__ == '__main__':
    filename = r'files\participants.txt'
    while True:
        command = input('Введите команду:\n1 - add\n2 - show\n3 - create\\truncate3\n0 - exit\nВаш выбор: ')
        if command == '1':
            name = input('Введите имя участника: ').strip().title()
            add_participants(filename, name)
            print(f'Участник {name} добавлен!')
        elif command == '2':
            show_participants(filename)
        elif command == '3':
            check_file(filename)
        elif command == '0':
            print('Программа завершает работу')
            break
        else:
            print(f'Неизвестная ошибка попробуйте снова.')
