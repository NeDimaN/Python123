from math import sqrt

list_res = []


def func_res(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        list_res.append(x1)
        list_res.append(x2)
    elif d == 0:
        x1 = (-b) / 2 * a
        list_res.append(x1)
    else:
        list_res.append("Корней нет")

    return list_res


print("Результат =", func_res(2, 3, -5))
