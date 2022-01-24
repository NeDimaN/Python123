class Clock:
    __DAY = 86400  # 24*60*60- число секунд в одном дне

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError('Секунды должны быть целым числом')

        self.__secs = secs % self.__DAY

    def get_format_time(self):
        s = self.__secs % 60  # секунды
        m = (self.__secs // 60) % 60  # минуты
        h = (self.__secs // 3600) % 24  # часы
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return self.__secs > other.__secs

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return self.__secs < other.__secs

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return self.__secs >= other.__secs

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return self.__secs <= other.__secs


c1 = Clock(200)
c2 = Clock(200)
c3 = Clock(1200)


print('c3 > c1', c3 > c1)
print('c3 >= c1', c3 >= c1)
print('c3 < c1', c3 < c1)
print('c3 <= c1', c3 <= c1)
