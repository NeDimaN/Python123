# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # print(type(p1))
# # print(type(p1) == Point)
# # print(isinstance(p1, Point))
# # p1.x = 5
# # p1.y = 10
# p1.set_coords(5, 10)
# print(p1.__dict__)
# Point.set_coords(p1, 25, 36)
# print(p1.__dict__)
# p2 = Point()
# p2.set_coords(4, 6)

# # p1.z = 28
# # print(getattr(p1, 'z', 'False'))
# # print(getattr(p1, 'x'))
# setattr(p1, 'z', 7)
# print(hasattr(p1, 'z'))
# print(hasattr(p1, 'x'))
# delattr(p1, 'z')
# p2 = Point()
# print(p2.__dict__)
# print(p1.__dict__)

# print(p2.x, p2.y)

# print(p1.__dict__)
# print(p1.x, p1.y, Point.x)
# p1.x = 5
# p1.y = 10
# print(p1.x, p1.y, Point.x)
# print(getattr(p1, 'x'))
# print(p1.__dict__)
# print(Point.__dict__)
# Point.x = 100
# print(p1.x, p1.y)
# print(id(p1))
# print(id(Point))

# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     city = 'city'
#     country = 'country'
#     address = 'Street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}')
#         print(f'Город: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # метод устанавливает имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '27.09.1978', '30-44-13', 'Россия', 'Москва', 'Чистопольский бульвар,14')
# h1.print_info()
# h1.set_name('Ольга')
# h1.print_info()
# print(h1.get_name())
# h1.set_birthday('12.06.2021')
# print(h1.get_birthday())
# h1.print_info()


# class Car:
#     name = 'name'
#     year = '0000'
#     product = 'product'
#     energy = '000 л.с.'
#     color = 'color'
#     price = '00000000'
#
#     def print_info(self):
#         print(' Данные автомобиля'.center(40, '*'))
#         print(
#             f'Название модели: {self.name}\nГод выпуска: {self.year}\nПроизводитель: {self.product}\nМощность двигателя: {self.energy}')
#         print(f'Цвет машины: {self.color}\nЦена: {self.price}')
#         print('=' * 40)
#
#     def input_info(self, name, year, product, energy, color, price):
#         self.name = name
#         self.year = year
#         self.product = product
#         self.energy = energy
#         self.color = color
#         self.price = price
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#
# c1 = Car()
# c1.print_info()
# c1.input_info('Веста', '2018', 'Автоваз', '107', 'Белый', '785000')
# c1.print_info()
# c1.set_color("Красный")
# print(c1.get_color())
# c1.print_info()


# class Person:
#     skill = 10  # переменная для квалификации
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f'Данные сотрудника : {self.name} {self.surname}')
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалификация сотрудника {self.name}: {self.skill}" )
#
#
# p1 = Person()
# p1.print_info('Виктор', "Резник")
# p1.add_skill(3)
# p2 = Person()
# p2.print_info('Анна', 'Долгих')


# def sum_arg(a, b):
#     print(a + b)
#
#
# sum_arg(5, 2)
# sum_arg('Hello', ' world')


# __магический метод__


# Специальные методы
# Конструктор  __new__
# инициализатор  __init__
# деструктор __del__

# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print("Конструктор")
#     #     return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print('Инициализатор')
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)


# class Point:
#
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
#
# p1 = Point(5, 10)
# print(p1._x, p1._y)
# p1._x = 100
# p1._y = 'abc'
# print(p1._x, p1._y)

# Инкапсуляция
# x- public
# _x - режим доступа protected
# __x- private
# import math
#
#
# class Rectangle:
#     def __init__(self, length = 1, width = 1):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def square(self):
#         return self.__length * self.__width
#
#     def perimetr(self):
#         return (self.__length * self.__width) * 2
#
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#
# rec1 = Rectangle()
# rec1.set_length(3)
# rec1.set_width(9)
# print(f'Длина прямоугольника {rec1.get_length()}')
# print(f'Ширина прямоугольника {rec1.get_width()}')
# print(f'Площадь {rec1.square()}')
# print(f'Периметр {rec1.perimetr()}')
# print(f'Гипотенуза{rec1.hypo()}')

# import math
#
#
# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def square(self):
#         return self.__length * self.__width
#
#     def perimetr(self):
#         return (self.__length * self.__width) * 2
#
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#     def get_draw(self):
#         # for i in range(self.__length):
#         #     print(self.__width * "*")
#         print((self.__width * "*" + "\n") * self.__length)
#
#
# rec1 = Rectangle()
# rec1.set_length(3)
# rec1.set_width(9)
# print('Длина прямоугольника', rec1.get_length())
# print('Ширина прямоугольника', rec1.get_width())
# print('Площадь', rec1.square())
# print('Периметр', rec1.perimetr())
# print('Гипотенуза', round(rec1.hypo(), 2))
# rec1.get_draw()

