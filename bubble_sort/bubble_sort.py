def bubble_sort(arr):
    for i in range(len(arr)):

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", my_list)

bubble_sort(my_list)
print("Sorted list:  ", my_list)

