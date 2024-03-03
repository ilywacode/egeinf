# id: 30446

def f(n):
    if n > 10:
        return n * n
    if n <= 10:
        return f(n + 2) - 2 * g(n + 1)

def g(n):
    if n < 2:
        return n * n * n
    if n >= 2:
        return f(n + 1)

print(f(18))

# output: 324