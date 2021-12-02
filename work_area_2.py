# картеж(tuple)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(tpl)
#
# a = ()
# print(type(a))
# b = tuple()
# print(type(b))
#
# # упаковка картежа
# a1 = (5,)
# print(a1)
# print(type(a1))
# c = 1, 2, 3
# print(type(c))
# print(c)
#
# t1 = tuple("hello")
# print(t1)

# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(a[3])
# print(a[1:3])
# a[1] = 3

# s1 = tuple([int(input("-> ")) for i in range(5)])
# print(s1)

# s = input("Введите по порядку без пробела:")
# a = tuple(s)
# print(a)
# print(int(a[0]))
# import random as r
#
# mas = tuple([r.randint(0, 100) for i in range(10)])
# # a = tuple(mas)
# # print(a)
# print(mas)

# a = tuple(mas)
# print(i ** 2 for i in range(1, 12))
# tpl = tuple(2 ** i for i in range(1, 13))
# print(tpl)

# t1 = tuple("Hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)


# print(len(t3))
# print(t3.count("l"))
# print(t3.count("a"))
# print(t3.index("l"))
# # print(t3.index("a"))
#
# if 'a' in t3:
#     print(t3.index("a"))
# else:
#     print("Такого символа нет")

# for i in t3:
#     if i == " ":
#         continue
#     print(i, end=" ")

# def slicer(tpl, l):
#     if l in tpl:
#         if tpl.count(l) > 1:
#             f = tpl.index(l)
#             s = tpl.index(l, f + 1)
#             return tpl[f:s + 1]
#         else:
#             return tpl[tpl.index(l):]
#
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# import random as r
#
#
# def tpl(a, b):
#     mas = tuple([r.randint(a, b) for i in range(10)])
#     return mas
#
#
# x1 = tpl(0, 5)
# print(x1)
# x2 = tpl(-5, 0)
# print(x2)
# x3 = x1 + x2
# print(x3)
# print("0 =", x3.count(0))

# t = (10, 11, [1, 2, 3], [5, 6, 7], ["hello", "world"])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# def func(tpl):
#     mas = []
#     [mas.append(i) for i in reversed(tpl) if i not in mas]
#     # for i in reversed(tpl):
#     #     mas.append(i)
#     #     if i in mas:
#     #         continue
#     #     else:
#     #         mas.append(i)
#
#     return tuple(mas)
#
#
# print(func([1, 2, 3, 3, 2]))
# print(func([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)
# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])


# lst = [1, 2, 3, 4, 5]
# a = tuple(lst)
# print(a)
#
# ls = list(a)
# print(ls)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.32), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
# for country in countries:
#     country_name, country_pop, cities = country
#     print("\nСтрана:", country_name, "население =", country_pop)
#     for city in cities:
#         city_name, city_pop = city
#         print("\t\tГород:", city_name, "Население:", city_pop)


# множество - set()
# s = {"banana", "apple", "orange", "apple", "orange"}
# print(type(s))
# print(s)
# print(len(s))
# a = set('hello')
# print(a)
#
# c = ["red", "green", "green", "blue", "purple"]
# col = set(c)
# print(col)


# s = {x * x for x in range(10)}
# print(s)
# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# num = list({i for i in numbers if i % 2 == 0})
# # num = set(numbers)
# print(num)

# def to_set(mas):
#     x_mas = set(mas)
#     return x_mas, len(x_mas)
#
#
# print(to_set("я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# c = {"red", "green", "green", "blue", "purple"}
# print("green" in c)
# print("green" not in c)

# pr = {1, 2, 3, 5, 7, 7, 11}
# for i in pr:
#     print(i, end=" ")

# r = ["ab_1", "ac_2", "bc_1", "bc_2"]
# a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r if i[1] == 'c'}
# print(a)

