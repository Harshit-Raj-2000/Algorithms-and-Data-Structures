# def num_triangles(arr,n):
#     num = 0
#     for i in range(n-2):
#         for j in range(i+1,n-1):
#             for k in range(j+1,n):
#                 if (arr[i]+arr[j] > arr[k]) and (arr[i]+arr[k] > arr[j]) and (arr[j]+arr[k] > arr[i]) :
#                     num += 1
#     return num
        ##The above was taking too much time, it was of O(n^3) time complexity

## below is a method to get the num of triangles, it is of O(n^2) time complexity but It is getting difficult for me to comprehend
## that exactly what is happening.

def num_triangles(arr,n):
    arr.sort()
    num = 0
    for i in range(0,n-1):
        k = i + 2
        for j in range(i+1,n):
            while k<n and (arr[i] + arr[j] > arr[k]):
                k += 1
            if k>j:
                num += k-j-1
    return num




array = [int(x) for x in input().strip().split()]
n = len(array)
print(num_triangles(array,n))
