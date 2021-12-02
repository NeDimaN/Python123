print("Выберите операцию:")
print("1-\"r\" -применяет унарный минус к операнду")
print("2-\"+\" -сложение")
print("3-\"-\" -вычитание")
print("4-\"/\" -деление")
print("5-\"*\" -умножение")
print("6-\"%\" -деление по модулю(остаток от деления)")
print("7-\"<\" -минимальное из двух чисел")
print("8-\">\" -максимальное из двух чисел")
num = input("Введите цифру: ")
while type(num) != int:
    try:
        num = int(num)
    except ValueError:
        print("Вы ввели не целое число!")
        num = input("Введите цифру: ")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num == 1:
    num1 = - num1
    num2 = - num2
    print(num1, num2, sep="\n")
if num == 2:
    res = num1 + num2
    print(res)
if num == 3:
    res = num1 - num2
    print(res)
if num == 4:
    try:
        res = num1 / num2
        print(res)
    except ZeroDivisionError:
        print("Делить на 0 нельзя!")
if num == 5:
    res = num1 * num2
    print(res)
if num == 6:
    res = num1 % num2
    print(res)
if num == 7:
    if num1 < num2:
        print(num1)
    else:
        print(num2)
if num == 8:
    if num1 > num2:
        print(num1)
    else:
        print(num2)
