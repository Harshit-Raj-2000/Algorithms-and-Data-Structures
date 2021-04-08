# def remove_duplicate(arr,n):
#     key = arr[0]
#     a = [key]
#     index = 1
#     while index < n:
#         while index<n and arr[index] == key:
#             index += 1
#         if index<n:
#             key = arr[index]
#             a.append(key)
#             index = index + 1
#     return a
    ##This works only if we use another array
    ##We have to modify the same array

# def remove_duplicate(arr,n):
#     key = arr[0]
#     index = 1
#     while index < n:
#         while index<n and arr[index] == key:
#             del arr[index]
#             n = n-1
#         if index<n:
#             key = arr[index]
#             index = index + 1
    ##This is a good way, another way to do the same is given
def remove_duplicate(arr,n):
    j = 0
    for i in range(0,n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j+=1
    arr[j] = arr[n-1]
    j+=1
    return j

arr = [int(x) for x in input().strip().split()]
j = remove_duplicate(arr,len(arr))
for i in range(j):
    print(arr[i],end=" ")
