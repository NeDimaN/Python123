f = open('Test3.txt', 'r', encoding='utf-8')
s = f.readlines()
print(s)
s = s[::-1]
f.close()
f = open('Test3.txt', 'w', encoding='utf-8')
f.writelines(s)
f.close()

