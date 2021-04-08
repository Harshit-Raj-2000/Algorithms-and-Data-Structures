N,M = [int(x) for x in input().strip().split(' ')]

a = N//M

num1 = M*a
num2 = M*(a+1)

if abs(N-num1) < abs(num2-N):
    print(num1)
elif abs(N-num1)>abs(num2-N):
    print(num2)
else:
    if abs(num1)>abs(num2):
        print(num1)
    else:
        print(num2)