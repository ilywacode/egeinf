# id: 37337r

f = open('17 (2).txt')
a = [int(i) for i in f]

k = 0
maxim = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        x, y = a[i], a[j]
        if x != y:
            if x % 160 != y % 160:
                if x * y % 7 == 0:
                    k += 1
                    maxim = max(maxim, x + y)

print(k, maxim)