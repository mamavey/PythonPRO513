def greet(name="Гость"):
    print(f'Привет {name}!')


def introduce(name, age=None):
    if not age:
        print(f'Меня зовут {name}')
    else:
        print(f'Меня зовут {name}, мне {age} лет.')
