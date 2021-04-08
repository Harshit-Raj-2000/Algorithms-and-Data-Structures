##similar to binary search, but wwe divide array into 3
#parts instead of 2

def ternary_search(arr,key,low,high):
    if high < low:
        return -1
    else:
        mid1 = low + (high-low)//3
        mid2 = mid1 + (high-low)//3
        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2
        if key<arr[mid1]:
            return ternary_search(arr,key,low,mid1-1)
        elif key > arr[mid2]:
            return ternary_search(arr,key,mid2+1,high)
        else:
            return ternary_search(arr,key,mid1+1,mid2-1)

#time complexity O(log(n)), but worse than binary search, because.
#somehow ternary search has more comparisions in worst case.
#space complexity O(log(n)) only due to call stack of recursive function
#if implemented iteratively, space complexity O(1)

arr = [1,3,5,7,9]
arr_len = len(arr)
key = 8
print(ternary_search(arr,key,0,arr_len-1))
