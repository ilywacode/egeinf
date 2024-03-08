# id:52532
def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 2, b) + f(a * 2, b)

print(f(3,9) * f(9, 11) * f(11, 13))

a = [0] * 14
a[3] = 1
for i in range(4, 14):
    a[i] = a[i - 1] + a[i - 2] + a[i // 2] * (i % 2 == 0)
    if i == 9 or i == 11:
        for j in range(i):
            a[j] = 0
print(a[13])
