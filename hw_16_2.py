def del_num(s, x):
    a = s[:x] + s[x + 1:]
    return a


s = '0123456789'
s2 = del_num(s, 4)
print(s)
print(s2)
