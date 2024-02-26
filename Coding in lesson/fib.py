def fibonacci(n):
    total = 0 
    while n > 0:
        total += n
        n -= 1
    return total

print(fibonacci(10)) # 55

def count(n):
    while n > 0:
        print(n)
        n -= 1
    print("You have reached the base case.")
    return

print(count(5))