str1 = 'Ежевику для ежат\nПринесли два ежа.\nЕжевику еле-еле\nЕжата возле ели съели.'
print(str1)
str2 = str1.lower().split()
x = 0
for i in str2:
    if i[0] == 'е':
        x += 1
print()
print("Количество слов: ", x)
