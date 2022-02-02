import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circle_square(self):
        return math.pi * self.radius ** 2

    def get_circle_length(self):
        return 2 * math.pi * self.radius

    def print_circle(self):
        print(f'Радиус : {self.radius}')

    def print_circle_square(self):
        print(f'Длина окружности: {round(self.get_circle_square(), 2)}')

    def print_circle_length(self):
        print(f'Площадь круга: {round(self.get_circle_length(), 2)}')
