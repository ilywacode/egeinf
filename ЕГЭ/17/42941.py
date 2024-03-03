# id: 42941

f = open('42941__11x26.txt')
a = [int(x) for x in f]
a.remove(25)

k = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        x, y = a[i], a[j]
        if (x > 100 or y > 100) and (x + y) % 12 == 0:
            k += 1

print(k)