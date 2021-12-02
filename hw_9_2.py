tpl = tuple(("ab", "abcd", "cde", "abc", "def"))
s = input("Введите элемент для поиска: ")
if s in tpl:
    print("Элемент есть!")
else:
    print("Элемента нет!")

