# id: 59227

from itertools import product

s = 'КОНФЕТА'

cnt = 0

for x in product(s, repeat=5):
    t = x[0] + x[1] + x[2] + x[3] + x[4]
    if t.count('О') + t.count('А') + t.count('Е') >= 2:
        cnt += 1

print(cnt)

# output: 11943