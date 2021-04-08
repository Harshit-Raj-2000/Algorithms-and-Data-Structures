def binary_search(arr,key,low,high):
    if low > high:
        return -1
    mid = low + (high-low)//2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr,key,low,mid-1)
    else:
        return binary_search(arr,key,mid+1,high)

#time complexity = O(log(n)) auxillary space = O(logn) as binary search is
#recursive else O(1) for iterative binary search
def exponential_search(arr,key):
    arr_len = len(arr)
    if arr[0] == key:
        return 0
    i = 1
    while i<=arr_len-1 and arr[i] <= key:
        i *= 2
    if i > arr_len-1 and key > arr[arr_len-1]:
        return -1
    else:
        k = min(i,arr_len-1)
        return binary_search(arr,key,i//2,k)

arr = [1,2,5,6,78,100]
key = 78
print(exponential_search(arr,key))
