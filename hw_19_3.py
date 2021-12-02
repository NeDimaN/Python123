import re

s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'
reg = r'\+?7[0-9() -]{10,16}'
reg1 = r'\+?7\s?[(]?\d{3}[)]?\s?[0-9- ]{7,9}'
print(re.findall(reg, s))
print(re.findall(reg1, s))


def val_num(num):
    reg3 = r'\+?7\s?[(]?\d{3}[)]?\s?[0-9- ]{7,9}'
    if re.findall(reg3, num):
        return print("Номер валидирован!")
    else:
        return print("Номер невалидирован!")


val_num('+7 499 456-45-78')
val_num('+74994564578')
val_num(' 7 (499) 456 45 78')
val_num(' 7 (499) 456-45-78')
val_num(' 7 (499) 456+45+78')