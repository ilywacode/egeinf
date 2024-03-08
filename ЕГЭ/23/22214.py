# id: 22214

a = [0] * 100
a[7] = 1
for i in range(8, 60):
    a[i] = a[i - 1] + a[i - 10]
print(a[49])