import math

from shape import circle, rectangle


class Cylinder(circle.Circle, rectangle.Rectangle):
    def __init__(self, radius, h):
        super().__init__(radius)
        self.h = h

    def get_volume(self):
        return math.pi * self.radius ** 2 * self.h

    def print_cylinder_square(self):
        return circle.Circle.get_circle_square(self)

    def print_cylinder(self):
        print(f'Площадь круга: {round(self.print_cylinder_square(), 2)}\nОбъем: {round(self.get_volume(), 2)}')



