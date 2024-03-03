# id: 42940

f = open('42940__11x1x.txt')
a = [int(x) for x in f]
a.remove(30)

k = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if (a[i] * a[j]) % (a[i] + a[j]) == 0:
            k += 1

print(k)