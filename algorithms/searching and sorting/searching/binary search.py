#space and time complexity both log(n)

def binary_search(sorted_arr,key):
    arr_len = len(sorted_arr)
    low = 0
    high = arr_len - 1

    while low <= high:
        mid = (low + high)//2
        if sorted_arr[mid] == key:
            return mid
        elif sorted_arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1
#the above works only for distinct elements, for same elements
# it might not return the first occurence of the number

#the below solution solves the above problem
#we store the index of key, and continue searching for other keys
#in remaining part of array
def binary_search_duplicate(arr,key):
    arr_len = len(arr)
    left = 0
    right = arr_len - 1
    mid_index = -1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == key:
            mid_index = mid
            right = mid - 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return mid_index

#recursive function for binary_search

def recursive_binary_search(arr,key,start,end):
    if start > end:
        return -1
    mid = (start+end)//2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return recursive_binary_search(arr,key,start,mid-1)
    else:
        return recursive_binary_search(arr,key,mid+1,end)

arr = [2,5,8,16,16,23,38,56,72,91]
key = 23
print(recursive_binary_search(arr,key,0,9))
