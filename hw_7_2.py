from math import sin, radians


def area(a, b, y):
    print("Площадь треугольника: ", round(((a * b) * sin(radians(y))) / 2, 2))


side1 = int(input("Сторона 1: "))
side2 = int(input("Сторона 2: "))
corner = int(input("Угол: "))
area(side1, side2, corner)
