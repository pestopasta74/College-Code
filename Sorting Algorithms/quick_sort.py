import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def main():
    sizes = [100, 1000, 10000, 100000]  # You can add more sizes to compare

    for size in sizes:
        arr = generate_random_array(size)

        start_time = time.time()
        quick_sort(arr)
        end_time = time.time()

        print(f"Time taken to sort {size} integers: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()