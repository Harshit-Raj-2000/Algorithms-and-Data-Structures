num1,den1,num2,den2 = [int(x) for x in input().strip().split(' ')]

def gcd(x,y):
    if min(x,y) == 0:
        return max(x,y)
    else:
        return gcd(max(x,y)%min(x,y),min(x,y))

num = num1*den2 + num2*den1
den = den1*den2

a = gcd(num,den)
num = num//a
den = den//a

print(f"{num}/{den}")

