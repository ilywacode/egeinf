# id: 30444

def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    if n > 2 and n % 2 == 1:
        return f(n - 3) + 3

for x in range(1000):
    if f(x) == 31:
        print(x)

# output: 893