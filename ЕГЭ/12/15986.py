# id: 15986

s = '23' * 14

while '2323' in s:
    s = s.replace('2323', '23', 1)

print(s)

# output: 23