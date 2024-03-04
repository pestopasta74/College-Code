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

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) # 4 time complexity is O(log n)