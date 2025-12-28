text = 'hello'
#       01234
# text[0] = 'H'
new_text = "H" + text[1:]
print(new_text)

greeting = "Hello World! Hello Python!"
first_letter = greeting[0]
print(first_letter)

sub_string = greeting[1:6]
print(sub_string)

last_symbol = greeting[-1]
print(last_symbol)

mirror_string = greeting[::-1]
print(mirror_string)

string_length = len(greeting)
print(string_length)
print()

for char in greeting:
    print(char)
print()

list_from_string = list(greeting)
print(list_from_string)

string_from_list = ''.join(list_from_string)
print(string_from_list)