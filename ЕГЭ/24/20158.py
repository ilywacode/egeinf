# id: 20158

f = open('24__svkj.txt')
s = f.readline()

s = s.split('K')
k = 0
for x in s:
    if len(x) == 2:
        k += 1
    elif len(x) >= 2:
        k += int(len(x)) - 1

print(k)

# output: 694797