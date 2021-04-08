#timecomplexity = O(n^2), space complexity = O(1)
#it takes a maximum of n swaps in insertion sort to complete
#the sorting

def selection_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        min_index = i
        for j in range(i+1,arr_len):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

a = [13,23,45,11,14,9,9]
selection_sort(a)
print(a)
