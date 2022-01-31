class Person:
    def __init__(self, surname, forename, old):
        self.__surname = surname
        self.__forename = forename
        self.__old = old


class Sort:
    def __init__(self, list_name):
        self.__list_name = list_name

    def __call__(self, *args, **kwargs):
        if len(args) == 1 and args[0] == 'surname':
            return sorted(self.__list_name, key=)

        elif len(args) == 2 and args[0] == 'surname' and args[1] == 'forename':
            return sorted(self.__list_name,key=)


p = [Person('Иванов', 'Игорь', '28'),
     Person('Петров', 'Степан', '21'),
     Person('Сидоров', 'Антон', '25'),
     Person('Петров', 'Анатолий', '11'),
     Person('Иванов', 'Иван', '28')
     ]

SortKey = Sort(p)
print(SortKey('surname'))
