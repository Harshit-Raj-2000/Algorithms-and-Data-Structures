N = int(input().strip())

for i in range(0,N):
    m = 1
    s = str(i)
    for j in range(0,len(s)-1):
        if abs(int(s[j]) - int(s[j+1])) != 1:
            m = 0
            break
    if m == 1:
        print(i,end=" ")
