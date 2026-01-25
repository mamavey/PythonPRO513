import re

my_str = """2024 Календарь соревнований:
07.04.2024 - Гран При Японии;
21.04.2024 - Гран При Китая."""

pattern = re.compile(r'[- ;:.]')
new_str = re.sub(pattern, '**', my_str)
print(new_str)

my_str = """2024 Календарь соревнований:
07.04.2024 - Гран При Японии,
21.04.2024 - Гран При Китая;
05.05.2024 - Гран При Майами."""

pattern = re.compile(r'[-;:,\n ]+')
my_str_re_split = re.split(pattern, my_str)
print(my_str_re_split)

clean_str = []
for item in my_str_re_split:
    if item.endswith('.'):
        item = item[:-1]
    clean_str.append(item)

print(clean_str)
