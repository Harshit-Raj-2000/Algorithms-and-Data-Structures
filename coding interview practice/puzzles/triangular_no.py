import math
M = int(input().strip())

#a triangylar no. can be represented a s a sum of first k natural numbers
#hence, for int k if k*(k+1)/2 = M, then M is a triangular number

a = (math.sqrt(1+(8*M)) - 1)/2

if int(a) == a:
    print(True)
else:
    print(False)
