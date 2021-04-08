def duplicates(arr, n):
    result = []
    flag = False
    for i in range(n):
        arr[arr[i]%n] += n
    for i in range(n):
        if arr[i]/n >=2:
            result.append(i)
            flag =True
    if flag == True:
        return result
    else:
        return[-1]




#{
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
