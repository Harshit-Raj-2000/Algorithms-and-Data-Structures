#using sieve of eratosthenes, finding sum
import math
def soe(N):
    table = [True for i in range(N+1)]
    sum = 0
    for i in range(2,int(math.sqrt(N))+1):
        if table[i] == True:
            for k in range(i*i,N+1,i):
                table[k] = False
    for i in range(2,N+1):
        if table[i] == True:
            sum+=i
    return sum

N = int(input().strip())

print(soe(N))

