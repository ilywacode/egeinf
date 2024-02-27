# id: 52134

f = open('24__1crre.txt')
s = f.readline()

alf = 'AEIOYU'

for x in alf:
    s = s.replace(x, '*')

print(s.count('*'))

# output: 57102
