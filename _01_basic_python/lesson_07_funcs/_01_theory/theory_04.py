def greet(name="Гость"):
    print(f'Привет {name}!')


def introduce(name, age=None):
    if not age:
        print(f'Меня зовут {name}')
    else:
        print(f'Меня зовут {name}, мне {age} лет.')


if __name__ == '__main__':
    user_name = 'Дмитрий'
    user_age = 37
    greet()
    greet("User12345")
    introduce(user_name)
    introduce(user_name, user_age)
