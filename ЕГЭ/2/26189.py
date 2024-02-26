# id: 26189

def f(x, y, z):
    return ((y or z) <= x) or (x == y)

print('x y z')

for x in range(2):
    for y in range(2):
        for z in range(2):
            if f(x, y, z) == False:
                print(x, y, z)


# output:
# x y z
# 0 1 0
# 0 1 1

# answer: zyx