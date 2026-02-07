from classes import DatabaseDataManager, FileDataManager

if __name__ == '__main__':
    file_manager = FileDataManager(filename=r'data/data.txt')
    file_manager.save('Пример записи данных\n')
    print(file_manager.load())

    db_manager = DatabaseDataManager()
    db_manager.save('Пример данных в БД')
    print(db_manager.load())
