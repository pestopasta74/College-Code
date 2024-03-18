import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def main():
    sizes = [100, 1000, 10000]  # You can add more sizes to compare

    for size in sizes:
        arr = generate_random_array(size)

        start_time = time.time()
        insertion_sort(arr)
        end_time = time.time()

        print(f"Time taken to sort {size} integers: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
