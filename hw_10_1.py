s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")
s3 = set(s1) - set(s2)
print("Искомыми буквами являются:")
for i in s3:
    print(i, end=" ")

