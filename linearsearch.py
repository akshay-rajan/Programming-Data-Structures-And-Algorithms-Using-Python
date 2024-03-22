def linearSearch(arr, val):
    for x in arr:
        if x == val:
            return True
    return False


if __name__ == "__main__":
    arr = [23, 12, 59, 34, 21, 11, 30, 25]
    if linearSearch(arr, int(input("Number to search for: "))):
        print("Number found!")
    else:
        print("Number not found!")
