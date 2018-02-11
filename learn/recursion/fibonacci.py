def fib(n):
    f = 0
    g = 1
    while n:
        g = g + f
        f = g - f
        n -= 1
    return g

print(fib(2))