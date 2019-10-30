
def binary_search(arr, start, finish, item):
    """Binary search, recursive definition.
    Returning True or False. Complexity O(log n)."""
    found = False
    if start <= finish:
        mid = (start + finish) // 2
        if item == arr[mid]:
            found = True
        elif item < arr[mid]:
            found = binary_search(arr, start, mid-1, item)
        else:
            found = binary_search(arr, mid+1, finish, item)
    return found


def binarySearch(arr, start, finish, item):
    """Binary search, recursive definition.
        Returning element index. Complexity O(log n)."""
    if start <= finish:
        mid = (start + finish) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binarySearch(arr, start, mid - 1, item)
        else:
            return binarySearch(arr, mid + 1, finish, item)
    else:
        return -1


def binarySearch(arr, start, finish, item):
    """Binary search, iterative definition.
        Returning element index. Complexity O(log n)."""
    while start <= finish:
        mid = (start + finish) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            start = mid + 1
        else:
            finish = mid - 1
    return -1

arr = [1,2,3,5,6,7,8,10]
print(binarySearch(arr, 0, len(arr)-1, 5))






