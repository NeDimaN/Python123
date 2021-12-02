def change_Char(s, c_old, c_new):
    s2 = ''
    i = 0
    while i < len(s):
        if (s[i] == c_old) and (i % 2 == 0):
            s2 = s2 + c_new
        else:
            s2 = s2 + s[i]
        i += 1

    return s2


str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
str2 = change_Char(str1, "N", "P")
print(str1)
print(str2)
