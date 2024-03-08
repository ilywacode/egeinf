# id: 54936
def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 4, b) + f(a * 3, b)


print(f(2, 18) * f(18, 35))

a = [0] * 100
a[2] = 1
for i in range(3, 36):
    a[i] = a[i - 1] + a[i - 4]
    if i % 3 == 0:
        a[i] += a[i // 3]
    if i == 18:
        for j in range(18):
            a[j] = 0
print(a[35])
