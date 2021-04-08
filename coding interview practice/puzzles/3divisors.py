import math

def soe(n):
    table = [True for i in range(n+1)]
    s = 0
    for i in range(2,int(math.sqrt(n))+1):
        if table[i] == True:
            for k in range(i*i,n+1,i):
                table[k] = False
    for i in range(2,n+1):
        if table[i] == True:
            s+= 1
    return s

N = int(input().strip())
a = int(math.sqrt(N))
print(soe(a))

#The above code is not optimised to get the number of numbers less than N with exactly 3 divisors.
#The above code is correct only, but it is somehow giving large time
#in python, same logic works in cpp.