# id: 58103
def f(a, b):
    if a > b or a == 8:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a * 2, b)

print(f(1, 30))