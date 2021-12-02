s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for i in range(len(s)):
    num = s.count(s[i])
    if num == 1:
        print(s[i], end=" ")