# class Point:
#     WIDTH = 5
#     z = 100
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y


# def __getattr__(self, name):
#     return f"В классе {__class__.__name__} отсутствует атрибут: {name}"
# def __getattribute__(self, item):
#     if item == '_Point__x':
#         return 'Закрытая переменная'
#     else:
#         return object.__getattribute__(self, item)

#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError
#         else:
#             self.__dict__[key] = value
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.check_val(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.check_val(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
#     def area(self):
#         return (self.__x * self.__y) + self.z
#
#
# p1 = Point(5, 10)
# print(p1.__x)
# print(p1._Point__x)
# print(p1.get_coords())
# p1.set_coords(2, 3)
# print(p1.get_coords())
# p1.z = 100
# Point.WIDTH = 10
# print(p1.area())

# class Point:
#     __slots__ = ['__x', '__y', 'z']
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         else:
#             return False
#
#     def __set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError('Неверный формат данных')
#
#     def __get_coords_x(self):
#         print('Вызов _get_coords_x')
#         return self.__x
#
#     def __del_coords_x(self):
#         print('Удаление свойства')
#         del self.__x
#
#     coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# # p1.coordX = 100
# # print(p1.coordX)
# del p1.coordX
# p1.coordX = 7
# print(p1.coordX)

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         else:
#             return False
#
#     @property # геттер
#     def coords_x(self):
#         print('Вызов _get_coords_x')
#         return self.__x
#
#     @coords_x.setter
#     def coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError('Неверный формат данных')
#
#     @coords_x.deleter
#     def coords_x(self):
#         print('Удаление свойства')
#         del self.__x
#
#     # coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coords_x = 100
# print(p1.coords_x)
# # del p1.coordX
# # p1.coordX = 7
# # print(p1.coordX)
# print(p1.__dict__)

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))
# q = Change()
# print(q.dec(5), q.inc(5))


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         if a > b and a > c and a > d:
#             return a
#         elif b > a and b > c and b > d:
#             return b
#         elif c > a and c > b and c > d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a < b and a < c and a < d:
#             return a
#         elif b < a and b < c and b < d:
#             return b
#         elif c < a and c < b and c < d:
#             return c
#         else:
#             return d
#
#     @staticmethod
#     def avarege(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factor(a):
#         fac = 1
#         for i in range(1, a + 1):
#             fac *= i
#         return fac
#
#
# print(Numbers.max(1, 5, 9, 7))
# print(Numbers.min(1, 5, 9, 7))
# print(Numbers.avarege(1, 5, 9, 7))
# print(Numbers.factor(4))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_bd(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# # d = "16.12.2021"
# #
# # day, month, year = map(int, d.split('.'))
# # print(day, month, year)
#
# dates = [
#     '30.12.2021',
#     '30-12-2020',
#     '01.11.2014',
#     '12.31.2010'
# ]
#
# for d in dates:
#     if Date.is_date_valid(d):
#         date = Date.from_string(d)
#         db = date.string_to_bd()
#         print(db)
#     else:
#         print('Неправильный формат с датой')
#
# d = Date()
# date = d.from_string('16.12.2021')
# print(date.string_to_bd())
#
# d1 = Date()
# date1 = d1.from_string('03.12.2021')
# print(date1.string_to_bd())
# date2 = Date.from_string('25.12.2021')
# print(date2.string_to_bd())


# class Area:
#     count = 0
#
#     @staticmethod
#     def geron1(a, b, c):
#         Area.count += 1
#         perimetr = (a + b + c) / 2
#         return (perimetr * (perimetr - a) * (perimetr - b) * (perimetr - c)) ** 0.5
#
#     @staticmethod
#     def treangle(a, h):
#         return 0.5 * h * a
#
#
# print(Area.geron1(3, 4, 5))
# print(Area.treangle(6, 7))
# a1 = Area()
# print(a1.geron1(2, 6, 7))
# print(Area.count)


# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname  # имя владельца
#         self.num = num  # номер счета
#         self.percent = percent  # процент начисления
#         self.value = value  # сумма в рублях
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):  # редактирование рубля по отношению к доллару
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):  # редактирование рубля по отношению к евро
#         cls.rate_euro = rate
#
#     def add_percents(self):  # начисление процентов
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):# снятие заданной суммы
#         if val > self.value:
#             print(f'к сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} ,было успешно снято')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} ,было успешно добавлено!')
#         self.print_balance()
#
#     def edit_owner(self, surname):  # смена владельца счета
#         self.surname = surname
#
#     def convert_to_usd(self):  # перевод в доллары
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):  # перевод в евро
#         eur_val = Account.convert(self.value, Account.rate_euro)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):  # метод вывода информации о счете
#         print('Информация о счете')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Процент {self.percent: .0%}')
#         print('-' * 20)
#
#
# acc = Account('Ненашев', 12345, 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
#
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'{self.x}, {self.y}'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         print('Инициализатор базового класса Prop')
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print('Переопределенный инициализатор Line')
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         self.__width = 5
#     # def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#     #     self.sp = sp
#     #     self.ep = ep
#     #     self.color = color
#     #     self.width = width
#
#     def draw_line(self):
#         print(f'Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.get_width()}')
#
#
# class Rect(Prop):
#     # def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#     #     self.sp = sp
#     #     self.ep = ep
#     #     self.color = color
#     #     self.width = width
#
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self.sp}, {self.ep}, {self.color}, {self.get_width()}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# print(line.__dict__)

# line.width = 10
# print(line.width)
# line.draw_line()
# rect = Rect(Point(30, 40), Point(7, 86))
# rect.draw_rect()

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('Значение ширины должно быть больше 0!')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError('Значение высоты должно быть больше 0!')
#
#     def border_new(self, b):
#         self.border = b
#
#     def area(self):
#         return self.__width * self.__height
#         # return self.border_new('1px solid gray')
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.area())

# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         self.verify_old(old)
#
#         self.__fio = fio
#         self.__old = old
#         self.__ps = ps
#         self.__weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()  # ['Фамилия','Имя','Отчество']
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))  # ФамилияИмяОтчество
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефисы!')
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 100 лет')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#
# p1 = UserDate('Орлов Дмитрий Николаевич', 35, '1234 567890', 90.9)
# p1.fio = "Соколов Александр Викторович"
# print(p1.__dict__)
# ______________________________________________________


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def __set_one_coords(self, sp):
#         if sp.is_int():
#             self._sp = sp
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def __set_two_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             self.__set_one_coords(sp)
#         else:
#             self.__set_two_coords(sp, ep)
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-10, -20))
# line.draw_line()
# ==========================================================

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self): # абстрактный метод
#         raise NotImplementedError('В дочернем классе должен быть определен метод draw')
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

# ==========================================================


# абстрактный класс
# class Chess(ABC):
#     def draw(self):
#         print('Нарисовал шахматную фигуру')
#
#     @abstractmethod
#     def move(self):  # абстрактный метод
#         print('Метод move() в базовом')
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print('Ферзь перемещен на e2e4')
#
#
# q = Queen()
# q.draw()
# q.move()
# from math import pi
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def set_radius(self, radius):
#         self._radius = radius
#
#     def set_sides(self, width=None, length=None ):
#         if length is None:
#             self._width = self._length = width
#         else:
#             self._width = width
#             self._length = length
#     def calc_area(self):
#         raise NotImplementedError('В дочернем классе должен быть определен метод calc_area')
#
# class Sq_table(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class Round_table(Table):
#     def calc_area(self):
#         return pi * self._radius ** 2
#
#
# t = Sq_table(20, 10)
# t.set_sides(2)
# print(t.__dict__)
# print(t.calc_area())
# t1 = Round_table(radius=10)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = Round_table(radius=20)
# t2.set_radius(60)
# print(t2.__dict__)
# print(t2.calc_area())
# ===================================

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_eur = 90.14
#     suffix = 'EURO'
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_eur
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print('*' * 50)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
# print('*'* 50)
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')

# ==================================================

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Child Class')
#         print("Display 1 Abstract Method")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('GrandChild Class')
#         print("Display 2 Abstract Method")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# ===========================


# class Geeksforgeeks:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Это внешний класс')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass
#
#         def show(self):
#             print('Это вложенный класс')
#
#         class InnerClass:
#             def show(self):
#                 print('Это класс вложенный во внутрь вложенного')
#
#
# outer = Geeksforgeeks()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
# inner2 = outer.inner1.inner_inner
# inner2.show()
# ==================================================

# class OS:
#     def system(self):
#         return 'Windows 10'
#
#
# class CPU:
#     def make(self):
#         return 'Intel'
#
#     def model(self):
#         return 'Core-i7'

# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i7'
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
#
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In base class")
#
#     class Inner:
#         def display1(self):
#             print('Inner of base class')


