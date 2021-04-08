#we need to remember that A*B = LCM(A,B)*GCD(A*B)

A,B = [int(x) for x in input().strip().split(' ')]

def GCD(A,B):
    if min(A,B) == 0:
        return max(A,B)
    else:
        A1 = max(A,B)%min(A,B)
        return GCD(A1,min(A,B))

def LCM(A,B):
    return int(A*B/GCD(A,B))

print(GCD(A,B),LCM(A,B))