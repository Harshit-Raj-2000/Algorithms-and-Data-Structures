import math
N,M = [int(x) for x in input().strip().split()]

error = 0.00000001
a = (M**(1/N))
if math.ceil(a)-a<error:
    a = math.ceil(a)
    print(a)
else:
    print(-1)