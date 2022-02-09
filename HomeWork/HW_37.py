import json
from random import choice


def get_person():
    name = ''
    tel = ''
    index_num = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)

    while len(index_num) != 5:
        index_num += choice(num)

    person = {'name': name, 'tel': tel}

    return person, index_num


def write_json(person_dict, num):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data[num] = person_dict
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=4)


for i in range(5):
    write_json(get_person()[0], get_person()[1])

with open('persons.json') as f:
    print(json.load(f))
    