# a = {0, 1, 2, 3}
# a.add(4)# добавление элемента
# print(a)
# a.remove(4) # удаление элемента
# print(a)
# b = 2
# if b in a:
#     a.remove(b)
# print(a)
#
# a.discard(1) # удаление элемента без генерации исключения, если элемент отсутствует
# print(a)
#
# a.pop() # удаление первого элемента
# print(a)
#
# a.pop()
# print(a)
#
#
# a.clear() # полная очистка
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # # a.update(b)
# # a |= b
# c = a.intersection(b)
# print(c)
# # a &= b
# # c = a - b
# # c = a ^ b
# c = a <= b
# print(c)
# print(a)
# a = {0, 1, 2, 3, }
# c = a.copy()
# print(c)

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}
# h = a | b | c | d | e | f | g
# print(h)
# print("Количество уникальных элементов:", len(h))
# print("Максимальный элемент:", max(h))
# print("Минимальный элемент:", min(h))

# x1 = input("введите первую строку: ")
# x2 = input("введите вторую строку: ")
# x3 = set(x1) & set(x2)
# print("Общими буквами являются:")
# for i in x3:
#     print(i, end=" ")
# draw = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# hobby1 = draw ^ music
# print(hobby1)
# hobby2 = draw & music
# print("Два хобби:", hobby2)
# draw -= hobby2
# print("Рисованием занимаются:", draw)

# тип frozenset
# s = frozenset({i ** 2 % 4 for i in range(10)})
# print(s)
# r = set("ABCD")
# b = {frozenset({i+j for j in r.difference({i})}) for i in r}
# print(b)

# def superset(s1, s2):
#     if s1 > s2:
#         print("Объект", s1, "является чистым супермножеством")
#     elif s1 == s2:
#         print("Множества равны")
#     elif s1 < s2:
#         print("Объект", s2, "является чистым супермножеством")
#     else:
#         print("Супермножество не обнаружено")
#
#
# set_1 = {1, 8, 3, 5}
# set_2 = {3, 5}
# set_3 = {5, 3, 8, 1}
# set_4 = {90, 100}
# superset(set_1, set_2)
# superset(set_1, set_3)
# superset(set_2, set_3)
# superset(set_4, set_2)

# Словари
# a = [1, 2, 3, 4]
# b = {"one": 1, "two": 2}
# print(b)

# d = {}
# print(d)
# print(type(d))
# d1 = dict()
# print(d1)
# # a = [1, 2, 3, 4]
# # c = dict()
# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3)
#
# user = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# )
# print(user)
# d_user = dict(user)
# print(d_user)

# d4 = {str(a): a ** 2 for a in range(2, 7)}
# print(d4)
# print(d4["2"])
# d4["2"] = 15
# print(d4)
# d4["5"] = 4 ** 2
# print(d4)
# d5 = {0: "text1", "one": 40, (1, 2.3): "кортеж", "two": [2, 3, 6, 7], True: 1}
# print(d5)
# print(d5["two"][1])
# print(d5[1, 2.3])
# del d5[1, 2.3]
# print(d5)
#
# print("one" in d5)
# print("a" in d5)
#
# print(d5.keys())
#
# if "one" in d5:
#     print("True")
# if "one" in d5.keys():
#     print("True")

# d6 = {"one": 1, "two": 2, "three": 3}
# # print(d6["four"])
# key = "two"
# if key in d6:
#     del d6[key]
# print(d6)
# capitals = dict()
# capitals['Россия'] = "Москва"
# capitals['Италия'] = "Рим"
# capitals['Испания'] = "Мадрид"
#
# countries = ["Россия", "Италия", "Франция", "Испания"]
#
# for country in countries:
#     if country in capitals:
#         print("Столица страны", country, ":", capitals[country])
#     else:
#         print("В базе данных нет страны с таким названием:", country)

# goods = {
#     "1": ['Core i3-4330', 9, 4500],
#     "2": ['Core i5-4670k', 3, 8500],
#     "3": ['Amd FX-6300', 6, 3700],
#     "4": ['Pentium 6320', 8, 2100],
#     "5": ['Core i5-3450', 5, 8500]
# }
# for i in goods:
#     print(i, ") ", goods[i][0], "-", goods[i][1], " шт. по ", goods[i][2], sep="")
#
# while True:
#     num = input("Введите № товара: ")
#     if int(num) == 0:
#         break
#     else:
#         sum = int(input("Введите количество товара: "))
#         goods[num][1] = sum
#
# for i in goods:
#     print(i, ") ", goods[i][0], "-", goods[i][1], " шт. по ", goods[i][2], sep="")

