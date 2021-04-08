#worst case time complexity - O(n*n), when elements are reverse sorted
#best case time complexity - O(n), when elements are sorted
#auxilarry space = O(1)

def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        flag = 0
        for j in range(0,arr_len-i-1):
            if arr[j+1] < arr[j]:
                flag = 1
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if flag == 0:
            break

arr = [8,9,10,11,34,23,15,11,9]
bubble_sort(arr)
print(arr)
