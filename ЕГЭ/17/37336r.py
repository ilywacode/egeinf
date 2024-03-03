# id: 37336r

f = open('17 (1).txt')
a = [int(i) for i in f]

k = 0
maxim = 0
for i in range(int(len(a)) - 1):
    x, y = a[i], a[i + 1]
    if x * y % 3 == 0:
        k += 1
        maxim = max(maxim, x + y)

print(k, maxim)