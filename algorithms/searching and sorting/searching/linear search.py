def linear_search(array,key):
    array_len = len(array)
    for i in range(array_len):
        if array[i] == key:
            return i
    return -1


#improve linear search worst case time complexity
#element not found becomes O(n/2)
#element at last index become O(1)

def improved_linear_search(arr,key):
    arr_len = len(arr)
    left = 0
    right = n-1

    while left<=right:
        if arr[left] == key:
            return left
        elif arr[right] == key:
            return right
        left += 1
        right -= 1
    return -1

arr = [1,5,3,2,7,4]
key = 2
print(linear_search(array,key))
