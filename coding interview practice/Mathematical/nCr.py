#nCr = fac(n)/(fac(n-r)*fac(r))
#we have to find the answer modulo (10**9+7)

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

n,r = [int(x) for x in input().strip().split()]

if r>n:
    print(0)
else:
    m = fac(n)//(fac(n-r)*fac(r))
    print(m%(10**9+7))

#in python the recursion limit is set to 10**4
#so to use recursive function on large nums like
#1000, we need to increase recursion limit to
#10**6, using the syntax-
# import sys
# sys.setrecursionlimit(10**6)