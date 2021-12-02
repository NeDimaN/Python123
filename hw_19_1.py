import re

while True:
    password = input('Введите пароль:')
    if re.match(r'[0-9a-zA-Z _@]{6,18}', password):
        print('Пароль введен корректно!')
        break
    else:
        print('Пароль введен некорректно')

