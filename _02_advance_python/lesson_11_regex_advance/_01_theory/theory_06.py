import random
import re
import string

print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)
print(string.whitespace)
print(string.printable)

# print(re.compile(fr'[{string.punctuation}]'))

random_login = random.choices(string.ascii_letters, k=8)
print(''.join(random_login))
random_pass = random.choices((string.ascii_letters + string.digits), k=12)
print(''.join(random_pass))
