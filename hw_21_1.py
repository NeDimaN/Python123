f = open('Test1.txt', 'r', encoding='utf-8')
s = f.readlines()
print(s)
pos = int(input("Введите индекс строки для удаления: "))
if 0 <= pos <= 2:
    s[pos] = ''
else:
    print("Индекс введен неверно!")

f.close()
f = open('Test1.txt', 'w', encoding='utf-8')
f.writelines(s)
f.close()
