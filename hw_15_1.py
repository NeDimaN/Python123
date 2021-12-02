def func_outer(n):
    def func_inner(x):
        return n * x

    return func_inner


res = func_outer(2)
print(res(15))
print(res(20))
res = func_outer(3)
print(res(15))
print(res(20))