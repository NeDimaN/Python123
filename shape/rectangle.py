class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_rect_perimeter(self):
        return (self.a + self.b) * 2

    def print_rect(self):
        print(f'Периметр: {self.get_rect_perimeter()}')

    def print_rect_info(self):
        print(f'Стороны: {self.a},{self.b}')


