
def quick_sort(arr):
    """Quick sort algorithm. Worst case time complexity O(n^2).
    Average case time complexity O(n log(n))."""
    quick_sort_helper(arr,0,len(arr)-1)

def quick_sort_helper(arr,first,last):
    if first<last:
        split_point = partition(arr,first,last)
        quick_sort_helper(arr,first,split_point-1)
        quick_sort_helper(arr,split_point+1,last)

def partition(arr,first,last):
    pivot_value = arr[first]
    left_mark = first+1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and arr[left_mark] <= pivot_value:
            left_mark += 1
        while left_mark <= right_mark and arr[right_mark] >= pivot_value:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]
    arr[first], arr[right_mark] = arr[right_mark], arr[first]
    return right_mark

arr = [54,26,93,17,77,31,44,55,20]
quick_sort(arr)
print(arr)

