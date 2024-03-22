def binarySearch(arr, l, r, value):
    if r - l <= 0:
        return False
    mid = (l + r) // 2
    if value == arr[mid]:
        return True
    # If the value is greater than value at the middle, search right
    elif value > arr[mid]:
        return binarySearch(arr, mid + 1, r, value)
    # If the value is lesser than value at the middle, search left
    else:
        return binarySearch(arr, l, mid, value)
    

if __name__ == "__main__":
    arr = [2, 4, 6, 9, 13, 25, 100]
    if binarySearch(arr, 0, len(arr), int(input("Value: "))):
        print("Number found!")
    else:
        print("Number not found!")