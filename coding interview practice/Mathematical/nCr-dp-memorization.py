# def ncr(n,r):
#     if r>n:
#         return 0
#     if r==0 or r==n:
#         return 1
#     else:
#         return ncr(n-1,r-1)+ncr(n-1,r)

#above is the method of ncr without using factorial
#however init many subproblems are being calculated again and again
#so we need to use dynamic programming techniques

#using memorization technique of dp

def ncr(n,r,lookup):
    if lookup[n][r] == -1:
        if r>n:
            lookup[n][r] = 0
        elif r==0 or r==n:
            lookup[n][r] = 1
        else:
            lookup[n][r] = ncr(n-1,r-1,lookup) + ncr(n-1,r,lookup)
    return lookup[n][r]

n,r = [int(x) for x in input().strip().split()]

lookup = [[-1 for x in range(r+1)]for y in range(n+1)]
ncr(n,r,lookup)
print(lookup)

