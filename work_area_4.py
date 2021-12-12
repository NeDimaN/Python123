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