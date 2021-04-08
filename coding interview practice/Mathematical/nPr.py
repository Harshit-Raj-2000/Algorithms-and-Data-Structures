def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

T = int(input().strip())

for i in range(0,T):
    n,r = [int(x) for x in input().strip().split(' ')]
    m = fac(n)//fac(n-r)
    print(m)