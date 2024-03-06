def bubble_sort_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr

print(bubble_sort_array(["F", "A", "B", "C", "D", "E"]) == ["A", "B", "C", "D", "E", "F"]) # True