# d = {"A": 1, "B": 2, "C": 3}
# print(list(d.values()))

# v = d.values() # список значений
# print(v)
# lst = list(v)
# print(lst)
# value = d.get("B")
# print(value)
# value = d.get("E", "Нет такого элемента") # получение значения по заданному ключу
# print(value)
# print(d)
#
# new = d.items() # список пар ключей и значений
# print(new)
#
# new1 = dict.items(d)
# print(new1)
#
# a = d.keys() # список ключей словаря
# print(a)
#
# item = d.pop("S", 5)
# print(item)
# print(d)
# item = d.popitem() # удаляет случайную пару ключ/значение
# print(item)
# print(d)

# item = d.setdefault("E", 5) # устанавливает элемент по умолчанию
# print(item)
# print(d)

# d.update([('F', 7), ('T', 9)])
# print(d)
# d.update([('A', 10), ('B',40)])
# print(d)

# d2 = d.copy()
# print(d)
# print(d2)
# d2["B"] = 5
# d["E"] = 7
# print(d)
# print(d2)
# # x = iter(d)
# print(x)
# lst = list(x)
# print(lst)
# d.clear()
# print(d)


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # c = {'q': 5, 'b': 10}
# # z = x.copy()
# # print(z)
# # z.update(y)
# # print(x)
# # print(y)
# # print(z)
# # z = x | y | c
# z = {i: d[i] for d in [x, y] for i in d}
# print(z)

# d1 = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new = dict()
# new['name'] = d1.pop('name')
# new['salary'] = d1.pop('salary')
#
# print(new)
# print(d1)


# a = {
#     "First": {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     "Second": {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(f'\t{y}:{a[x][y]}')

# dict1 = {
#     'Jonh': {
#         'N': 3056,
#         'S': 8436,
#         'E': 8441,
#         'W': 2694,
#     },
#     'Tom': {
#         'N': 4832,
#         'S': 6786,
#         'E': 4737,
#         'W': 3612,
#     },
#     'Anne': {
#         'N': 5239,
#         'S': 4282,
#         'E': 5820,
#         'W': 1859,
#     },
#     'Fiona': {
#         'N': 3984,
#         'S': 3645,
#         'E': 8821,
#         'W': 2451,
#     }
# }
# for i in dict1:
#     print(i)
#     for y in dict1[i]:
#         print(f'\t{y}:{dict1[i][y]}')
# name = input("Введите имя: ")
# region = input("Введите регион: ")
# new_value = input("Новое значение: ")
# dict1[name][region] = new_value
# print(dict1[name])

# a = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# d = {key: value for key, value in a.items() if value < 3}
# print(d)

# a = {i: i**3 for i in range(1, 11)}
# print(a)
# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)
# value = input('->')
# lst = [1, 2, 3, 4]
# d = {k: value for k in lst}
# print(d)

# m = dict()
# m[(0, 1)] = 1
# m[(1, 2)] = 3
# m[(2, 0)] = 2
#
# print(m.get((2, 1), 0))
# print(m.get((2, 0), 0))
# try:
#     print(m[(2, 0)])
# except KeyError:
#     print(0)
# if (2, 0) in m:
#     print(m[(2, 0)])
# else:
#     print(0)

# SciPy

# list()

# a = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# k = list(a.values())  # cписок значений словаря
# print(k)
# k = list(a.keys())  # cписок ключей словаря
# print(k)
#
# par = list(a.items())  # cписок пар(ключ/значение) словаря
# print(par)

# lst = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# # dict1 = {key = i  for i in lst if i is str else value = i }
# d = dict()
# s = None
# for i in lst:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# zip
# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = zip(a, b)
# # # d = {k: v for (k, v) in zip(b, a)}
# print(d)
# print(type(d))

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = [4.6, 4.0, 9.2]
# d = zip(a, b, c)


