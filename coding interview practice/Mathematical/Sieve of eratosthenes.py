import math
def sieve(n):
    truth_table = [True for i in range(n+1)]
    prime = []

    for p in range(2,int(math.sqrt(n))+1):
        if truth_table[p] == True:
            for i in range(p*p,n+1,p):
                truth_table[i] = False
    for i in range(2,n+1):
        if truth_table[i] == True:
            prime.append(i)

    return prime

print(sieve(35))
        






    




