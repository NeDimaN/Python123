import random as r

mas1 = [r.randint(0, 100) for i in range(20)]
print(mas1)
a = 0
for i in range(len(mas1)):
    a += mas1[i]
print("Сумма элементов списка: ", a)