# print(list(zip(range(5), range(100))))

# a = {12: 'Dec', 1: 'Jan', 2: 'Feb'}
# b = {12: 'KKK', 3: 'March', 4: 'April', 5: 'May'}
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# ls = [2, 1, 4, 3]
# n = ['b', 'd', 'a', 'c']
#
# # a = list(zip(ls, n))
# # print(a)
# # a.sort()
# # print(a)
# # a = list(zip(n, ls))
# # print(a)
# # a.sort()
# # print(dict(a))
#
# a = sorted(zip(ls, n))
# print(a)

# month = ['January', 'February', 'March']
# total = [52000.00, 51000.00, 48000.00]
# prod = [46800.00, 45900.00, 43200.00]
# for t, p, m in zip(total, prod, month):
#     profit = t - p
#     print(f'общая прибыль {m} = {profit}')

# one = {'apple': 0.84, 'orange': 0.35}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(f'{k} -> {v}')

# data = [5, 6, 7, 8, 9, 4, 1]
# data = {1: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 4, 7: 1}
# for i, val in enumerate(data):
#     print(f'{i} = {data[val]}')
#
# d = {1: {'a': 1, 'b': 2, 'c': 3},
#      2: {'a': 10, 'b': 20, 'c': 30}
#      }
# for i, k in enumerate(d, 1):
#     print(f'{i} ) key = {k}, value = {d[k]}', sep='')

# lst = [1, 2, 3, 4, 5]
# itr = iter(lst)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr, "STOP"))

# lst = [1, 2, 3, 4, 5]
# b = enumerate(lst)
# c = next(b)
# print(c)
# print(type(c))
# print(next(b))

# a = [1, 2, 3]
# b = [4, 5, *a, 6]
# print(b)

# def func(*args, **kwargs):
#     return args, kwargs
#
#
# print(func(4, 6, a=1, b=3, c=5))
# print(func(w="python"))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#     # return sum(params)
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 5, 1))

# def func(*args):
#     return {i: i for i in args}
#
#
# print(func(1, 2, 3, 4))
# print(func('grey', (2, 17), 3, 4))


# def func(*args):
#     summa = round(sum(args) / len(args), 1)
#     print(summa)
#     return [i for i in args if i < summa]
#
#
# print(func(1, 2, 3, 6, 8, 8, 4))


# def print_scores(student, *scores):
#     print("Имя студента: ", student)
#     for s in scores:
#         print(s, end=' ')
#     print()
#
#
# print_scores("Валентин", 100, 90, 88, 92, 99)
# print_scores("Cергей", 97, 92, 89, 91, 94)


# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or (only_add and i % 2 != 0):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))


# def info(**data):
#     for k, v in data.items():
#         print(f'{k} is {v}')
#     print()
#
#
# info(firstname="Irina", lastname="Sharma", age=22, phone='123456789')
# info(firstname="Igor", lastname="Wood",email="igor@gmail.ru", country='Russia', age=25, phone='456123879')


# my_dict = {'one': 'first'}
#
#
# def func(**kwargs):
#     my_dict.update(**kwargs)
#     return my_dict
#
#
# print(func(k1=22, k2=31, k3=11, k4=91))
# print('my_dict-', func(name='Bob', age=31, weight=61, eyes_color='grey'))


# def pet_names(name, **pets):
#     print("name:", name)
#     for pet, name in pets.items():
#         print(pet, ":", name)
#
#
# pet_names("Jonatan", dog='Brock', fish=["latty", "dery"], turtle="sylvia")


# def func(name, *args, add=False, **kwargs):
#     return name, args, add, kwargs
#
#
# print(func("irina", 1, 2, 3, 4, add=True, one='1', two='3'))

# def func(name, *args, **kwargs):
#     print(args[0])
#     print(kwargs['two'])
#
#
# func("irina", 1, 2, 3, 4, add=True, one='1', two='3')

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, 'one': 1, 'two': 2, **y}
# print(z)


# name = 'Tom'
# print(name)
#
#
# def hi():
#     global name
#     name = 'Sam'
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# print(name)
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func() # 5

# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))
# print(x)

# def add_five(a):
#     x = 2
#
#     def wrap():
#         print("x = ", x)
#         return a + x
#
#     return wrap()
#
#
# print(add_five(5))


# x = 4
#
#
# def func():
#     a = 3
#     print(x + a)
#
# func()
# max = 5
# print(max)

# import builtins
#
# names = dir(builtins)
#
# for i in names:
#     print(i)

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("world")
# outer_func("star")

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма встроенной функции", a + b)
#
#     print("Значение внешней переменной a:", a)
#     fun2(4)
#
#
# fun1()

# x = 25
#
#
# def fn():
#     global t
#     a = 30
#     t = a
#     print("global:", x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal: ", a)
#         return
#
#     inner()
#     t = a
#     return
#
#
# fn()

# z = x + t
# print(z)

# def fn1():
#     x1 = 25
#
#     def fn2():
#         x1 = 33
#
#         def fn3():
#             nonlocal x1
#             x1 = 55
#
#         fn3()
#         print('fn2.x1 = ', x1)
#     fn2()
#     print('fn1.x1 = ', x1)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# result = outer(2, 3, -1, 4)
# print("result = ", result)

#
# def par_res(a, b, c):
#     s = 0
#
#     def res_inner(i, j):
#         nonlocal s
#         s += i * j
#
#     res_inner(a, b)
#     res_inner(a, c)
#     res_inner(b, c)
#     return 2 * s
#
#
# print(par_res(2, 4, 6))
# print(par_res(5, 8, 2))
# print(par_res(1, 6, 8))

# closure(замыкание)
# def increment(n):
#     def inner_increment(x):
#         return n + x
#
#     return inner_increment


# a = increment(12)
# print(a(5))
# print(increment(12)(5))

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "1"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Nik': 69
# }
#
#
# def make_classfilter(lower, upper):
#     def class_student(exem):
#         return {k: v for (k, v) in exem.items() if lower <= v <= upper}
#
#     return class_student
#
#
# a = make_classfilter(80, 100)
# b = make_classfilter(70, 80)
# c = make_classfilter(50, 70)
# d = make_classfilter(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
#
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())

# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(2, 5))
#
# print((lambda x, y: x ** 2 + y ** 2)(5, 2))

# summ = lambda a=1, b=2, c=3: a + b + c
# print(summ())

# func1 = lambda *args: args
# print(func1(1, 2, 3, 4))
# print(func1('a', 'b'))


# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc'))

# def inc(n):
#     return lambda x: x + n
# inc = (lambda n: (lambda x: x + n))
#
# # f = inc(42)
# print((lambda n: (lambda x: x + n))(42)(5))


# print((lambda x: lambda y: (lambda z: x + y + z))(3)(5)(7))

# d = {'a': 10, 'c': 4, 'b': 15}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[0])
# print(list_d)
# print(dict(list_d))
# lst1 = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6},
# ]
#
# res = sorted(lst1, key=lambda item: item['last name'])
# print(res)
# res = sorted(lst1, key=lambda item: item['raiting'])
# print(res)
# res = sorted(lst1, key=lambda item: item['raiting'], reverse=True)
# print(res)
# d_players = list(lst1.items())

# a = [
#     (lambda x, y: x + y),
#     (lambda x, y: x - y),
#     (lambda x, y: x * y),
#     (lambda x, y: x / y),
# ]
# b = a[2](5, 12)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
#     5: lambda: print('Friday'),
#     6: lambda: print('Saturday'),
#     7: lambda: print('Sunday')
# }
#
# d[2]()

# from math import *
#
# d = {
#     'circle': lambda r: pi * r ** 2,
#     'squre': lambda a, b: (a * b),
#     'trape': lambda a, b, h: h(a + b) * 0.5
#
# }
#
# print('Площадь окружности:', d['circle'](2))
# print('Площадь прямоугольника:', d['squre'](2, 5))

# TRUE if условие else FALSE

# maximum = lambda a, b: a if a > b else b
# print(maximum(15, 13))
# print(maximum(5, 13))

# min_1 = lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c
# print(min_1(9, 8, 5))


