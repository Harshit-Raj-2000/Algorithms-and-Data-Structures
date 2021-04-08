class Solution:

	def findSubarray(self,a, n):
	    elements = []
    	sum = 0
        len_array = 0
        i = 0
        while i!= n:
            local_array = []
            local_sum = 0
            local_len = 0
            t=0
            while i!=n and a[i] >=0:
                local_array.append(a[i])
                local_sum += a[i]
                local_len += 1
                i += 1
                t = 1
            while i!=n and a[i] < 0:
                i += 1
            if t==1:
                if local_sum > sum :
                    elements = local_array
                    sum = local_sum
                    len_array = local_len
                elif local_sum ==sum and local_len>len_array:
                    elements = local_array
                    len_array = local_len
        if len(elements) == 0:
            return [-1]
        return elements







#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int, input().strip().split()))
	    ob = Solution()
	    ans=ob.findSubarray(a, n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends
