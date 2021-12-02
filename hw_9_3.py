tpl = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
print(tpl)
res = []
for el in tpl:
    if el not in res:
        print("Количество", el, "=", tpl.count(el))
        res.append(el)


