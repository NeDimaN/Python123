# список
# кортеж
# словарь
# множество


# s = 'hello, WORLD! I am learning Python.123!#'
# print(id(s))
# # s = s.capitalize()
# print(s.capitalize()) # первый символ преобразуется в верхний регистр, все остальные преобразовываются в нижний регистр
# print(id(s))
# print(s.lower()) # преобразует все символы в нижний регистр
# print(s.upper()) # преобразует все символы в верхний регистр
# print(s.swapcase()) # меняет регистр символов на противоположный
# print(s.title()) # преобразует первые буквы всех слов в заглавные
# print(s.count('h')) # возвращает количество вхождений подстроки в строку
# print(s.lower().count('i'))
# print(len(s))
# print(s.count('l', 0, 15))
# print(s.find('Python', 3)) # возвращает первый индекс, который соответствует элементу начиная с начала строки

# s = input("Введите два слова через пробел: ")
# s1 = s[s.find(' ')+1:]
# print(s1, s[:s.find(' ')])


# str = 'ab12c59p7dq'
# digits = [int(i) for i in str if '1234567890'.find(i) != -1]
# print(digits)

# print(s.index('Python'))  # возвращает первый индекс, который соответствует элементу,начиная с начального элемента
# str = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# print(str[str.index('(') + 1: str.index(')')])

# print(s.rfind('l', 18))
# print(s.rindex('l'))

# str = 'prjgnvknvdxclskadjwehndmgrkhjgkmkncusndkmvlmbln'
# if str.count('f') == 0:
#     print("символ отсутствует")
# elif str.count('f') == 1:
#     print(str.index('f'))
# else:
#     print(str.index('f'), str.rindex('f'))

# print(s.endswith('123!'))  # определяет заканчивается ли строка заданной подстрокой
# print(s.endswith('I am', 3, 18))

# print('abv#123'.isalnum()) # определяет, состиот ли строка из букв и цифр
# print('FGHHJkiuy'.isalnum()) # определяет, состиот ли строка из букв, не присутствуют служебные символы
# print('454564#'.isdigit())# определяет, состоит ли строка из  цифр
# print('asd'.isidentifier()) # является ли строка допустимым идентификатором
# print('abc'.islower()) # определяет, являются ли буквенные символы строки строчными
# print(' '.isspace()) # определяет состоят ли строка из пробельных символов
# print('Hello'.istitle()) # определяет начинается ли строка с заглавной буквы
# print('HELLO'.isupper())# определяет, являются ли буквенные символы строки заглавными
# print('pyn'.center(11, '=')) # выравнивает строку по центру
# print('https://www.python.org'.lstrip('/:pths')) # обрезает заданные символы с левой стороны
# print('     https://www.python.org     '.rstrip())
# print('https://www.python.org/'.lstrip('htps:/').rstrip('/'))
# print('https://www.python.org/'.strip('htps:/'))

# s = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования"
# print(s.replace('Nuthon', 'Python')) # заменяет вхождение подстроки в строке

# s = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего'
# print(s)
# print(s[:s.find('о') + 1] + s[s.find('о')+1:s.rfind('о')].replace('о', 'О') + s[s.rfind('о'):])
#
# # s = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения.'
# print(s[:s.find('о') + 1] + s[s.find('о')+1:s.rfind('о')].replace('о','О') + s[s.rfind('о'):])

# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))# объединили список в строку
# print('...'.join(['1', '99']))
# print() # H:e:l:l:o
# print(':'.join('Hello'))
#
# print('Строка разделенная пробелами'.split('а'))
# print('www.python.org'.split('.', 1))

# arr = input("->").split()
#
#
# print(arr[0]+' '+arr[1][0]+'.'+arr[2][0]+'.')

import re

# s = 'Я ищу совпадения в 2021 году. И я их найду в 200000 счёта.25_65'
# reg = 'я'
# print(s.find(reg))
# # find()- в строке будет искать шаблон и возвращать индекс первого вхождения в строке
# # если шаблон не найден, то будет возвращать -1
# print(reg in s)
#
# print(re.findall(reg, s))  # возвращает все совпадения с регулярным выражением
# print(re.findall('12', s))
# print(re.search(reg, s))  # месторасположение первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# # reg = 'Я'
# print(re.match(reg, s)) # поиск по заданному шаблону вначале сироки
# reg = r'\.'
# print(re.split(reg, s)) # возвращает список , в котором строка разбита по шаблону

