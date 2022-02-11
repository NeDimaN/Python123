# from car import electrocar
#
#
# def main():
#     e = electrocar.ElectroCar('Tesla', 'T', 2018, 99000)
#     e.show_car()
#     e.description_battery()
#
#
# if __name__ == '__main__':
#     main()
# ===============================================03.02.2022


# упаковка данных-
# Сериализация(кодирование)- запись данных на диск
# Десериализация(декодирование) - чтение данных

# Стандартной библиотеке Python:
# - marshal
# - pickle
# dump()- сохраняет данные в файл
# load() - считывает данные из файла
# dumps() - сохраняет данные в оперативную память
# loads() -считывает данные из оперативной памяти
# -json

# import pickle
#
# filename = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоко', 'манго'],
#     'овощи': ['морковь'],
#     'бюджет': 1000
# }
#
# with open(filename, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
#
# with open(filename, 'rb') as fh:
#     print(pickle.load(fh))

# ===========================
# import pickle


# class Test:
#     a_number = 35
#     a_string = 'привет'
#     a_list = [1, 2, 3]
#     a_tuple = (22, 23)
#     a_dict = {'first': 'a', 'second': 2, 'third': [1, 2, 3]}
#
#     def __str__(self):
#         return f'Число: {Test.a_number}\nСтрока: {Test.a_string}\nСписок: {Test.a_list}' \
#                f'\nКортеж: {Test.a_tuple}\nСловарь: {Test.a_dict}'
#
#
# obj = Test()
# my_obj = pickle.dumps(obj)
# print(f'Сериализация в строку:\n{my_obj}\n')
#
# l_obj = pickle.loads(my_obj)
# print(f'Десериализация в строку:\n{l_obj}\n')
# =============================
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(2)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         print(attr)
#         del attr['c']
#         print(attr)
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)
# ======================================


# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename, encoding='utf-8')
#         self.count = 0
#
#     def red_line(self):
#         self.count += 1
#         line = self.file.read_line()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return f'{self.count}: {line}'
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename, encoding='utf-8')
#         for i in range(self.count):
#             file.read_line()
#         self.file = file
#
#
# reader = TextReader('hello.txt')
# print(reader.red_line())
# print(reader.red_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.red_line())
# ===============================================

# import json

# data = {
#     "firstName": 'Jane',
#     "lastName": 'Djo',
#     "hobbies": ["running", "sky diving"],
#     "age": 5
# }
#
# with open("data_file.json", "w") as fw:
#     json.dump(data, fw, indent=4)
#
# with open('data_file.json', 'r') as fw:
#     print(json.load(fw))

# st = json.dumps(data, sort_keys=True)
# data = json.loads(st)
# print(data)
# ==========================================
# x = {
#     "name": "Виктор"
# }
# y = {
#     "name": "Виктор"
# }
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))

# =============================================

# import json
# from random import choice
#
#
# def get_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#     data.append(person_dict)
#     print(data)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(get_person())
# ======================================08.02.2022
# import json
# from random import choice
#
#
# def get_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person, tel
#
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = {}
#     data[num] = person_dict
#
#     print(data)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(get_person()[0], get_person()[1])
#
# with open('persons.json', 'r') as f:
#     print(json.load(f))
# ==============================================
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ', '
#         return f'Студент {self.name}: {a[:-2]}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 1)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#         data.append({'name': stud.name, 'marks': stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=3)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + '\n'
#         return f'Группа:{self.group}\n{a}'
#
#     def add_st(self, new_student):
#         self.students.append(new_student)
#
#     def remove_st(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def change_group(cls, group1, group2, index):
#         return group2.add_st(group1.remove_st(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             tpm = {'Students': stud_list}
#             data.append(tpm['Students'])
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_journal(cls, file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
# st1 = Student('Orlov', [5, 4, 4, 5, 3])
# st2 = Student('Sokolov', [3, 4, 2, 2, 3])
# st3 = Student('Filynin', [3, 4, 3, 4, 3])
#
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# print(my_group)
# # Group.dump_group('Group.json', my_group)
# my_group.add_st(st3)
# print(my_group)
# my_group.remove_st(0)
# print(my_group)
#
# group2 = [st1]
# my_group2 = Group(group2, 'ГК Java')
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)
# # Group.dump_group('Group.json', my_group2)
#
# # Student.dump_to_json(st1, 'student.json')
#
# # Student.dump_to_json(st2, 'student.json')
# # Student.load_from_file('student.json')
# Group.upload_journal('Group.json')
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(4)
# # print(st1)
# # st1.edit_mark(4, 5)
# # print(st1)
# # print(st1.average_mark())
# =================================================
# request
# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
# print(todos[:10])
#
# print(type(todos))

# =========================================10.02.2022


# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
#
# todos_by_users = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_users[todo['userId']] += 1
#         except KeyError:
#             todos_by_users[todo['userId']] = 1
#
# print(todos_by_users)
#
# top_users = sorted(todos_by_users.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# max_users = ' and '.join(users)
# print(users)
# s = 's' if len(users) > 1 else ''
# print(f'user{s} {max_users} completed {max_complete} TODOs')
#
#
# def keep(todo):
#     is_completed = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_completed and has_max_count
#
#
# with open('data.json', 'w') as f:
#     td = list(filter(keep, todos))
#     json.dump(td, f, indent=2)
#
# with open('data.json', 'r') as f:
#     print(json.load(f))

# ============================================
# csv ( comma separeted values)
# csv.reader
# csv.writer
# csv.DictWriter
# csv.DictReader


import csv

# with open('data.csv') as f:
#     reader = csv.reader(f, delimiter=';')
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f'Файл содержит стобцы: {";".join(row)}')
#         else:
#             print(f'\t{row[0]} - {row[1]}. Родился в {row[2]} году.')
#         count += 1
#     print(f'всего в файле {count} строки')


# with open('data.csv') as f:
#     fields_name = ['Имя', 'Профессия', 'Год рождения']
#     reader = csv.DictReader(f, fieldnames=fields_name, delimiter=';')
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f'Файл содержит стобцы: {";".join(row)}')
#         print(f'\t{row["Имя"]} - {row["Профессия"]}. ', end='')
#         print(f'Родился в {row["Год рождения"]} году.')
#         count += 1
#     print(f'всего в файле {count + 1} строки')

# ============================================

# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Дима', '5', '12'])
#     writer.writerow(['Маша', '5', '11'])
#     writer.writerow(['Оля', '11', '18'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London; Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool; Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool; Better str'],
#         ['sw4', 'Cisco', '3650', 'London; Best str']]
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
#
# with open('sw_data.csv') as f:
#     print(f.read())

# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(data)
#
# with open('sw_data.csv') as f:
#     print(f.read())
# =============================================================

# with open('student1.csv', 'w') as f:
#     names = ['Имя', 'Возраст']
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     writer.writeheader()
#     writer.writerow({'Имя': 'Дима', 'Возраст': '6'})
#     writer.writerow({'Имя': 'Маша', 'Возраст': '7'})
#     writer.writerow({'Имя': 'Матвей', 'Возраст': '12'})
 #===============================================

data = [{
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]

with open('dict.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(data[0].keys()))
    writer.writeheader()
    for d in data:
        writer.writerow(d)