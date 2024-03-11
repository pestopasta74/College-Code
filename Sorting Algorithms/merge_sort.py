from merge_sorted_lists import merge_sorted_lists

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_sorted_lists(left, right)

print(merge_sort([3, 1, 5, 2, 4]))  # [1, 2, 3, 4, 5]