# У исполнителя Калькулятор две команды, которым присвоены номера:
# 1. прибавь 1
# 2. умножь на 2
# Сколько есть программ, которые преобразуют число 1 в 16?

a = [0] * 100
a[1] = 1
for i in range(2, 17):
    if i % 2 == 0:
        a[i] = a[i - 1] + a[i // 2]
    else:
        a[i] = a[i - 1]

print(a[16])


from functools import lru_cache
@lru_cache(None)

def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a * 2, b) + f(a + 2, b)

print(f(3, 9) * f(9, 11) * f(11, 13))