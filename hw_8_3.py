def check_num(n=9874023, even=True):
    s = 0
    while n > 0:
        a = n % 10
        if even and a % 2 == 0:
            s += a
        elif not even and a % 2 != 0:
            s += a
        n //= 10
    return s


print("Сумма четных элементов:")
print(check_num(9874023))
print(check_num(38271))
print(check_num(123456789))
print("Сумма нечетных элементов:")
print(check_num(9874023, even=False))
print(check_num(38271, even=False))
print(check_num(123456789, even=False))