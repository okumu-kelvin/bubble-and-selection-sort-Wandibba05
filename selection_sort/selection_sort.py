def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


my_list = [29, 10, 14, 37, 13]
print("Original:", my_list)

selection_sort(my_list)
print("Sorted:  ", my_list)


