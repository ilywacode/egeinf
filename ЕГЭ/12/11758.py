# id: 11758

s = '3' * 10

while '33' in s:
    if '33' in s:
        s = s.replace('33', '32', 1)

print(s)

# output: 3232323232