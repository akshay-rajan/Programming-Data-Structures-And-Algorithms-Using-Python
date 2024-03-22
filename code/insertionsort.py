def insertionSort(arr):
    for i in range(len(arr)):
        pos = i
        # * Swap the current element with the previous element until it is in the correct position
        while pos > 0 and arr[pos] < arr[pos - 1]:
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            pos -= 1
            

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original:", arr)
    insertionSort(arr)
    print("Sorted:", arr)