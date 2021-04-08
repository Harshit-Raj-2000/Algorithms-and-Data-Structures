import math
def perfect_number(n):
    s = 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            s = s + i + n//i
    if n>1:
        s+=1
    return 1 if s == n else 0

N  = int(input().strip())
print(perfect_number(N))        