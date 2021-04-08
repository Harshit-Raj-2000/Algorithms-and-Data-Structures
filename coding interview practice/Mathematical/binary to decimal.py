a = input()
n = len(a)
decimal = 0

for i in range(0,n):
    if a[i] == '1':
        decimal += 2**(n-1-i)

print(decimal)
