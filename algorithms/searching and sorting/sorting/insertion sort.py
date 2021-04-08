# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
#worst case is when elements are in reverse order - O(n^2)
#best case when elements are already sorted - O(n)

def insertion_sort(arr):
    arr_len = len(arr)
    for i in range(1,arr_len):
        temp = arr[i]
        k = i-1
        while k >= 0 and arr[k] > temp:
            arr[k+1] = arr[k]
            k -= 1
        arr[k+1] = temp

arr = [12,32,11,23,11,35,46,39]
insertion_sort(arr)
print(arr)
