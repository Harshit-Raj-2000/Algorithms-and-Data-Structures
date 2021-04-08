def count(arr,x,n):
    left = 0
    right = n
    while left < right:
        mid = (left+right)//2
        if arr[mid] == x:
            while mid + 1 < n and arr[mid+1]==x:
                mid += 1
            break
        elif arr[mid]<x:
             left = mid+1
        else:
             right = mid

    while mid>-1 and arr[mid]>x:
        mid -= 1

    return mid+1

arr = [int(x) for x in input().strip().split()]
x,n = [int(a) for a in input().strip().split()]
print(count(arr,x,n))
