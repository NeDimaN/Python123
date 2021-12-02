
s = input("Введите строку: ")
print(s[:s.find('h')] + s[s.rfind('h') + 1:])
print(s[:s.find('h')+1] + s[s.rfind('h')-1:s.find('h'):-1] + s[s.rfind('h'):])
