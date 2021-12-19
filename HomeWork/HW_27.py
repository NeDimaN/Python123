class Grad:
    count = 0

    @staticmethod
    def cels(x):
        Grad.count += 1
        return (x - 32) / 1.8
    @staticmethod
    def farengeit(y):
        Grad.count += 1
        return y * 1.8 + 32


print(f'Перевод Фаренгейты в Цельсии: {Grad.cels(100)}')
print(f'Перевод Цельсии в Фаренгейты: {Grad.farengeit(25)}')
print(Grad.count)
