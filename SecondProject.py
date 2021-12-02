# name_new = "Dima"
# print("Hello,", name_new)
# age = 20
# print(age)
# a, b, c = 5, "Hello", 9.2
# print(a, b, c)

# PI = 3.14
# PI = 2
# print(PI)
# a = 1
# b = 2
# c = a
# a = b
# b = c
#
# print("a:", a)
# print("b:", b)

# print("строку \
# символов")
# print('строкa\nсимволов')
# print("\tДокумент   \"myfirstscript.ru\" находится на пути:\n"
#       "\"D:\Python\" ")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " ," + s2 +"!\t\t"
# print(s3 * 5)
# b1 = "Вывести на экран с помощью функции print() строку след.образом:\n"
# b2 = "\"Выполнил задание\n (Ваше ФИО)\""
# print(b1, b2)
# nam = input("Введите своё имя")
# print("Привет", nam)
# a = 2.46266899444448889989
# print(a)
# print(type(a))
# print(6/2)    #3.0
# print(7/2)     #3.5
# print(7//2)   #3

# a = 5
# b = 7
# c = 3
# d = a + b + c
# print("sum", d)
# d = a * b *c
# print("sub", d)
# d = (a + b + c)/3
# print(d)

# number = (6 + 4) * 5 ** 2 + 7
# print(number)

# num = 10
# num *= 5     # num = num * 5
# print(num)

# num = 9753
# print("Исходное число", num)
# res = (num % 10) * 1000
# num = num // 10
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += (num % 10)
# print(num)
#
# print("Обратное число", res)

# num1 = "2"
# num2 = 3
# print(int(num1) + num2)
# print(num1 + str(num2))

# num1 = "2"
# num2 = 3
# print(int(3.8))
# print(round(3.891, 2))
# print(num1 + str(num2))

# a = "5.2"
# b = 10
# print(float(a) + b)
# a = 1
# b = 2
# print("a:", a, "\nb:", b)
# name = "Victor"
# age = 28
# grade = 9.2
# print("It's %s, %d. Level: %.2f" % (name, age, grade))

# print("This is a {0}. It's {1}.".format("ball", "red"))

# name = input("Ваше имя: ")
# city = input("Ваш город: ")
# print("Вас зовут {0}.Ваш город {1}".format(name, city))
# n = input("Введите число:")
# a = input("Введите степень:")
# print(int(n) ** int(a))
# a = int(input("Введите 1-е число: "))
# b = int(input("Введите 2-е число: "))
# c = int(input("Введите 3-е число: "))
# d = int(input("Введите 4-е число: "))
#
# h = (a + b) / (c + d)
# print(round(h, 2))

# test = None
# print(test)
# print(test is None)
# test = 5
# print(test is None)
#
# print("привет" > "Привет")

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)
#
# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 or 1 + 2 == 4)
# print(not 9 - 8)

# v1 = (0 or 1) and (0 or 1)
# v2 = 0 or 1 and 0 or 1
# a = 0
# b = 0
# v3 = (a or 1) or (b and 0)
# print(v1)
# print(v2)
# print(v3)

# if логическое выражение:
# выражение
# cnt = 6
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("доступ запрещен")
# a = 15
# b = 15
# if a > b:
#     print("a больше b")
# elif a < b:
#     print("b больше a")
# else:
#     print(" a равно b")

# a = int(input("введите первую сторону: "))
# b = int(input("введите вторую сторону: "))
# c = int(input("введите третью сторону: "))
# if a == b and a == c:
#     print("треугольник равносторонний")
# elif a == b or a == c:
#     print("треугольник равнобедренный")
# else:
#     print("треугольник разносторонний")

# day = int(input("Введите день недели(цифрами): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#          print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day ==6  or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня нет")

# month = int(input("Введите номер месяца: "))
# if 1 <= month <= 2 or month == 12:
#     print("Зима")
# elif 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода")

# a, b = 5, 16
# print("a == b" if a == b else "a > b " if a > b else "a < b")


# i = 20
# while i > 0:
#     if i % 2 == 0:
#         print("i = ", i)
#     i -= 1


# s = int(input("Введите количество звездочек: "))
# i = 0
# while i < s:
#     print("*", end=" ")
#     i += 1


# n = input("введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число:")
# if n % 2 ==0:
#     print("Четное")
# else:
#     print("не четное")

# a = int(input("введите начало диапозона: "))
# b = int(input("введите конец диапозона: "))
# res = 0
# while a <= b:
#     if a % 2 != 0:
#         res += a
#     a += 1
#
# print("Сумма целых нечетных чисел :", res)

