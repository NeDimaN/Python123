d1 = {'emp1': {'name': 'Jhon', 'salary': 7500},
      'emp2': {'name': 'Emma', 'salary': 8000},
      'emp3': {'name': 'Brad', 'salary': 6500}
      }
print(d1['emp3'])
print(d1['emp3']['salary'])
d1['emp3']['salary'] = 8500
for i in d1:
    print(i)
    for key, value in d1[i].items():
        print(f'{key} : {value}')
