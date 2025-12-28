def greet(name):
    print(f'Привет {name}!')


def introduce(name, age):
    print(f'Меня зовут {name}, мне {age} лет.')


if __name__ == '__main__':
    user_name = 'Дмитрий'
    user_age = 37
    greet("Иван")
    introduce(user_name, user_age)  # вызов с использованием позиционных аргументов
    introduce(name=user_name, age=user_age)  # вызов с использованием именованных аргументов
    introduce(age=user_age, name=user_name)  # вызов с использованием именованных аргументов
