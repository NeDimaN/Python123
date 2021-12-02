num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
res = num1 if num1 > num2 and num1 > num3 else num2 if num2 > num1 and num2 > num3 else num3
print("Максимальное значение:", res)
