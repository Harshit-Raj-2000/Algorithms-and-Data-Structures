T = int(input().strip())

def reverse(N,arr):
    for i in range(N//2):
        arr[i],arr[N-1-i] = arr[N-1-i],arr[i]
while T>0:
    N = int(input())
    arr = [int(x) for x in input().strip().split()]
    reverse(N,arr)
    print(*(arr))
    T = T-1

# A python way would be to use arr[::-1]
