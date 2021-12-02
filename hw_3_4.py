num = int(input("Введите колиество символов: "))
typ = input("Введите символ: ")
print("0 - горизонтальная \n1 - вертикальная")
orient = int(input("Ориентация линия: "))
i = 0
if orient == 0:
    while i < num:
        print(typ, end=" ")
        i += 1
else:
    while i < num:
        print(typ)
        i += 1