# i = 0
# while True:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# while True:
#     n = int(input("Введите положительное число: "))
#     if not n > 0:
#         break
# res = 1
# while True:
#     n = int(input("Введите  число: "))
#     if not n != 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("цикл закончен , i =", i)

# i = 1
# while i < 5:
#     print("инешний цикл : i = ", i)
#     j = 1
#     while j < 4:
#         print("\tвнутренний цикл : j = ", j)
#         j += 1
#     i += 1
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i + "*")
#     i += 1
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# for element in collections:
#     print(element)
# for i in 'Hello':
#     print(i)

# j = 1
# for color in 'red', 'blue', 'orange', 'yellow', 'green', 'black':
#     print(j, 'color:', color)
#     j += 1
# for i in 'one', 'two', 1, 28, 8.3:
#     print(i)

# for i in range(n):
#     тело цикла

# range(start, stop, step)

# for i in range(9, -1, -1):
#     print(i, end=" ")


# a = int(input("Введите число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(10):
#     print(i, end=" ")
#     if i == 5:
#         break
# else:
#     print("\nDone!")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("------")


# w = int(input("введите ширину прямоугольника: "))
# h = int(input("введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end=" ")
#     print()

# w = int(input("введите ширину прямоугольника: "))
# h = int(input("введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if (i == 0 or i == h - 1) or (j == 0 or j == w - 1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# [результирующее выражение | цикл | опциональное условие]
# print([i * 2 for i in 'Hello'])
# num = [i ** 3 for i in range(30) if i % 2 == 0]
# print(num)

# a = 12
# for i in range(1, 100):
#     num = int(input("Введите число от 1 до 100: "))
#     if num == 0:
#         print("Вы вышли")
#         break
#     if num < a:
#         print("Загаданное число больше")
#     elif num > a:
#         print("загаданное число меньше")
#     else:
#         print("Вы угадали число с ", i, "раза")
#         break


# Списки
# num = [8, 3, 9, 4, 1]
# print(id(num))
# print(num)
# print(type(num))
# print(type(['one', 'two', 2, 3.2, [1, 2, 3]]))
# print(num[0])
# print(num[-3])
# num[1] = 256
# print(num)
# num[3] += 100
# print(num)
# print(id(num))
# print("Длина списка:", len(num))

# s = [5] * 6
# # print(s)
# # b = list("Hello")
# # print(b)

# n = list(range(10, 2, -2))
# print(n)
# n = 5
# a = [i ** 2 for i in range(1, n+1)]
# print(a)

# c = [i * 3 for i in "list"]
# print(c)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)
# a = [0] * int(input("Введите количество элементов списка: "))
# # print(a)
# for i in range(len(a)):
#     a[i] = int(input("->"))
# print(a)

# a = [input("->") for i in range(int(input("введите количество элементов: ")))]
# print(a)
# a = list(range(10, 2, -2))
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
# for j in a:
#     print(j, end=" ")

# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print("---------")
# for i in my_list:
#     print(i**2, end=" ")
# print("\n---------")
# for i in range(len(my_list)):
#     my_list[i] = my_list[i] ** 2
#     print(my_list[i], end=" ")

# a =[input("->") for i in range(int(input("введите количество элементов: ")))]
# res = 0
# for i in range(len(a)):
#     if int(a[i]) < 0:
#         res += int(a[i])
# print("Сумма отрицательных элементов: ", res)


# n = list(range(21, 41))
# print("Список: ", n)
# a = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         a += 1
#     else:
#         s += n[i]
# print("Количество четных : ", a)
# print("Cумма  нечетных : ", s)

# a =[int(input("->")) for i in range(int(input("введите количество элементов: ")))]
# b = s = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         s += a[i]
#         b += 1
#
# print("среднее арифм.: ", s / b)

# s1 = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     s1.append(x)
# print(s1)

# s = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)
# import asyncio

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# i = 0
# # for i in a:
# #     for j in b:
# #         if i % 2 != 0:
# #             c.append(i)
# #             continue
# #         else:
# #             j % 2 != 0
# #             c.append(j)
# #             continue
# # print(c)
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)
# s = [1, 2, 3, 7, 89, 0, 9, 8, 9, 7, 8]
# print(s)
# # s[7:] = []
# print(s)
# s.remove(0)   # удаляем элем. из списка с заданным значением, если элем.несколько удалится 1-й
# print(s)
# # s.remove(4)
# # print(s)
#
# s[3:5] = []
# print(s)
#
# last = s.pop()  # возвращает эл. на указанные позиции, удаляя его из списка
# print(last)
# print(s)
#
# second = s.pop(-2)
# print(second)
# print(s)
#
# # s.clear()   # удаляет из списка все имеющиеся в нем значения
# # print(s)
#
# # del s[:]
# del s[1]
# print(s)


