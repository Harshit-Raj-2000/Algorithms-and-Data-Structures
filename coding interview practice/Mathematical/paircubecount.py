import math
N = int(input().strip())
error = 0.0001
s = 0
for i in range(1,int(N**(1/3))+1):
    m = (N-(i**3))**(1/3)
    if math.ceil(m)-m<error:
        m = math.ceil(m)
    if int(m) == m:
        s+=1

print(s)

#above code fails for 1729
# (10,9)(9,10)(1,12),(12,1)
# 11 11.99998