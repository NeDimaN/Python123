import random as r

mas1 = [r.randint(1, 100) for i in range(10)]
print(mas1)
a = []
b = []

for i in range(len(mas1)):
    for x in range(2, mas1[i]):
        if mas1[i] % x == 0:
            b.append(mas1[i])
            break
    else:
        a.append(mas1[i])

print(a)
print(b)

lst_sample_min = min(a)
print("Min: ", lst_sample_min)

mas1_max = max(b)
print("Max: ", mas1_max)