# s = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     s.append(x)
# print(s)
# k = int(input("Введите индекс: "))
# del s[k]
# print(s)
# s = []
#
# s.extend([3, 1, 3, 20, 3, 4, 3, 50, 3])
# print(s)
# num = s.count(3)  # считает количество значений "3" в списке
# print(num)
#
#
# ind = s.index(3, 3, -1)  # возвращает положение первого индекса
# print(ind)
#
#
# s_copy = s.copy()  # возвращает копию списка
# print(s)
# print(s_copy)
#
# a = [1, 2, 3]
# b = a
# a.append(20)
# print("a = ", a)
# print("b = ", b)
# s.append(120)
# print(s)
# print(s_copy)
#
# s.reverse()  # перестраивает элем.списка в обратном порядке
# print(s)
# # s.sort(reverse=True)  # сортирует список
# # print(s)
#
# # sorted_s = sorted(s, reverse=True)
# # print(sorted_s)
# # print(s)
#
# s2 = ["Виталий", "сергей", "Александр", "Анна"]
# s2.sort(key=len, reverse=True)
# print(s2)


# s = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     s.append(x)
# print(s)
# k = int(input("Введите индекс: "))
# del s[k]
# s.sort(reverse=True)
# print(s)

# import random
# from random import random, randint, randrange
#
# print(random()) # [0.0 , 1.0]
# print(randint(0, 9))
# print(randrange(0, 10, 2))

# import random as r
#
# print(r.randint(0, 5))
# print(r.randint(0, 5))
# print(r.randrange(0, 10, 2))
#
# cities = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(r.choice(cities))
#
# s = [55, 66, 77, 88, 99, 66, 45, 78, 90]
# print(r.sample(s, 5))
# print(r.choices(s, k=5))
# r.shuffle(s)
# print(s)
# print(round(r.uniform(10.5, 25.5), 3))
#
# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)


# lst = [5, 3, 2, 4, 1]
# print("Длина списка: ", len(lst))
# print("Минимальное значение : ", min(lst))
# print("Минимальное значение : ", max(lst))
# print("сумма: ", sum(lst))
# import copy
# import random as r

# num = [r.randint(1, 100) for i in range(10)]
# print(num)
# max_1 = max(num)
# print("Max: ", max(num))
# num.remove(max_1)
# num.insert(0, max_1)
# print(num)

# import random as r

# mas1 = [r.randint(0, 100) for i in range(10)]
# print(mas1)
# max_1 = max(mas1)
# print("Max: ", max_1)
# mas1.remove(max_1)
# mas1.insert(0, max_1)
#
# print(mas1)

# mas1 = [r.randint(-20, 20) for i in range(10)]
# print(mas1)
# mas1.sort(reverse=True)
# print(mas1)


# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# lst_1 = [r.randint(0, 10) for i in range(n1)]
# lst_2 = [r.randint(0, 10) for i in range(n2)]
# print("Первый список: ", lst_1)
# print("Второй список: ", lst_2)
# lst_3 = lst_1 + lst_2
# print("Третий список: ", lst_3)
# lst_3 = []
# for i in range(len(lst_1)):
#     if lst_1[i] not in lst_3:
#         lst_3.append(lst_1[i])
# for i in range(len(lst_2)):
#     if lst_2[i] not in lst_3:
#         lst_3.append(lst_2[i])
#
# print("элементы обоих списков без повторений: ", lst_3)
# lst_3 = []
# for i in lst_1:
#     repeat = False
#     for j in lst_2:
#         if i == j:
#             repeat = True
#     if not repeat:
#         lst_3.append(i)
# for i in lst_2:
#     repeat = False
#     for j in lst_2:
#         if i == j:
#             repeat = True
#     if not repeat:
#         lst_3.append(i)
# print(lst_3)
#
# lst_3 = []
# for i in range(len(lst_1)):
#     if lst_1[i] in lst_2 and lst_1[i] not in lst_3:
#         lst_3.append(lst_1[i])
# print(lst_3)
#
# lst_3 = []
# lst_3 = [min(lst_1), min(lst_2), max(lst_1), max(lst_2)]
# print(lst_3)