# s = 'Час в 24-часовом формате T21:45 Минуты в диапозоне 2021-06-25Т01:09'
# reg = r'[0-2][0-9][\:][0-5][0-9]'
# print(re.findall(reg, s))

# reg = r'\AЯ ищу'
# reg = r'20*'
# print(re.findall(reg, s))
# \d -одна любая цифра[0-9]
# \w- буква, цифра,символ подчеркивания
# \s- один пробельный символ(включая табуляцию и перенос строки)
# \D -все кроме цифр
# \W- все кроме букв, цифр,символа подчеркивания
# \S- все кроме  пробельных символов(включая табуляцию и перенос строки)
# \A -ищет символ в начале строки
#  количество повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1
# d = 'Цифры: 7, +17, -42, 0013, 0.3'
# print(re.findall(r'[+-]?\d+', d))

# s = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub('#.*', '', s))
# # заменить дефис на точки
# print(re.sub('-', ':', s))
# print("Дата рождения", re.sub("-", ":", re.sub("#.*", "", s)))
# s = '12 сентября 2021 года'
# reg = r'\d{4,}'
# print(re.findall(reg, s))
# s = ' МИД - Министерство иностранных дел, ГЭС - гидроэлектростанция, ФСБ- Федеральная служба безопасности'
# reg = r'[А-ЯЁ]{2,}\s*[А-ЯЁ]'
# print(re.findall(reg, s))


# s = '+7 499 456-45-78, +74994564578, 7(499) 456 45 78, 74994564578'
# # reg = r"[+][7]\d{10,}"
#
# reg = r"\+?7[0-9]{10}"
# print(re.findall(reg, s))

# s = 'Я ищу совпадения в 2021 году. И я их найду в 200000 счёта.'
# s = '+7 980'
# reg = r'^\+\d+\s+\d+$'
# print(re.findall(reg, s))]

# s = 'Я ищу совпадения в 2021 году. И я их найду в 200000 счёта.'
# reg = r'я'
# print(re.findall(reg, s, flags=re.IGNORECASE))
#
# print(re.findall(r'\d+', '12 + '))
# print(re.findall(r'\d+', '12 +  ', flags=re.ASCII))
#
# # re.DEBUG
# # re.LOCALE
#
#
# text = r'''
# Торт
# с вишней1
# вишней2
# '''
# # print(re.findall(r'Торт с '))
# print(re.findall(r'виш\w+', text, flags=re.DOTALL))
# print(re.findall(r'^виш\w+', text, flags=re.MULTILINE))

# print(re.findall('''
# [\w.-]+
# @ # разбиваем по @
# [\w.-]+
# ''', 'test@mail.ru', re.VERBOSE))
# import re
#
# s = 'author=Пушкин А.С.; title= Евгений Онегин; price = 200; год = 1831'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))
# import re
#
#
# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)
#
#
# print(validate_name("Python_master"))
# print(validate_name("Python_master_master"))

import re

# жадные (gredy)- захватывают максимально возможное число символов
# *, +?, ?? ленивые(lazy) - захватывают минимально возможное число символов
# {n,m}?, { , m}?, {n, }?

# text = '<body>Пример  жадного соответствия регулярных выражений</body>'
# # print(re.findall('<.*?>', text))
# print(re.search('<.*?>', text).group())

# s = '<p>Изображение <img src="bg.jpg">- фон страницы</p>'
# reg = r'<img[^>]*>'
# print((re.findall(reg, s)))

# s = 'jngrkerngktrnjgndfnxfhg  fjgrntujdr gjrbg[6]nrngrntgnt rgnrn[9]rngrengn rngmn[7][5]'
# reg = r'\[.*?]'
# print(re.findall(reg, s))


# s = 'Петр, Ольга и Виталий отлично учатся'
# reg = 'Петр|Ольга|Виталий'
# print(re.findall(reg, s))

# s = 'Word2016, PS6, AI5, qw'
# reg = r'[a-z]+\d*'
# print(re.findall(reg, s, re.IGNORECASE))

# s = '5 + 7*2 - 4'
# reg = '
# print(re.split(reg, s))


# s = input("Введите дату в формате dd-mm-YYYY: ")
# reg = r'([0-2][0-9]|[3][01])-([0][1-9]|[1][0-2])-([1][9][0-9][0-9]|[2][0][0-9][0-9])'
# # print(re.split(reg, s))
# print(re.findall(reg, s))


# 192.168.222.255
# s = '127.0.0.1'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s))

