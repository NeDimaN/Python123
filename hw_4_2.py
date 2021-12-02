num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))
for i in range(num1, (num2 + 1)):
    if i % 2 != 0:
        print(i, end=" ")