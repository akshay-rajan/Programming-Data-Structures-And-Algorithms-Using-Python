def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    # Partition the array into three parts based on the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively sort the left and right parts
    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    arr = list(range(49, 0, -2))
    print("Original: ", arr)
    print("Sorted: ", quicksort(arr))