# def mul(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# # lst2 = list(map(mul, lst))
# # print(lst2)
#
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)

# t = (2.88, -1.75, 10.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)


# lst = ['1', '2', '3', '4', '5', '6', '7']
# lst2 = list(map(int, lst))
# print(lst2)

# areas = [3.6987, 5.369787, 4.87239, 28.369874, 98.36987714, 5.236987]
# res = list(map(round, areas, range(1, 8)))
# print(res)


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)

# st = 'hello'
# res = list(map(lambda x: x * 3, st))
# print(res)

# t = ('djfugjg', 'asd', 'iymhljljfh', 'fuckable', 'pmo')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 89, 36, 78, 56, 99, 100, 45, 81]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# import random as r
#
# mas1 = [r.randint(10, 40) for i in range(10)]
# print(mas1)
#
# res = list(filter(lambda s: 10 <= s <= 20, mas1))
# print(f'[10,20] = {res}')

# lst = [45, 55, 60, 37, 100, 105, 220]
# # res = list(filter(lambda s: s % 15 == 0, lst))
# res = list(filter(lambda s: not s % 15, lst))
# print(res)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10))))
# print(m)


# a = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# m = list(filter(lambda x: x == x[::-1], a))
# print(m)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(help(square))

# a = """Тройные двойн"ые" кавычки """
# b = '''Тройные одинарные кавычки'''
# print(a)
# print(b)
# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основе заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(3, 6))
# print(cylinder.__doc__)
# print(max.__doc__)


# Декораторы
# def hello():
#     return 'Hello, I am func"Hello"'
#
#
# def super_func(func):
#     print('Hello, I am func"super_func"')
#     print(func())
#
#
# super_func(hello)
# def hello():
#     return 'Hello, I am func"Hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_1():
#         print('code before')
#         func()
#         print('code after')
#
#     return func_1
#
# @my_decorator
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
#
# # test = my_decorator(func_test)
# # test()
# func_test()

# def my_decorator(func):
#     def func_1(n, m):
#         print('*' * 20)
#         func(n, m)
#         print('*' * 20)
#
#     return func_1
#
#
# @my_decorator
# def func_test(a, b):
#     print(a * b)


# test = my_decorator(func_test)
# test()
# func_test(2, 5)

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def decor_fn(fn):
#     i = 0
#
#     def wrap():
#         fn()
#         nonlocal i
#         i += 1
#         print('Вызов функции:', i)
#
#     return wrap
#
#
# @decor_fn
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         fn(*args, **kwargs)
#         print("args:", args)
#         print("kwargs:", kwargs)
#
#     return wrap
#
#
# @args_decorator
# # def print_full_name(a, b, c='Виктор', study="Python"):
# #     print(a, b, c, "изучают", study, "\n")
#
# def one(a, b):
#     print(a + b)
#
#
# @args_decorator
# def two(a, b, c=3):
#     print(a * b * c)
#
#
# one(2, 9)
# two(2, 8, 4)
# two(2, 8, c=5)

# print_full_name("Ирина", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина")


# def args_decorator(args1, args2):
#     print("Я создаю декоратор, Аргументы:", args1, args2)
#
#     def my_decorator(func):
#         print("Я декоратор, Аргументы", args1, args2)
#
#         def wrapper(func_arg1, func_arg2):
#             print("Я - обертка вокруг декоративной функции")
#             func(args1, args2)
#             return func(func_arg1, func_arg2)
#
#         return wrapper
#
#     return my_decorator
#
#
# @args_decorator("Игорь", "Нефедов")
# def print_full_name(first, last):
#     print("Меня зовут:", first, last)
#
#
# print_full_name("Ирина", "Лаврова")


# def args_decorator(decor_text):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decor_text, end="")
#             func(*args)
#
#         return wrap
#
#     return my_decorator
#
#
# @args_decorator(decor_text="Hello, ")
# def hello_world(text):
#     print(text)
# hello_world("world!")

