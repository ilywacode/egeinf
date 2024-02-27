# id: 23511

f = open('Задание_24__ktcx__t5nu.txt')
s = [str(x) for x in f]
cnt = 0
for x in range(len(s)):
    if s[x].count('X') == s[x].count('S'):
        cnt += 1

print(cnt)

# output: 48