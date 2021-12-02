from math import *


def rectangle(a, b):
    print("Площадь прямоугольника равна: ", a * b)


def triangle(c, h):
    print("Площадь треугольника равна: ", (c * h) / 2)


def circle(r):
    print("Площадь круга равна: ", round(pi * r ** 2, 2))


choice = int(input("Выберите фигуру:\n1-прямоугольник\n2-треугольник\n3-круг\n"))

if choice == 1:
    a = int(input("Введите сторону 1: "))
    b = int(input("Введите сторону 2: "))
    rectangle(a, b)
elif choice == 2:
    c = int(input("Введите основание: "))
    h = int(input("Введите высоту: "))
    triangle(c, h)
else:
    r = int(input("Введите радиус: "))
    circle(r)
