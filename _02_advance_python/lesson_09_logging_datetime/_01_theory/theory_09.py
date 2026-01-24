from datetime import datetime, timedelta

now = datetime.now()
print(now)

formatted = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted)
print(type(formatted))

formatted = now.strftime('%d.%m.%Y %H:%M:%S')
print(formatted)

formatted = now.strftime('%d %B %Y %H:%M:%S')
print(formatted)

formatted = now.strftime('%d (%A) %B %y %H:%M:%S')
print(formatted)

"""
%Y — год (четырёхзначный);
%m — месяц (двухзначный);
%d — день (двухзначный);
%H — час (24-часовой формат);
%M — минуты;
%S — секунды.
"""

# получение объекта даты из строк разного вида
str_date1 = '10.05.2025'
str_date2 = '26-June-2025'
str_date3 = '5 Jan, 11'

first_date = datetime.strptime(str_date1, '%d.%m.%Y')
second_date = datetime.strptime(str_date2, '%d-%B-%Y')
third_date = datetime.strptime(str_date3, '%d %b, %y')

print(first_date)
print(second_date)
print(third_date)


delta1 = second_date - first_date
print(delta1)
print(sorted([first_date, second_date, third_date]))
