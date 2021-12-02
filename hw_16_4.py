def func_bin(x):
    s = ''

    while x > 0:
        s = str(x % 2) + s
        x = x // 2
    return s


num = int(input("Введите число: "))
print(func_bin(num))
