def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1) + (2*n + 1)

print(f(5))