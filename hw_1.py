print("Вариант 1")
a = 6
b = 10
print("a = ", a, "\n" + "b = ", b)
print("Замена")
a, b = b, a
print("a = ", a, "\n" + "b = ", b)
print("Вариант 2")
a = 8
b = 4
print("a = ", a, "\n" + "b = ", b)
a = a + b
b = a - b      #(a+b)-b
a = a - b      #a-(a-b)
print("Замена")
print("a = ", a, "\n" + "b = ", b)