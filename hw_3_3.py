quant = int(input("Введите количество чисел последовательности: "))
i = 0
res = 0
while i < quant:
    num = float(input("Введите число: "))
    if i == 0:
        min, max = num, num
    if min > num:
        min = num
    if max < num:
        max = num
    res += num
    i += 1
print("Количество чисел: ", quant)
print("Среднее арифметическое: ", res / quant)
print("Минимальное число: ", min)
print("Максимальное число: ", max)
