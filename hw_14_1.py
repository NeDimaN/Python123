from math import sqrt

d = (lambda a: lambda b: (lambda c: b ** 2 - 4 * a * c))(2)(3)(-5)
list_res = []
x1 = (lambda a: lambda b: (lambda z: (-b - sqrt(z)) / (2 * a)))(2)(3)(d)
x2 = (lambda a: lambda b: (lambda z: (-b + sqrt(z)) / (2 * a)))(2)(3)(d)
list_res.append(x1)
list_res.append(x2)
print("Результат =", list_res)



