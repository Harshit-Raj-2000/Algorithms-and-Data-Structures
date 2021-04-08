# recursive ncr function without using factorial

# def ncr(n,r):
#     if r>n:
#         return 0
#     if r==n or r==0:
#         return 1
#     return ncr(n-1,r-1)+ncr(n-1,r)

# n,r = [int(x) for x in input().strip().split()]

# print(ncr(n,r))

#this method has many subproblems which are being calculated again and again.
#we need to use dp. Here we are using tabulation method of dp.

# def ncr(n,r):
#     if r>n:
#         return 0
#     lookup = [[0 for i in range(r+1)] for j in range(n+1)]

#     for i in range(1,n+1):
#         for j in range(min(i,r)+1):
#             if j == 0 or j == i:
#                 lookup[i][j] = 1
#             else:
#                 lookup[i][j] = lookup[i-1][j-1] + lookup[i-1][j]
#     return lookup[n][r]

# n,r = [int(x) for x in input().strip().split()]
# print(ncr(n,r))

#the above is the tabulation method of dp, where we move bottom up, to create  all the elements of the table
#but there can be another method to decrease the space complexity.let's try that below.

def ncr(n,r):
    lookup = [0 for i in range(r+1)]
    lookup[0] = 1
    #because for any value of n nC0 =1

    for i in range(1,n+1):
        j = min(i,r)
        while j>0:
            lookup[j] = lookup[j] + lookup[j-1]
            j = j-1
    return lookup[r]

n,r = [int(x) for x in input().strip().split()]
print(ncr(n,r))

