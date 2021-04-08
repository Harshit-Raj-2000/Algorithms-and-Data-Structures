# M,N = [int(x) for x in input().strip().split()]

# a = min(M,N)
# sum = 0
# for i in range(1,a+1):
#      sum += ((1 + (M-i))*(1+(N-i)))

# print(sum)

#a better sol'n withpout using any loops is as follows-

#no. of squares in a m*m matrix is M^2 + (M-1)^2+....1
#no. of squares in a square matrix of order m is m(m+1)(2m+1)/6

#in a rectangular matrix, for each extra row,
# extra squares are  = 1+2+3+4..n where n is the order of square matrix, n<m
# so, for each extra row, no. of squares are n(n+1)/2 , n<m

# so, for (m-n) extra rows, extra squares are (m-n)(n)(n+1)/2

M,N = [int(x) for x in input().strip().split()]

a = min(M,N)
b = (a*(a+1)*(2*a+1)//6) + (max(M,N) -a)*((a)*(a+1))//2
print(b)