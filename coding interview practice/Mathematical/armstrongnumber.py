N = int(input().strip())

num = N
sum = 0
while num>0:
    digit = num%10
    num = num//10
    sum += digit**3

if sum == N:
    print('YES')
else:
    print('NO')

    