# s = 'Базовый JS. Продвинутый Python сложен. Базовый Python прост'
# # reg = r'[а-яё]+(?= Python)'
# # reg = r'Базовый(?! Python)'
# # reg = r'(?<=Базовый )\w{2,6}'
# reg = r'(?<!Продвинутый )Python'
# print(re.findall(reg, s, re.IGNORECASE))

# s = "КарлIV, КарлIX, КарлV, КарлVI, КарлVII, КарлVIII, ЛюдовикIX, ЛюдовикVI, ЛюдовикVII, ЛюдовикVIII, ЛюдовикX, ..., " \
#     "ЛюдовикXVIII, ФилиппI, ФилиппII, ФилиппIII, ФилиппIV, ФилиппV, ФилиппVI"
# reg = r'\w+(?<!Людовик)VI'
# print(re.findall(reg, s, re.IGNORECASE))

# s = '1X, Text ABC 123 A1B2C3'
# reg = r'(?<!\d)\d(?!\d)'
# print(re.findall(reg, s))
#
# s1 = "text from #START# till #END#"
# reg = r'(?<=#START#).*(?=#END#)'
# print(re.findall(reg, s1))
#
# s2 = "12_34__56"
# reg = r'\d+(?=_(?!_))'
# print(re.findall(reg, s2))

# s = 'Я ищу совпадения в 2021 году. И я их найду в 200000 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print('Строка: ', m[0])
# print('Цифра: ', m[1])
# print('Цифра: ', m[2])

# s = 'Самолет прилетает 10/23/2021. Будем вас рады видеть после 10/24/2021'
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# reg1 = r'\2.\1.\3'
# print(re.sub(reg, reg1, s))

# s = 'google.com and google.ru'
# reg = r'(([a-z0-9-_]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

# def is_roman_number(num):
#     pattern = r'^M{0,3}(CD|CM|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})$'
#     if re.search(pattern, num):
#         return True
#     return False
#
#
# print(is_roman_number('MMDCCLXXIII'))
# print(is_roman_number('CCCMMVIIVV'))
# print(is_roman_number('VI'))
# print(is_roman_number('VIC'))

# Рекурсия
# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("->", n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print((sum_list([1, 2, 3, 4, 8, 9])))

# def sum_list(lst):
#     if len(lst) == 1: # базовый случай
#         print(lst, '->lst[0]', lst[0])
#         return lst[0]
#     else:
#         print(lst, '->lst[0]', lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print((sum_list([1, 2, 3, 4, 8, 9])))

# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))


# print(type(names)==list)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
# print(len(names))
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
# names = ['Adam', ["Bob", ["chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]


# print(count_items(names))

# def count_items(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count


# print(count_items(names))

# names = ['Adam', ["Bob", ["chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def union(s):
#     if not s:  # s == []
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# print(union(names))

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == '\t' or text[0] == ',':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(' Hello, \tWorld, Hi '))

# s = [-2, 3, 8, -11, -4, 6]
#
#
# def count_minus(lst):
#     count = 0
#     if not lst:
#         return count
#     if lst[0] > 0:
#         return count_minus(lst[1:])
#     else:
#         count += 1
#     return count + count_minus(lst[1:])
#
#
# print(s)
# print('n =', count_minus(s))

# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))

# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# # print(binary_search(lst, 3))
# print(binary_search(lst, 8))


# import random as r
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [r.randint(1, 99) for i in range(10)]
# print(a)
# bubble(a)
# print(a)

# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#     i = j = 0
#     res = []
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
#
# array = [9, 5, 3, 8, 6]
# print(array)
# array = merge_sort(array)
# print(array)

# def shell_sort(s):
#     gap = len(s)
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#         gap //= 2
#     return s
#
#
# a = [10, 44, 26, 14, 67, 21, 9, 87]
# print(a)
# shell_sort(a)
# print(a)


# f = open(r"C:\Users\user\PycharmProjects\pythonProject1\Text.txt", "r")
# print(*f)
# print(f)
# print(f.closed)
# print(f.name)
# print(f.encoding)
# print(f.read(3))
# print(f.read())
# f.close()
# f = open("Text.txt", "r")
# try:
#     print(f.read())
# finally:
#     f.close()


# f = open('Test.txt', 'r')
# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# print(f.readlines())
#

# for line in f:
#     print(line)
# f.close()
# s = f.readlines()
# print(s)
# print(f'В документе {len(s)} строк')
# count = 0
# for line in f:
#     count += 1
# print(count)
# f.close()

# f = open('xyz.txt', 'w')
# f.write("Hello\nWorld!")
#
# f.close()

