# id: 26177

f = open('Задание_17__iob5__rkna.txt')
a = [int(i) for i in f]

k = 0
maxim = -100000

for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if (x * y) % 2 == 1 and (x + y) % 2 == 0:
        k += 1
        maxim = max(maxim, x + y)

print(k, maxim)