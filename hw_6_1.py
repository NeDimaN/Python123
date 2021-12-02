num = [int(input("-> ")) for i in range(int(input("введите  элементы списка:\nn = ")))]
ch = int(input("Введите число: \nch= "))
if ch in num:
    print("Число присутствует в элементах списка")
else:
    print("Число отсутствует в элементах списка")


