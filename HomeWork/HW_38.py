import json

data = {}


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f'{self.country}: {self.capital}'

    @classmethod
    def remove_dict(cls, old_value, new_value, filename):
        try:
            data1 = json.load(open(filename))
        except FileNotFoundError:
            data1 = {}

        data1[old_value] = new_value
        with open(filename, 'w') as f:
            json.dump(data1, f, indent=3, ensure_ascii=False)

    @classmethod
    def search_data(cls, country, filename):
        try:
            data1 = json.load(open(filename))
        except FileNotFoundError:
            data1 = {}

        if country in data1:
            print(f'Страна {country} столица {data1[country]} есть  в словаре!')
        else:
            print(f'Страны {country} нет  в словаре!')

    @classmethod
    def add_country(cls, new_country, new_capital, filename, ):
        try:
            data1 = json.load(open(filename))
        except FileNotFoundError:
            data1 = {}
        data1[new_country] = new_capital

        with open(filename, 'w') as f:
            json.dump(data1, f, indent=3, ensure_ascii=False)

    @classmethod
    def delete_country(cls, del_country, filename, ):
        try:
            data1 = json.load(open(filename))
        except FileNotFoundError:
            data1 = {}
        del data1[del_country]

        with open(filename, 'w') as f:
            json.dump(data1, f, indent=3, ensure_ascii=False)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            print(json.load(f))


index = ''
while index != 6:
    try:
        index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n'
                          '4 - редактирование данных\n5 - просмотр данных\n6 - Завершение работы\nВвод: '))
        if index == 1:
            country_name = input('Введите название страны(с заглавной буквы):')
            capital_name = input('Введите название столицы страны(с заглавной буквы):')
            CountryCapital.add_country(country_name, capital_name, 'list_capital.json')
            print('Файл сохранен')

        if index == 2:
            country_name = input('Введите страну для удаления(с заглавной буквы):')
            CountryCapital.delete_country(country_name, 'list_capital.json')
            print('Файл сохранен')

        if index == 3:
            country_name = input('Введите название страны(с заглавной буквы):')
            CountryCapital.search_data(country_name, 'list_capital.json')

        if index == 4:
            country_name = input('Введите страну для корректировки: ')
            new_capital = input('Введите новое название столицы: ')
            CountryCapital.remove_dict(country_name, new_capital, 'list_capital.json')
            print('Файл сохранен')

        if index == 5:
            CountryCapital.load_from_file('list_capital.json')
    except:
        break