# def multiply(num):
#     def my_decorator(func):
#         def wrap(args):
#             return str(func(num) * args)
#
#         return wrap
#
#     return my_decorator
#
#
# @multiply(3)
# def return_num(num):
#     return num
# print(return_num(5))


# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Типы данных не соответствуют")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Типы данных не соответствуют")
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 6))
# print(typed_fn2("Hello, ", "world ", "!"))
# print(typed_fn3("Hello, ", "world! ", z=5))


# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#         return wrap
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="hello, ")
# def hello_world2(text):
#     print(text)
#
#
# hello_world("Hi!")
# hello_world2("world!")

# print(1)


# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))

# print(bin(19)) # двоичная система счисления
# print(oct(19)) # восьмиричная система счисления
# print(hex(19)) # шестнадцатиричная система счисления
#
# print(0b1010)
# print(0B1010)
# print(0o12)
# print(0xFF)
# print(0xA)

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print(e in 'I am learn Python')
# print(e in 'I am learn Java')
# s = 'Hello'
# print(s[-2])
# print(s[2:-1])
# print(s[4:0:-2])
# print(s[::-1])


# s = 'abcdefgh'
# print(s[slice(2, 5)])
# print(s[slice(5, None, -1)])
# print(s[slice(None, None, 2)])
# print(s[slice(None, None, -1)])

# s = 'python'
# print(id(s))
# s = s[:3] + 't' + s[4:]
# print(id(s))
# print(s)
# def change_Char(s, c_old, c_new):
#     a = ''
#     i = 0
#     while i < len(s):
#         if (s[i] == c_old) and (i%2 == 0):
#             a = a + c_new
#         else:
#             a = a + s[i]
#         i += 1
#
#     # for i in range(len(s)):
#     #     if s[i] == c_old:
#     #         a = s[:i] + c_new
#     #     else:
#     #         a[:i] + s[i]
#     return a
#
#
# str1 = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования.'
# str2 = change_Char(str1, "N", "P")
# print(str1)
# print(str2)

# print(u'Hello')
# print('I\'m learning\npython')
# print('C:\\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + "\\")
# print('C:\\file.txt\\')
# print(b'a1b2c3')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd'[1])

# name = "Дмитрий"
# age = 25
# print(f'Меня зовут {name}, мне {age} лет.')

# import math
# print(f"Значение числа pi: {math.pi:.2f}")
#
# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}")

# planets = ["Меркурий", "Венера", "Земля", "Марс"]
# print(f"Мы живем на планете {planets[2]}")
#
# planet = {"name": "Земля", "radius": 6378000}
#
# print(f"Планета {planet['name']}. Радиус {planet['radius']/1000}км.")
#
# print(f'13 / 3 = {round(13/3)}')

# name = "друг"
# prof = "программист"
# lang = "Python"
# message = (
#     f"Привет {name}."
#     f"Ты {prof}."
#     f"На языке {lang}."
#
# )
# print(message)

# a = 74
# print(f"{{{{{a}}}}}")

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print("home\\" + dir_name + "\\" + file_name)

# s = "5"
# s1 = "2"
# print("Мне " + str(s) + " лет")
# print(sum(s, s1))


# print(ord('a')) #97
# print(ord('#')) # 35
#
# print(ord('у'))
#
# while True:
#     n = input("-> ")
#     if n != -1:
#         print(ord(n))
#     else:
#         break


# mystr = "Test string for me"
#
# lst = [ord(x) for x in mystr]
# print(f'ASCII коды: {lst}')
#
# lst = [int(sum(lst) / len(lst))] + lst
# print(f'среднее арифмитическое {lst}')
# lst += [x for x in [ord(x) for x in (input("-> "))[:3]] if x not in lst]
# print(lst)
# if lst[-1] in lst[:-1]:
#     print("Количество последних элементов:", lst.count(lst[-1]) - 1)
#
# lst.sort(reverse=True)
# print(lst)


# print(chr(97))
# print(chr(35))

# a = 122
# b = 97
#
# if a>b:
#     for i in range(b,a+1):
#         print(chr(i),end=" ")
# else:
#     for i in range(a,b+1):
#         print(chr(i),end=" ")
# print()
# print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))
