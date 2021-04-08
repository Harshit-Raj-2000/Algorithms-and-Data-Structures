import sys

def minDist(arr, n, x, y):
    ans = sys.maxsize
    recent_x = -1
    recent_y = -1
    for i in range(n):
        if arr[i] == x:
            recent_x = i
            if recent_y != -1:
                ans = min(ans,abs(recent_x-recent_y))
        elif arr[i] == y:
            recent_y = i
            if recent_x != -1:
                ans = min(ans,abs(recent_y-recent_x))
    if ans == sys.maxsize:
        return -1
    else:
        return ans

#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(minDist(arr, n, x, y))



# } Driver Code Ends
