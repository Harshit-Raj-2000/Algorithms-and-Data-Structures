N = int(input().strip())

for i in range(N,0,-1):
    for j in range(N,0,-1):
        print(f'{j} '*i,end="")
    print('$',end="")
    