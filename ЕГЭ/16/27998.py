# id: 27998

def f(n):
    if n <= 2:
        return n * n
    if n > 2:
        return f(n - 2) + g(n - 1) * 2 - n

def g(n):
    if n <= 2:
        return n + 1
    if n > 2:
        return g(n - 1) + f(n - 2) + n

print(f(5) + g(3))

# output: 36