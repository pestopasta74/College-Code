def countWays(n):
    if n==1:
        return 1
    else:
        return countWays(n-1) + countWays(n-2)

print(countWays(50))
