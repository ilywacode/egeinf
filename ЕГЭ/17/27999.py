# id: 27999

f = open('Задание_17__t7ox.txt')
a = [int(x) for x in f]

mid = sum(a) / 10000
k = 0
maxim = 0

for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if (x < mid and y > mid) or (x > mid and y < mid):
        k += 1
        maxim = max(maxim, x + y)

print(k, maxim)