# users1 = ["Игорь", "Владимир", "Алла"]
# users2 = users1
# users2.append("Виктория")
# print(users1)
# print(users2)
# # is - возвращает True , если оба операнда указывают на один и тот же объект
# # is not- возвращает True , если оба операнда указывают на разные объекты
# print(users1 is users2)


# users1 = ["Игорь", "Владимир", "Алла"]
# users2 = copy.deepcopy(users1)
# users2.append("Виктория")
# print(users1)
# print(users2)
# print(id(users1))
# print(id(users2))
# print(users1 is users2)

# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8, ],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]
# print(m[1][2])
# # m[row][col]
# print(m)

# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8, ],
#     [9, 10, 11, 12]
# ]
# # for row in m:
# #     for x in row:
# #         print(x**2, end="\t")
# #     print()
# square = [[x**2 for x in row] for row in m]
# for row in square:
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# m = [[0 for x in range(w)] for y in range(h)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


# m = [[x for x in range(y, y+10)] for y in range(10)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# m = [
#     [2, 5, 8],
#     [8, 6, 9],
#     [4, 3, 2],
#     [5, 4, 1],
#     [9, 7, 6]
# ]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
#
# for i in range(len(m)):
#     if i % 2 == 0:
#         m[i].sort()
#     else:
#         m[i].sort(reverse=True)
#
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# import random as r
#
# w, h = 3, 4
# a = 0
# m = [[r.randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in m:
#     for x in row:
#         if x < 0:
#             a += 1
#         print(x, end="\t\t")
#     print()
# print("Количество отриц.элемен. : ", a)

# import math as m
# from math import * #sqrt, ceil, floor
# num = sqrt(4)
# print(num)
# num1 = ceil(3.8)
# print(num1)
# num2 = floor(3.8)
# print(num2)

# from math import pi as p
# print(pi)

# from math import *

# radius = 2
# print(pi * (radius**2))
#
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * radius, 2))

# num = -5.24
# print("Модуль числа: ", fabs(num))
#
# a = 14
# b = 8
# c = 4
# print("Наибольший общий делитель: ", gcd(a, b, c))
#
# # num_lst = [1, 5, 3, 3.8]
# num_lst = [0.3, 0.3, 0.3]
# print("Сумма", fsum(num_lst))
# print("Сумма", sum(num_lst))
# # decimal
# print(degrees(3.12159))
# print(radians(180))
# print(cos(radians(60)))
# print(sin(radians(90)))
# print(tan(radians(0)))

# a = int(input("Катет 1: "))
# b = int(input("Катет 2: "))
# print("Гипотенуза: ", sqrt(a ** 2 + b ** 2))

# x = int(input("Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - круг\n: "))
# if x == 1:
#     a = float(input("Введите сторону а = "))
#     b = float(input("Введите сторону b = "))
#     c = float(input("Введите сторону c = "))
#     print((a + b + c) / 2)
# elif x == 2:
#     a = float(input("Введите сторону а = "))
#     b = float(input("Введите сторону b = "))
#     print(a * b)
# else:
#     a = float(input("Введите радиус r = "))
#     print(round(pi * a ** 2, 2))


# import time

# sec = time.time()
# print(sec)
# local_time = time.ctime(sec)
# print("Местное время", local_time)
#
# res = time.localtime(sec)
# print("Localtime:", res)
# print("Год", res.tm_year)
# print("Месяц", res.tm_mon)
# print("День месяца", res.tm_mday)
# print("Часы", res.tm_hour)  # часы с 0 до 23
# print("Минуты", res.tm_min) # с 0 по 59
# print("Секунды", res.tm_sec) # от 0 до 61
# print("День недели", res.tm_wday)
# print("День года", res.tm_yday) # от 1 до 366
# print("Учет перехода на летнее время", res.tm_isdst) # 0 или 1
#
# print(time.strftime("Today is %B %d, %Y", time.localtime(4444446)))
#
# print(time.strftime("%m/%d/%Y, %I:%M:%S"))

# pause = 0.5
# print("Программа запустилась...")
# time.sleep(pause)
# print(str(pause) + "seconds")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print("Programm time: ", str(res) + "sec")

# start = time.monotonic()
# time.sleep(2)
# finish = time.monotonic()
# res = finish - start
# print("Programm time: ", str(res) + "sec")
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.strftime("Сегодня: %B %d, %Y"))
# sec = time.time()
# local_time = time.ctime(sec)
# print(local_time)


