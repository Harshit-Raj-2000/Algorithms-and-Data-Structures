import math

def isPrime(n):
    if n<=1:
        return 0
    if n<=3:
        return 1
    if n%2==0 or n%3==0:
        return 0
    
    for k in range(5,int(math.sqrt(n))+1,6):
        if n%k==0 or n%(k+2)==0:
            return 0
    return 1

n = int(input().strip())
print(isPrime(n))