class Book:
    name = 'name'
    year = '0000'
    publisher = 'publisher'
    type = 'type'
    author = 'author'
    price = '00000000'

    def print_info(self):
        print(' Информация о книге '.center(40, '*'))
        print(f'Название: {self.name}\nГод выпуска: {self.year}\nИздательство: {self.publisher}\nЖанр: {self.type}')
        print(f'Автор: {self.author}\nЦена: {self.price}')
        print('=' * 40)

    def input_info(self, name_book, year_book, pub_book, t_book, au_book, pr_book):
        self.name = name_book
        self.year = year_book
        self.publisher = pub_book
        self.type = t_book
        self.author = au_book
        self.price = pr_book

    def set_name(self, name_book):
        self.name = name_book

    def get_name(self):
        return self.name

    def set_year(self, year_book):
        self.year = year_book

    def get_year(self):
        return self.year

    def set_publisher(self, pub_book):
        self.publisher = pub_book

    def get_publisher(self):
        return self.publisher

    def set_type(self, t_book):
        self.type = t_book

    def get_type(self):
        return self.type

    def set_author(self, au_book):
        self.author = au_book

    def get_author(self):
        return self.author

    def set_price(self, pr_book):
        self.price = pr_book

    def get_price(self):
        return self.price


b1 = Book()
b1.print_info()
b1.input_info('Расстрелять!', '2011', 'Инапресс', 'Современная русская литература', 'Александр Покровский', '453 рубля')
b1.print_info()
b1.set_name('Расстрелять!(Сборник)')
b1.set_year('2020')
b1.set_publisher('ВоеннИздат')
b1.set_type('Армия.Флот.Юмор')
b1.set_author('Покровский Александр Михайлович')
b1.set_price('502 рубля')
b1.print_info()
