from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def draw_shape(self):
        pass

    @abstractmethod
    def out_info(self):
        pass


class Square(Shape):
    def __init__(self, a, color):
        self.a = a
        super().__init__(color)

    def perimeter(self):
        return self.a * 4

    def square(self):
        return self.a * self.a

    def draw_shape(self):
        return ('*' * self.a + '\n') * self.a

    def out_info(self):
        print(
            f'===Квадрат===\nСторона:{self.a}\nЦвет:{self.color}\nПлощадь:{self.square()}\nПериметр:{self.perimeter()}\n'
            f'{self.draw_shape()}')


class Rectangle(Shape):
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        super().__init__(color)

    def perimeter(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b

    def draw_shape(self):
        return ('*' * self.b + '\n') * self.a

    def out_info(self):
        print(f'===Квадрат===\nДлина:{self.a}\nШирина:{self.b}\nЦвет:{self.color}\nПлощадь:{self.square()}\n'
              f'Периметр:{self.perimeter()}\n{self.draw_shape()}')


class Triangle(Shape):
    def __init__(self, a, b, c, color):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(color)

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = (self.a + self.b + self.c) / 2
        return round(((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5), 2)

    def draw_shape(self):
        for i in range(self.b):
            print(' ' * (self.a // 2 - i) + '*' * i + '*' + '*' * i + '\n', end='')

    def out_info(self):
        print(f'===Треугольник===\nСторона 1:{self.a}\nСторона 2:{self.b}\nСторона 3:{self.c}\nЦвет:{self.color}\n'
              f'Площадь:{self.square()}\n'
              f'Периметр:{self.perimeter()}\n', end='')
        self.draw_shape()


figure = [Square(3, 'black'),
          Rectangle(3, 7, 'Pink'),
          Triangle(11, 6, 6, 'yellow')
          ]

for i in figure:
    i.out_info()