# def hello(name, word):
#     print("Hello,", name, ". Say " + word, sep=" ")
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(6, 7)
# get_sum(2.6, 4.3)
# get_sum("abc", "def")

# def symbol(a, b, c):
#     for i in range(a):
#         print(b if i % 2 == 0 else c, end="")
#
#     print()


# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def maxmin(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#     # print('Hi')
#
#
# # hi()
# print(maxmin(10, 5))
# print(maxmin(5, 15))

# def res(a, b):
#     if a > b:
#         return print("Результат: ", a - b)
#     else:
#         return print("Результат: ", a + b)
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# res(a, b)

# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def fib(n):
#     a, b = 0, 1
#
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b
#         c = a + b
#         a = b
#         b = c
#     print()
#
#
# x = int(input("Введите ограничение : "))
# fib(x)
# def change(lst):


# temp = lst[0]
# lst[0] = lst[-1]
# lst[-1] = temp
# lst[0], lst[-1] = lst[-1], lst[0]
# start = lst.pop()
# end = lst.pop(0)
# lst.append(end)
# lst.insert(0, start)
#     lst.append(lst[0])
#     lst[0] = lst.pop(-2)
#
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def get_sum(a, b, c, d):  # аргументы по умолчанию
#     return a + b + c + d
#
#
# print(get_sum(3, 2, 5, d=6))


# x, y, z = 1, 5, 6
# print(get_sum(1, 5, 2, 2))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5, d=6))  # именованные(ключевые) параметры
# print(get_sum(x, y, d=z))


# def res(a=20, b='-'):
#     for i in range(a):
#         print(b, end="")
#     print()
#     # print(a * b)
#
#
# res(25, "9")
# res()
# res(15, "+")
# x = int(input("введите количество символов: "))
# y = input("введите  символ: ")
# res(x, y)


# def check_passwd(username, password, min_length=8, check_username=True):
#     if len(password) < min_length:
#         print("пароль слишком короткий")
#     elif check_username and username in password:
#         print("Пароль содержит имя пользователя")
#         return False
#     else:
#         print("Пароль для пользователя", username, "прошел все проверки")
#         return True
#
#
#
#
# check_passwd("igor", '123478')
# check_passwd("igor", '123478igor', check_username=False)
# check_passwd("igor", '123478name')


# def check_num(n=9874023, even=True):
#     s = 0
#     while n > 0:
#         a = n % 10
#         if even and a % 2 == 0:
#             s += a
#         elif not even and a % 2 != 0:
#             s += a
#         n //= 10
#     return s
#
#
# print("Сумма четных элементов:")
# print(check_num(9874023))
# print(check_num(38271))
# print(check_num(123456789))
# print("Сумма нечетных элементов:")
# print(check_num(9874023, even=False))
# print(check_num(38271, even=False))
# print(check_num(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age, "\n")
#
#
# display_info("ira", 23)
# display_info(23, "ira")
# display_info(age=23, name="ira")
# display_info("Igor", age=26)

# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
#
#
# print(func(1))
# print(func(2))
# print(func(3))


# a1 = [1, 2, 3]
# # a2 = [1, 2, 3]
# print(type(a1))
# print(id(a1))
# a1.append(4)
# print(a1)
# print(id(a1))
# a1[1] = "Hello"
# print(a1)
# print(id(a1[1]))


# print(id(a2))
# print(a1 == a2)
# print(a2 is a1)
#
# a3 = 'Hello'
# a4 = 'Hello'
# print(a3 == a4)
# print(a4 is a3)

# s ="Hello"
# print(id(s))
# s += "World"  # s = s + "World"
# print(s)
# print(id(s))

# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# st = "Hello"
# print(id(st))
# st = st[1:-1]
# print(st)
# print(id(st))

# a1 = [1, 2, 3]
# a2 = [1, 2, 3]
# print(type(a1))
# print(id(a1))
# print(id(a2))
# y = a1
# print(id(y))
# print(a1 == a2)
# print(a1 is a2)
# print(a1 == y)
# print(a1 is y)
# a1[0] = 0
# print(a1)
# print(y)

# x = [1, 2, 3]
# # y = x[:]
# # print(y)
# # y[0] = 0
# # print(y)
# # print(x)
# # print(id(y))
# print(id(x))
# x += [4, 5]
# print(x)
# print(id(x))

def add_number(n):
    print("Внутри функции:", n, "=", id(n))
    n += [4]
    print("После присваивания:", n, "=", id(n))


x = [1, 2, 3]
print(x, "=", id(x))
add_number(x)
print(x, "=", id(x))
