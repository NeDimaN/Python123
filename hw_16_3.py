def del_num(s, num):
    i = 0
    s2 = ''
    while i < len(s):
        if s[i] != num:
            s2 = s2 + s[i]
        else:
            s2 = s2
        i += 1
    return s2


str1 = '012345363738494'
str2 = del_num(str1, '3')
print(str1)
print(str2)
