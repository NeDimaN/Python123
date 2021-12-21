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
#         print(f'Счет #{num} принадлежащий {surname} был открыт.')
#         print('*' * 50)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):  # перевод в доллары
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
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


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        print('Инициализатор базового класса Prop')
        self.sp = sp
        self.ep = ep
        self.color = color
        self.__width = width

    def get_width(self):
        return self.__width


class Line(Prop):
    def __init__(self, *args):
        print('Переопределенный инициализатор Line')
        # Prop.__init__(self, *args)
        super().__init__(*args)
        self.__width = 5
    # def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
    #     self.sp = sp
    #     self.ep = ep
    #     self.color = color
    #     self.width = width

    def draw_line(self):
        print(f'Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.get_width()}')


class Rect(Prop):
    # def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
    #     self.sp = sp
    #     self.ep = ep
    #     self.color = color
    #     self.width = width

    def draw_rect(self):
        print(f'Рисование прямоугольника: {self.sp}, {self.ep}, {self.color}, {self.get_width()}')


line = Line(Point(1, 2), Point(10, 20))
line.draw_line()
print(line.__dict__)

# line.width = 10
# print(line.width)
# line.draw_line()
# rect = Rect(Point(30, 40), Point(7, 86))
# rect.draw_rect()
