import math
N = int(input().strip())

s = math.sqrt(N)

if int(s) == s:
    print(int(s-1))
else:
    print(int(s))