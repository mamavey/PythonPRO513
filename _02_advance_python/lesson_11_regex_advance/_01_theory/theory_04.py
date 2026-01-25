import re

my_str_1 = "А1 +375(29)6234567; МТС +375(33)3334455"
my_reg = re.compile(r'А1 \+\d{1,3}\((\d{2})\)(\d{7})')
match_obj = my_reg.match(my_str_1)
print(match_obj)
print(match_obj.group())
print(match_obj.group(1))
print(match_obj.group(2))
