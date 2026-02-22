import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\example.db')
    cursor = conn.cursor()
    try:
        # conn = sqlite3.connect(r'databases\example.db')
        # cursor = conn.cursor()
        conn.execute('BEGIN TRANSACTION')
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))
        raise sqlite3.Error('Что-то пошло не так')
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f'Ошибка: {type(e).__name__} >> {e}')
    finally:
        conn.close()