# f = open('xyz.txt', 'a')
# # print(f.write("New text!"))
# lst = [str(i)+str(i-1) for i in range(1, 20)]
# # lines = ['This is line 1', 'This is line 2']
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open('Тест.txt', 'r', encoding='utf-8')
# s = f.readlines()
# print(s)
# s[1] = 'Hello World!\n'
# print(s)
# f.close()
# f = open('Тест.txt', 'w', encoding='utf-8')
# f.writelines(s)
# f.close()

# f = open('text.txt', 'r+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# print(f.read(3))
# print(f.tell())  # 3
# print(f.seek(1)) # 1
# print(f.read())
# print(f.tell())
# f.close()

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789\nfggjgkkdls'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:5])

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)


# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print("done")


# with open(file_name, 'r') as f:
#     file_lst = f.read().split()
# file_lst = list(map(float, file_lst))
# print(file_lst)
# print(len(file_lst))

# def find_in_file(file_name):
#     max_l = 0
#     temp_res = []
#     res = []
#     c = 0
#     with open(file_name, "r", encoding='utf-8') as new_file:
#         temp_file = new_file.read().split()
#         for i in temp_file:
#             temp_res.append(len(i))
#             if len(i) > max_l:
#                 max_l = len(i)
#         for j in temp_res:
#             if j == max_l:
#                 res.append(temp_file[c])
#             c += 1
#     return res
#
#
# print(find_in_file("poisk.txt"))

# with open('poisk.txt', 'r', encoding='utf-8') as f:
#     lst = f.read().split()
#     print(lst)
#     m = max(len(i) for i in lst)
#     print(m)
#     print([i for i in lst if len(i) == m])


# text = 'Строка №1\nСтрока №1\nСтрока №1\nСтрока №1\nСтрока №1\nСтрока №1\nСтрока №1\nСтрока №1\nСтрока №1\nСтрока №1\n'
# with open('one.txt', 'w') as f:
#     f.write(text)
#
#
# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)
#
# with open(write_file, 'r') as fr:
#     for line in fr:
#         print(line, end="")


# os -модуль
# os.path

# import os

# print('Текущая директория', os.getcwd()) # возвращает текующую директорию(там где наш документ)
# print(os.listdir('..'))# возвращает список директорий и файлов, находящихся в текущей директории(по умолчанию) или в директории по указанному пути
# os.mkdir('folder') # создает директорию по указанному пути
# os.mkdir('folder1.folder2')
# os.makedirs('folder1/folder2/folder0/folder3/folder4/folder5') # создаст конечную директорию, и промежуточные папки

# os.remove('xyz.txt') # удаляет файл

# os.rename('folder', 'test') # переименовывает файл или директорию или папку
# os.rename('folder1/folder2/Tst.txt', 'ts.docx')
# os.renames('Text.txt', 'text/new_text/Tx.txt') # переименовываться и перемещаться создавая промежуточные дипектории


# os.rmdir('text') # удаляет пустую директорию(папку).Если папка не существует или ора не пустая -будет ошибка
# возвращает имена объектов в дереве папки, обходя это дерево сверху вниз(True)
# for root, dirs, files in os.walk('folder1', topdown=False):
#     print('Root:', root)
#     print('Subdirs:', dirs)
#     print('Files:', files)


# for root, dirs, files in os.walk("folder1", topdown=False):
#     if len(dirs) == 0 and len(files) == 0:
#         print("Deriktoriya " + root + " udalena")
#         os.rmdir(root)

# for root, dirs, files in os.walk("folder1", topdown=False):
#     if not os.listdir(root):
#         os.rmdir(root)
#         print(f'Директория {root} удалена')

# import os
#
# print(os.path.normcase('c:/User/admin/Documents'))
#
# print(os.path.relpath(r'C:\Users\user\PycharmProjects\pythonProject1\two.txt'))
# print(os.path.isfile(r'C:\Users\user\PycharmProjects\pythonProject1\two.txt'))# возвращает TRUE если концом пути является существующий файл
# print(os.path.isdir(r'C:\Users\user\PycharmProjects\pythonProject1'))# возвращает TRUE если концом пути является существующий папка
#
#
# dir_name = "folder1"
#
# objs = os.listdir(dir_name)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f'{obj}- file- {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{obj}- dir')


# print('Hello')
# elif os.path.isfile(path) and os.path.getsize(path) == 0:
#     # os.mkdir('empty_file')
#     path1 = os.getcwd()
#     path2 = 'empty_file'
#     os.renames(path1, path2)
#     path3 = os.getcwd()
#     print(f'файл {f} со старым адресом {path1} перемещен по адресу {path3}')



