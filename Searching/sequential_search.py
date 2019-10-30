
def seq_search(arr, item):
    """Sequential search into the array. Complexity O(n).
        Stops when found."""
    found = False
    for elem in arr:
        if elem == item:
            found = True
            break
    return found

def seq_search_2(arr, item):
    """Sequential search into the array. Complexity O(n).
        Stops when found."""
    found = False
    idx = 0
    while not found and idx < len(arr):
        if arr[idx] == item:
            found = True
        idx += 1
    return found

def seq_search_3(arr, item):
    """Sequential search into the array. Complexity O(n).
        Stops when found. Most elegant way."""
    for elem in arr:
        if elem == item:
            return True
    return False

def seq_search_on_sorted(arr, item):
    """Sequential search on sorted array. Complexity O(n).
        Stops when place where element should be is passed."""
    ptr = 0
    while ptr < len(arr) and arr[ptr] < item:
        ptr += 1
    if ptr > len(arr)-1:
        return False
    else:
        return arr[ptr] == item

#%%
seq_search_3([2,3,1,2,3,6,8,4,6], 1)
sequential_search([2,3,1,2,3,6,8,4,6], 7)
seq_search_on_sorted([1,2,3,4,5,6,8], 9)

