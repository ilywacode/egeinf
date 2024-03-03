# id: 30194

def count_div(n):
    k = 0
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            k += 1
            if x != n // x:
                k += 1
    return k

k = 0

for x in range(421431, 754124):
    if count_div(x) == 12:
        k += 1

print(k)