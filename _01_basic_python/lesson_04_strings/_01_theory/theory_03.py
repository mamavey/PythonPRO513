# my_string = "   \n\tHello, world!    "
# print(my_string)
#
# stripped_string = my_string.strip()
# print(stripped_string)
# rstripped_string = my_string.rstrip()
# print(rstripped_string)
# lstripped_string = my_string.lstrip()
# print(lstripped_string)

# my_string = 'Hello world!'
# char_idx = my_string.find('wor')
# print(char_idx)
#
# my_string1 = "Hello, world! Hello python!"
# print(my_string1.find('Hello'))
# print(my_string1.rfind('Hello'))
#
# replaced_string = my_string1.replace('Hello', 'HELLO')
# print(replaced_string)
# print()
#
# my_string2 = "Hello, ***world! Hello &&&python!"
# replaced_string2 = my_string2.replace('*', '^').replace('&', '*').replace('^', '&')
# print(replaced_string2)


my_string3 = "Hello, world! Hello python!"
lower_string = my_string3.lower()
print(lower_string)
print(my_string3.upper())
print(my_string3.capitalize())
print(my_string3.title())
print(my_string3.swapcase())

my_string4 = '  apple   '
print(my_string4.strip().capitalize())

user_answer = input("Пушистый зверек говорит мяу: ")
if user_answer.strip().lower() == 'кот':
    print('Верно')
else:
    print('Неверно')


user_answer = input("Пушистый зверек говорит мяу: ")
if user_answer.strip().lower() in ['кот', 'котик', 'кошка']:
    print('Верно')
else:
    print('Неверно')
