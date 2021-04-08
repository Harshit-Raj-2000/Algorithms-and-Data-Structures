#the nth power of the matrix [[1,1],[1,0]] will have[0][0]term as n+1th fibonacci
#to calculate nth fibonacci, we need to calculate n-1th power of[[1,1],[1,0]]

def multiply(F,N):
    w = F[0][0]*N[0][0] + F[0][1]*N[1][0]
    x = F[0][0]*N[0][1] + F[0][1]*N[1][1]
    y = F[1][0]*N[0][0] + F[1][1]*N[1][0]
    z = F[1][0]*N[0][1] + F[1][1]*N[1][1]

    F[0][0] = w
    F[0][1] = x
    F[1][0] = y
    F[1][1] = z

def power(F,n):
    M = [[1,1],[1,0]]
    if n==0 or n==1:
        return
    power(F,n//2)
    multiply(F,F)
    if n%2!=0:
        multiply(F,M)

def fib(n):
    if n==0:
        return 0
    F = [[1,1],[1,0]]
    power(F,n-1)
    return F[0][0]

N = int(input().strip())
print(fib(N))
    