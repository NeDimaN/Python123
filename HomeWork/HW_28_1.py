class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname  # имя владельца
        self.__num = num  # номер счета
        self.__percent = percent  # процент начисления
        self.__value = value  # сумма в рублях
        print(f'Счет #{self.__num} принадлежащий {self.__surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):  # редактирование рубля по отношению к доллару
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):  # редактирование рубля по отношению к евро
        cls.rate_euro = rate

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent):
        self.__percent = percent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    def add_percents(self):  # начисление процентов
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, val):  # снятие заданной суммы
        if val > self.__value:
            print(f'к сожалению у вас нет {val} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} ,было успешно снято')
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} ,было успешно добавлено!')
        self.print_balance()

    def convert_to_usd(self):  # перевод в доллары
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')

    def convert_to_eur(self):  # перевод в евро
        eur_val = Account.convert(self.__value, Account.rate_euro)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')

    def print_balance(self):
        print(f'Текущий баланс {self.__value} {Account.suffix}')

    def print_info(self):  # метод вывода информации о счете
        print('Информация о счете')
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Процент {self.__percent: .0%}')
        print('-' * 20)


acc = Account('Пушкин', 12345, 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()

Account.set_usd_rate(2)
Account.set_eur_rate(3)
print()
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.surname = 'Дантес'
acc.num = 6666
acc.percent = 0.05
acc.value = 2000
acc.print_info()

acc.add_percents()
print()
acc.withdraw_money(3000)
print()
acc.withdraw_money(100)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)
print()
