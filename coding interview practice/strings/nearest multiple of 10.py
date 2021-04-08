
class Solution:
    def roundToNearest (self, N) :
        num = int(N)
        small = (num//10)*10
        large = small+10
        if large-num < num - small:
            return large
        else:
            return small


#{
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):

    s = input()
    ob = Solution()
    res = ob.roundToNearest(s)
    print(res)


# } Driver Code Ends
