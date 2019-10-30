
def selection_sort(arr):
    """Selection sort algorithm. Complexity O(n^2)"""
    for i in range(0, len(arr)-1):
        min_ptr = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_ptr]:
                min_ptr = j
        tmp = arr[i]
        arr[i] = arr[min_ptr]
        arr[min_ptr] = tmp
    return arr

#%%
print(selection_sort([5,3,4,6,2,1,7,3,2,6,5,2]))





