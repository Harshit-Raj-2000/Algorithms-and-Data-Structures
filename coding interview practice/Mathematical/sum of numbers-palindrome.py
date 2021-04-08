N = int(input().strip())

sum = 0
while N>0:
    digit = N%10
    N = N//10
    sum += digit


a = str(sum)
n = len(a)
m = 1

for i in range(0,n//2):
    if a[i] != a[n-1-i]:
        m = 0
        break

if m == 1:
    print(1)
else:
    print(0)
        

