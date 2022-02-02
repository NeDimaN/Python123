class Person:
    def __init__(self, surname, name, old):
        self.surname = surname
        self.name = name
        self.old = old

    @property
    def data(self):
        return self.surname, self.name, self.old

    def __str__(self):
        return f'{self.surname}, {self.name}, {self.old}'


class SortKey:
    def __init__(self, *args):
        self.__list_name = args

    def __call__(self, lst):
        lst.sort(key=lambda j: [j.__dict__[key] for key in self.__list_name])


p1 = [Person('Иванов', 'Игорь', '28'),
      Person('Петров', 'Степан', '21'),
      Person('Сидоров', 'Антон', '25'),
      Person('Петров', 'Анатолий', '11'),
      Person('Иванов', 'Иван', '28')
      ]

for i in p1:
    print(i.data)
print()

s1 = SortKey('surname')
s1(p1)
for i in p1:
    print(i.data)
print()
s2 = SortKey('surname', 'name')
s2(p1)
for i in p1:
    print(i.data)


