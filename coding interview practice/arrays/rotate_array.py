T = int(input())

def reverse(arr,low,high):
    n = (high - low + 1)//2
    for i in range(low,low+n):
        arr[i],arr[high+low-i] = arr[high+low-i],arr[i]

while T>0:
    N,R = [int(x) for x in input().strip().split()]
    arr = [int(x) for x in input().strip().split()]
    reverse(arr,0,R-1)
    reverse(arr,R,N-1)
    reverse(arr,0,N-1)
    print(*arr)
    T = T-1