# class SubClass(Base):
#     def __init__(self):
#         print('In Subclass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#
#         def display2(self):
#             print('Inner of Subclass')


# a = Base()
# a.display()
# b = a.db
# b.display1()

# a = SubClass()
# a.display()

# b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()


# ===============================================


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is braking')
#
#
# b = Dog('Baggi')
# b.bark()
# b.play()
# b.sleep()
# ===========================================

# class A:
#     # def __init__(self):
#     #     print('Инициализатор класса А')
#     def hi(self):
#         print('A')
#
# class B(A):
#     def hi(self):
#         print('B')
#
#     # def __init__(self):
#     #     print('Инициализатор класса B')
#
#
# class C(A):
#     def hi(self):
#         print('C')
#
#     # def __init__(self):
#     #     print('Инициализатор класса C')
#
#
# class D(B, C):
#     pass
#
#     # def __init__(self):
#     #     print('Инициализатор класса D')
#
#
# d = D()
# d.hi()
# print(D.mro())
# ==================================================

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}), ({self.y})'
#
#
# class Styles:
#     def __init__(self, color='red', width=1):
#         print('Инициализатор Styles')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         Styles.__init__(self, *args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# ============================================================


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclass.txt')
#
#
# sub = MySubClass()
# sub.display('Это строка будет отображаться и записываться в файл')

# ==================================================================
# Миксины/примеси
# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print('Init Goods')
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name},{self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Это Init MixinLog')
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар был продан 00:00 часов')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# print(NoteBook.mro())
# n2 = NoteBook('HP', 1.5, 35000)
# n2.save_sell_log()

# ============================================

# Перегрузка операторов

# class Clock:
#     __DAY = 86400  # 24*60*60- число секунд в одном дне
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError('Секунды должны быть целым числом')
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # секунды
#         m = (self.__secs // 60) % 60  # минуты
#         h = (self.__secs // 3600) % 24  # часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.__secs + other.__secs)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.__secs - other.__secs)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.__secs * other.__secs)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.__secs // other.__secs)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.__secs % other.__secs)
#
#     def __eq__(self, other):
#         return self.__secs == other.__secs
#
#     # if self.__secs == other.__secs:
#     #     return True
#     # return False
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#
# c1 = Clock(200)
# c2 = Clock(200)
# c3 = Clock(1200)
# print(c2.get_format_time())
# print(c1.get_format_time())
# print(c3.get_format_time())
# print(c3 > c1)


# if c1 == c2:
#     print('Время одинаковое')
# if c1 != c3:
#     print('Время разное')

# ================================20.01.2022

# ================================25.01.2022


# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f'{self.last_name} {self.first_name} {self.age}')
#
#
# class Student(Human):
#     def __init__(self, spec, group, rating, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.spec = spec
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         print(f'{self.spec} {self.group} {self.rating}', end=' ')
#         super().info()
#
#
# class Teacher(Human):
#     def __init__(self, spec, experience, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.spec = spec
#         self.experience = experience
#
#     def info(self):
#         print(f'{self.spec} {self.experience}', end=' ')
#         super().info()
#
#
# class Graduate(Student):
#     def __init__(self, topic, spec, group, rating, last_name, first_name, age):
#         super().__init__(spec, group, rating, last_name, first_name, age)
#         self.topic = topic
#
#     def info(self):
#         print(f'{self.topic}', end=' ')
#         super().info()
#
#
# group = [
#     Student('Батодалаев', 'Даши', 16, 'ГК', 'Web_011', 5),
#     Graduate('Шугани', 'Сергей', 15, 'РПО', 'PD_011', 5, 'Защита персональных данных'),
#     Teacher('Башкиров', 'Алексей', 45, 'Разработка приложений', 20)
#
# ]
# for i in group:
#     i.info()

# ==================================================

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __str__(self):
#         return f'{self.__coords}'
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
#
# p = Point(6, -9, 8)
# print(len(p))
# print(p.__dict__)
# print(abs(p))
# print(p)

# =======================================================

# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(5, 9)
# print(p.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
#
# print('pt =', pt.__sizeof__())
# print('pt2 =', pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt3 = Point3D(10, 20, 30)
#
# # print(pt3.__dict__)
# print(pt3.x, pt3.y, pt3.z)

# ==================================

# Функторы

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#         return self.__counter
#
#
# c1 = Counter()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c2()

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, s):
#         if not isinstance(s, str):
#             raise ValueError('Аргумент должен быть строкой')
#         return s.strip(self.__chars)
#
#
# s1 = StripChars('&:!?.; ')
# print(s1(' ?Hello . World! Hi!, '))
#
#
# def strip_string(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError('Аргумент должен быть строкой')
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = strip_string('&:!?.; ')
# print(s1(' ?Hello . World! Hi!, '))

