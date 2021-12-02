num = int(input("Введите число: "))
res = num
ret = 0
while num > 0:
    num2 = num % 10
    ret = ret * 10 + num2
    num = num // 10
if res == ret:
    print("Число палиндром!")
else:
    print("Число не палиндром!")
