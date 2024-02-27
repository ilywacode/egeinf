# id: 29877

f = open('Задание_5_ДЗ__tcey.txt')
s = f.readline()

cnt = 1
maxim = 0
for i in range(len(s) - 1):
    if (s[i] != s[i + 1]):
        cnt += 1
        maxim = max(maxim, cnt)
    else:
        cnt = 1

print(maxim)

# output: 35