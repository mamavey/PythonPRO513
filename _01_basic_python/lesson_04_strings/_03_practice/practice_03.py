"""
Наращивание строки
"""
result_string = ""

while True:
    user_input = input("Введите слово не менее чем из 5 букв или 0 для завершения работы: ")
    if user_input == "0":
        result_string = result_string[:-2]
        break

    if len(user_input.strip()) >= 5:
        result_string += user_input + ", "
        # result_string = result_string + user_input + ", "
    else:
        print(f'В слове {user_input} {len(user_input)} букв, а надо не менее 5')

print(result_string)
