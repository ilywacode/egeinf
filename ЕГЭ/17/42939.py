# id: 42939

f = open('42939__11x1i.txt')
a = [int(x) for x in f]
a.remove(28)

k = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        x, y = a[i], a[j]
        if (x + y) % 10 == 0 and (x * y) % 2 == 0:
            k += 1
print(k)