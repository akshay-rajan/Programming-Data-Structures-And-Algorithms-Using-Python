# Select the next element in the sorted order and exchange it with the values at the beginning of the list

def selection_sort(arr):
    for start in range(len(arr)):
        minpos = start
        # For each element in the array starting from the current index
        for i in range(start, len(arr)):
            # Find the minimum value in the array
            if arr[i] < arr[minpos]:
                minpos = i
        # Swap the minimum value with the current index
        arr[start], arr[minpos] = arr[minpos], arr[start]
        

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original: ", arr)
    selection_sort(arr)
    print("Sorted: ", arr)