# def leader(arr,n):
#     max = arr[n-1]
#     a = []
#     for i in range(n-2,-1,-1):
#         if arr[i] > max:
#             a.insert(0,max)
#             max = arr[i]
#     a.insert(0,max)
#     return a

   ## The above logic is correct, but somehow a.insert(0,max) was taking time, so
   ## the below code worked

def leader(arr,n):
    max = arr[n-1]
    a = []
    for i in range(n-2,-1,-1):
        if arr[i] > max:
            a.append(max)
            max = arr[i]
    a.append(max)
    a.reverse()
    return a
    
arr = [int(x) for x in input().strip().split()]
a = leader(arr,len(arr))
print(*a)
