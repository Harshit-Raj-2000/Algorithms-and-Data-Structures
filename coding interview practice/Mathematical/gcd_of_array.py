def gcd(a,b):
    if min(a,b) == 0:
        return max(a,b)
    else:
        return gcd(max(a,b)%min(a,b),min(a,b))

def gcd_of_array(ar):
    if len(ar) == 1:
        return ar[0]
    g = gcd(ar[0],ar[1])
    for i in range(2,len(ar)):
        g = gcd(g,ar[i])
    return g

ar = []
N = int(input().strip())
for i in range(0,N):
    ar.append(int(input()))

print(gcd_of_array(ar))
