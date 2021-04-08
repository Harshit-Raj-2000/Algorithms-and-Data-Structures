#we jump over a few elements in the array, for eg- if jump size
#is m, we go m,2m,2m, at any point the value is greator than m,
#we do linear search from last jump value to current jump value

#In the worst case the num of comparisions are (n//m + m-1),
#this value is min when m = √n, so this is the optimal jump
#size

#no. of blocks to be jumped = n/jump_value(√n) = √n
#time complexity = O(√n) space complexity = O(1)
import math

def jump_search(arr,key):
    arr_len = len(arr)
    jump_value = int(math.sqrt(arr_len))
    i = 0
    while i < arr_len and arr[i]<key:
        i += jump_value
    for k in range(i-jump_value+1,i+1):
        if k == arr_len:
            break
        if arr[k] == key:
            return k
    return -1



#different code(geeks for geeks) for same above logic-
#P.S. I don't like this code

def gfg_jump_search(arr,key):
    arr_len = len(arr)
    step = math.sqrt(arr_len)

    while arr[int(min(step,arr_len)-1)] < key:
        prev = step
        step += math.sqrt(arr_len)
        if prev >= arr_len:
            return -1
    while arr[int(prev)] < key:
        prev += 1
        if prev == min(step,arr_len):
            return -1
    if arr[int(prev)] == key:
        return int(prev)
    return -1

arr = [1,3,5,5,6,6,9]
key = 6
print(gfg_jump_search(arr,key))
