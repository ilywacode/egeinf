# id: 58501

def f(a, b):
    if a > b or a == 28:
        return 0
    if a == b:
        return 1
    return f(a + 3, b) + f(a * 2, b)

print(f(4, 47))