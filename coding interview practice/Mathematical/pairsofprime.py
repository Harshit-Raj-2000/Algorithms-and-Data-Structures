import math
def soe(n):
    table = [True for i in range(n+1)]
    prime = []
    for i in range(2,int(math.sqrt(n))+1):
        if table[i] == True:
            for k in range(i*i,n+1,i):
                table[k] = False
    for i in range(2,n+1):
        if table[i] == True:
            prime.append(i)
    return prime

def pair(n,prime_list):
    p = len(prime_list)
    for i in range(0,p):
        for j in range(0,p):
            if prime_list[i]*prime_list[j] <=n:
                print(f"{prime_list[i]} {prime_list[j]}",end=" ")
            else:
                break

a = int(input().strip())

pair(a,soe(a//2))