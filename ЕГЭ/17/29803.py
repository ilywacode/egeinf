# id: 29803

f = open('dz17-11__tcck.txt')
a = [int(x) for x in f]

k = 0
maxim = 0

for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if (x + y) % 3 == 0 and (x + y) % 6 != 0 and abs(x * y) % 10 == 8:
        k += 1
        maxim = max(maxim, x + y)

print(k, maxim)

