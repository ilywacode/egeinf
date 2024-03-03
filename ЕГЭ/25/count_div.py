def count_div(n):
    k = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            k += 1
            if i != n // i:
                k += 1
    return k