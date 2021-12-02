from math import *


def figure_type(name, **kwargs):
    if name == 'rhombus':
        res_area = kwargs['d1'] * kwargs['d2'] / 2
    elif name == 'square':
        res_area = kwargs['a'] ** 2
    elif name == 'trapezoid':
        res_area = (kwargs['a'] + kwargs['b']) * kwargs['h'] / 2
    elif name == 'circle':
        res_area = kwargs['r'] ** 2 * pi
    else:
        res_area = 'invalid data'

    return res_area


print(figure_type('rhombus', d1=10, d2=8))
print(figure_type('square', a=5))
print(figure_type('trapezoid', a=12, b=3, h=6))
print(figure_type('circle', r=18))
print(figure_type('unknown', a=1, b=2, c=3))
