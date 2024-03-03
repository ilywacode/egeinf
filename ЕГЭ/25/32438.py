# id: 32438

def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

k = 0
s = 0

for x in range(157314, 853413):
    a = x ** 0.5
    if a == int(a):
        if is_prime(x ** 0.5):
            k += 1
            s += x
print(k, s)