# =====================================

# p = [Person('Иванов', 'Игорь', 28), Person('')]

# ================================================

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('перед вызовом функции')
#         self.func()
#         print('после вызова функции')
#
#
# @MyDecorator
# def function():
#     print('func')
#
#
# function()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#
#         print('перед вызовом функции')
#         res = self.func(a, b)
#         print('после вызова функции')
#         return res
#
#
# @MyDecorator
# def function(a, b):
#
#     return a * b
#
#
# print(function(2, 5))

# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = self.func(a, b)
#         return res**2
#
#
# @Power
# def function(a, b):
#     return a * b
#
#
# print(function(2, 3))

#
# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print('перед вызовом функции')
#             print(self.name)
#             func(a, b)
#             print('после вызова функции')
#
#         return wrap
#
#
# @MyDecorator('test2')
# def function(a, b):
#     print(a, b)
#
#
# print(function(2, 5))


# ======================================27.01.2022
#
# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             res = func(a, b)
#             return res ** self.arg
#
#         return wrap
#
#
# @Power(3)
# def multuple(a, b):
#     return a * b
#
#
# print('Результат:', multuple(2, 2))

# =======================================
#
# def dec(fn):
#     def wrap(*args, **kwargs):
#         print('*' * 20)
#         fn(*args, **kwargs)
#         print('*' * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     # def dec(fn):
#     #     def wrap(*args, **kwargs):
#     #         print('*' * 20)
#     #         fn(*args, **kwargs)
#     #         print('*' * 20)
#     #
#     #     return wrap
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person('Дима', 'Орлов')
# p1.info()
# ===================================================
#
# def decorator(cls):
#     class Wrap(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrap
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print('Init ActualClass')
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
#
# print(obj.quad(4))
# print(obj.doubler(4))

# =====================================
#
# class Message:
#     _REGISTERY = {}
#
#     def __init__(self, text):
#         self.text = text
#
#     @classmethod
#     def register(cls, name):
#         def decorator(klass):
#             cls._REGISTERY[name] = klass
#             return klass
#
#         return decorator
#
#     @classmethod
#     def create(cls, message_type, text):
#         klass = cls._REGISTERY.get(message_type)
#         if klass is None:
#             raise ValueError('Такого мессенджера нет ')
#         print(text, end=' ')
#         return klass(text)
#
#
# @Message.register('Telegram')
# class TelegramMessage(Message):
#     def sent(self):
#         print('(Telegram)')
#
#
# @Message.register('WhatsApp')
# class WhatsAppMessage(Message):
#     def sent(self):
#         print('(WhatsApp)')
#
# @Message.register('Viber')
# class ViberMessage(Message):
#     def sent(self):
#         print('(Viber)')
#
#
# m1 = Message.create('Telegram', 'text')
# m1.sent()
# m2 = Message.create('WhatsApp', 'new text')
# m2.sent()
# m3 = Message.create('Viber', 'new text2')
# m3.sent()
# ==================================================
# Дискриптор

# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, value):
#         self.__surname = value
#
#
# p = Person('Дмитрий', 'Орлов')

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)

# @property
# def name(self):
#     return self.__name
#
# @name.setter
# def name(self, value):
#     self.__name = value
#
# @property
# def surname(self):
#     return self.__surname
#
# @surname.setter
# def surname(self, value):
#     self.__surname = value


# p = Person('Дмитрий', 'Орлов')
# print(p.name.get())
# p.name.set('Александр')
# print(p.name.get())
# ======================================
# Дискриптор это класс в котором определены магические методы
# __get__()
# __set__()
# __delete__()
# __set_name__()
#
# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person('Дмитрий', 'Орлов')
# print(p.name)
# print(p.surname)
# p.name = 'Александр'
# print(p.name)

# =======================================
# data descriptor -дескриптор данных
# Non-data descriptor - дескриптор неданных (только метод __get__)
#
# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Значение должно быть положительным')
#         instance.__dict__[self.__name] = value
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())

# =============================================


# Метаклассы


# a = 5
# print(type(a))
# print(type(int))
#
# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())

# Mylist = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
# ================================================ 01.02.2022

# Создание модулей

# import math
# from math import pi
#
# print(math.pi)
# print(pi)

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c

# from geometry import rect, sq, trian
#
#
# # from geometry import *
# def main():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#     shape = [r1, r2, s1, s2, t1, t2]
#     for i in shape:
#         print(i.get_perimetr())
#
#
# if __name__ == '__main__':
#     main()






