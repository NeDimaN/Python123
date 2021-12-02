f = open('Test2.txt', 'r', encoding='utf-8')
s = f.readlines()
print(s)
pos1 = int(input("Введите индекс строки 1 для обмена: "))
pos2 = int(input("Введите индекс строки 2 для обмена: "))
if 0 <= pos1 <= 2 and 0 <= pos2 <= 2:
    s[pos1], s[pos2] = s[pos2], s[pos1]
else:
    print("Индексы введены неверно!")

f.close()
f = open('Test2.txt', 'w', encoding='utf-8')
f.writelines(s)
f.close()