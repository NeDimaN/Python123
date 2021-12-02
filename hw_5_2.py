num = [int(input("-> ")) for i in range(int(input("введите  элементы списка:\nn = ")))]
a = num[0]
for i in range(len(num)):
    if a < num[i]:
        print(num[i], end=" ")
    a = num[i]
