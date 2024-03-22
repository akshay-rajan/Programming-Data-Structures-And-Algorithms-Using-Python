def mergeSort(arr, left, right):
    # If the array has 1 element, return it
    if right - left <= 1:
        return arr[left:right]
    # Recursively sort the left and right halves
    mid = (left + right) // 2
    print("Splitting:", arr[left:mid], arr[mid:right])
    left_half, right_half = mergeSort(arr, left, mid), mergeSort(arr, mid, right)
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left_half, right_half):
    # If one half is empty, return the other
    if not left_half:
        return right_half
    if not right_half:
        return left_half
    # Merge the two halves by comparing the first elements
    print("Merging:", left_half, right_half)
    # If one half has a smaller element, merge the rest
    if left_half[0] < right_half[0]:
        return [left_half[0]] + merge(left_half[1:], right_half)
    return [right_half[0]] + merge(left_half, right_half[1:])



if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original:", arr)
    arr = mergeSort(arr, 0, len(arr))
    print("Sorted:", arr)