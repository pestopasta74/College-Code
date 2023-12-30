def factiorial(n):
    if n == 0:
        return 1
    else:
        return n * factiorial(n-1)

print(factiorial(int(input())))