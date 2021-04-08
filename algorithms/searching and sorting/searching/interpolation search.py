#this is applied to sorted arrays where values are distributed
#uniformly.
#similar to binary search, bur instead of going to mid, we use
#the fact that the elements are uniformly distributed, to
#calculate pos, which is near to the key

#pos = lo + ((key - arr[lo])*((high-lo)//(arr[high]-arr[low])))

def interpolation_search(arr,key):
    arr_len = len(arr)
    low = 0
    high = arr_len - 1
    while low <= high and key>=arr[low] and key<=arr[high]:
        pos = low + int((key-arr[low])*((high-low)/(arr[high]-arr[low])))
        if arr[pos] == key:
            return pos
        elif arr[pos]>key:
            high = pos - 1
        else:
            low = pos + 1
    return -1

def recursive_interpolation_search(arr,key,low,high):
    if high < low or x < arr[low] or x > arr[high]:
        return -1
    pos = low + int((key-arr[low])*((high-low)/(arr[high]-arr[low])))
    if arr[pos] == key:
        return pos
    elif arr[pos]>key:
        return recursive_interpolation_search(arr,key,low,high-1)
    else:
        return recursive_interpolation_search(arr,key,low+1,high)

a = [1,3,5,8,9]
key = 8
n = len(a)
print(interpolation_search(a,key))
