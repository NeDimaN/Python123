import math


class Sphere:

    def __init__(self, r, x, y, z):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (self.r ** 3) * math.pi * 4 / 3

    def get_square(self):
        return (self.r ** 2) * math.pi * 4

    def get_radius(self):
        return self.r

    def get_centre(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_centre(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if ((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2) <= self.r ** 2:
            return True
        else:
            return False


s1 = Sphere(0.6, 0, 0, 0)
print(f'Объем шара: {s1.get_volume()}')
print(f'Площадь внешней поверхности: {s1.get_square()}')
print(f'Радиус сферы: {s1.get_radius()}')
print(f'Координаты центра сферы: {s1.get_centre()}')
print(f'Нахождение точки внутри сферы: {s1.is_point_inside(0, -1.5, 0)}')
s1.set_radius(1.6)
print(f'Изменение радиуса сферы:{s1.get_radius()}')
s1.set_centre(0, -1.5, 0)
print(f'Изменение координаты центра сферы:{s1.get_centre()}')
print(f'Нахождение точки внутри сферы: {s1.is_point_inside(0, -1.5, 0)}')
