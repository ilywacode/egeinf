# id: 26959

f = open('Задание_24__odge__wzwt.txt')

s = f.readline()

maxim = 0

s = s.replace('D', ' ')
s = s.replace('M', ' ')
s = s.split(' ')

for x in s:
    maxim = max(maxim, len(x))

print(maxim)

# output: 2