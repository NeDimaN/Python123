def func(mas):
    res = []
    [res.append(i) for i in mas if i % 13 == 0 and i > 0]
    if len(res) > 0:
        print("Максимальное число кратное 13:", max(res))
    else:
        print("Нет положительного числа кратного 13")


func((2, 7, 0, 3, 1, 5, -13))
func((2, 7, 0, 3, 1, 5, -13, 13))
func([26])
func((99, 99, 100, 34, -39))
func((99, 39, 99, 100, 34))
