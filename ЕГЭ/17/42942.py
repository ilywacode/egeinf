# id: 42942
f = open('42942__11x2b.txt')

n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))

maxim = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        x, y = a[i], a[j]
        if (x + y) % 13 == 0 and (x * y) % 2 == 0:
                maxim = max(maxim, x + y)

print(maxim)