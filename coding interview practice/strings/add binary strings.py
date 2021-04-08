#User function Template for python3
class Solution:
	def addBinary(self, A, B):
	    A = A.lstrip('0')
	    B = B.lstrip('0')
	    max_len = max(len(A),len(B))
	    A = A.zfill(max_len)
	    B = B.zfill(max_len)
	    carry = 0

	    output = [0]*max_len

	    for i in range(max_len-1,-1,-1):
	        carry += int(A[i]) + int(B[i])
	        if carry %2 == 0:
	            output[i] = '0'
	        else:
	            output[i] = '1'
	        if carry >= 2:
	            carry = 1
	        else:
	            carry = 0
	    if carry == 0:
	        return "".join(output)
	    else:
	        return '1' + "".join(output)






#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		a,b = input().split(" ")
		ob = Solution()
		answer = ob.addBinary(a,b)

		print(answer)


# } Driver Code Ends
