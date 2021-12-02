import random as r


def binary_search(lst, n):
    lst.sort()
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == n:
            found = True
        else:
            if n < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


s = [r.randint(0, 100) for i in range(10)]
print(s)

num = int(input("Введите число: "))
if binary_search(s, num) is True:
    print(f'Число {num} в списке присутствует')
else:
    print(f'Число {num} в списке отсутствует')
