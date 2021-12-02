def count_minus(lst):
    count = 0
    if not lst:
        return count
    if lst[0] > 0:
        return count_minus(lst[1:])
    else:
        count += 1
    return count + count_minus(lst[1:])


s = [-2, 3, 8, -11, -4, 6]
print(s)
print(f'Количество отрицательных элементов равно n = {count_minus(s)}')
