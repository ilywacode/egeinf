# id: 29631

def f(x, y, z, w):
    return (not w) <= ((y or not(z)) == (x <= (not y)))

print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w) == False:
                    print(x, y, z, w)

# output:
# x y z w
# 0 0 1 0
# 1 0 1 0
# 1 1 0 0
# 1 1 1 0

# answer: yzwx