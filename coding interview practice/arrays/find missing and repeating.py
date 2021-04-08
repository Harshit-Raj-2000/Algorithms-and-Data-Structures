#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n):
        big = n+1
        repeated = -1
        missing = -1
        for i in range(0,n):
            arr[arr[i]%big-1] += big
        for i in range(0,n):
            if arr[i]//big == 0:
                missing = i+1
            elif arr[i]//big > 1:
                repeated = i+1
            if repeated != -1 and missing != -1:
                break
        return [repeated,missing]




#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
