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
