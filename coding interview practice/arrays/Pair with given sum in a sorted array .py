def Countpair (arr, n, k) :
    i = 0
    j = n-1
    count = 0
    while i<j and arr[i]<k:
        value = arr[i] + arr[j]
        if value == k:
            count += 1
            i += 1
            j -= 1
        elif value > k:
            j -= 1
        else:
            i += 1
    if count == 0:
        return -1
    else:
        return count



#{
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):

    n = int(input())
    arr = list(map(int,input().strip().split()))
    K = int(input())
    res = Countpair(arr, n, K)
    print(res)



# } Driver Code Ends
