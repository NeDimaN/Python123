vowels = {"а", "о", "э", "е", "и", "ы", "у", "ё", "ю", "я"}
s = input("Введите строку: ")
a = []
[a.append(i) for i in s if i in vowels]
print("Количество гласных равно:", len(a))




