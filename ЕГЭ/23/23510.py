# id: 23510

a = [0] * 100
a[1] = 1
for i in range(2, 56):
    a[i] = a[i - 1] + a[i // 4] * (i % 4 == 0)

print(a[55])