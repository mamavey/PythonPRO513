def process_number(value: int):
    if not isinstance(value, int):
        raise TypeError(f'Ожидаемый тип данных int, получено {type(value).__name__}')
    return value ** 2


if __name__ == '__main__':
    print(process_number(5))
    print(process_number('5'))
