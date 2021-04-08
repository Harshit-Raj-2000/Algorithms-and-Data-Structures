N = int(input())
arr = [int(x) for x in input().strip().split()]

if N == 1:
    print(arr[0])
else:
    large = arr[0]
    second = -1
    for i in range(1,N):
        if arr[i]>large:
            second = large
            large = arr[i]
        elif arr[i] > second and arr[i]!=large:
            second = arr[i]
    print(second)
