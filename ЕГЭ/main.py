# id: 58505

def f(a, b):
    if a > b or a == 29:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 9, b)

print(f(4, 13) * f(13, 49))