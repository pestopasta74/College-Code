def merge_sorted_lists(list_1, list_2):
    result = []
    while len(list_1) > 0 and len(list_2) > 0:
        if list_1[0] < list_2[0]:
            result.append(list_1.pop(0))
        else:
            result.append(list_2.pop(0))
    result += list_1
    result += list_2
    return result

if __name__ == '__main__':
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6, 7]))  # [1, 2, 3, 4, 5, 6, 7]
    print(merge_sorted_lists([1, 3, 5, 7], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6, 7]
    print(merge_sorted_lists([1, 3, 5, 7], [2, 4, 6, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]
    print(merge_sorted_lists([], [2, 4, 6, 8]))  # [2, 4, 6, 8]
    print(merge_sorted_lists([1, 3, 5, 7], []))  # [1, 3, 5, 7]
