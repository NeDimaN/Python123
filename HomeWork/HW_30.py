from abc import ABC, abstractmethod
import math


class Root(ABC):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @abstractmethod
    def decision(self):
        pass

    def print_x(self):
        print('The root of ', end='')


class Line(Root):

    def decision(self):
        x = -self.b / self.a
        return x

    def print_x(self):
        super().print_x()
        print(f' \'{self.a}x + {self.b} = 0\' is: ', end='')


class Square(Root):

    def decision(self):
        disc = self.b ** 2 - (4 * self.a * self.c)
        if disc > 0:
            x1 = (-self.b + math.sqrt(disc)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(disc)) / (2 * self.a)
            return x1, x2
        elif disc == 0:
            x = -self.b / (2 * self.a)
            return x
        else:
            return 'корней нет'

    def print_x(self):
        super().print_x()
        print(f' \'{self.a}x^2{self.b}x{self.c} = 0\' are: ', end='')


l1 = Line(3, 7, 0)
l1.print_x()
print(f'{l1.decision():.2f}')
s = Square(1, -2, -3)
s.print_x()
print(" ".join(map(str, s.decision())))
