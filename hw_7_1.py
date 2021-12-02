from math import sqrt


def distance(x1, x2, y1, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x_1 = int(input("Введите х1: "))
x_2 = int(input("Введите х2: "))
y_1 = int(input("Введите y1: "))
y_2 = int(input("Введите y2: "))

res = distance(x_1, x_2, y_1, y_2)
print("Расстояние между точками: ", round(res, 2))
