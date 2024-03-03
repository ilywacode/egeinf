# id: 30448

def f(n):
    if n < 3:
        return 2
    if n > 2:
        return f(n - 1) + 2 * g(n - 1) + f(n / 2)

def g(n):
    if n < 3:
        return 2
    if n > 2:
        return f(n - 1) + g(n / 3) + g(n - 1)

print(f(12) + g(4))

# output: 29476