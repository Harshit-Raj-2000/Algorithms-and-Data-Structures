#Another method of log(n) time also possible.


#User function Template for python3
class Solution:
	def kthCharacter(self, m, n, k):
		bin_rep = bin(m)[2:]
		for i in range(n):
		    output = []
		    for i in bin_rep:
		        if i == '1':
		            output.append('10')
		        else:
		            output.append('01')
		    bin_rep = ('').join(output)
        return bin_rep[k-1]


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n,k = input().split()
		m,n,k = int(m),int(n),int(k)

		ob = Solution()
		answer = ob.kthCharacter(m, n, k)
		print(answer)

# } Driver Code Ends
