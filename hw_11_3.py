col = int(input("Введите количество студентов: "))
dict_stud = {}
sum_value = 0
for i in range(1, col + 1):
    key = input(f'{i}-й студент: ')
    value = int(input('Балл: '))
    dict_stud[key] = value
    sum_value += value
mid_sum = round(sum_value / col)
print(f'Средний балл: {mid_sum}. Студенты с баллом выше среднего:')
for key in dict_stud:
    if dict_stud[key] > mid_sum:
        print(key)







