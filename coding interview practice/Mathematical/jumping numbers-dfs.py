class stack:
    def __init__(self):
        self.lst = []
    def push(self,el):
        self.lst.append(el)
    def pop(self):
        return self.lst.pop()
    def isEmpty(self):
        return self.lst == []

def dfs(x,num):
    s = stack()
    s.push(num)

    while not(s.isEmpty()):
        p = s.pop()
        if p<=x:
            ar.append(p)
            last_digit = p%10
            if last_digit == 0:
                m = p*10 + 1
                s.push(m)
            elif last_digit == 9:
                m = p*10 + 8
                s.push(m)
            else:
                m = p*10 + last_digit - 1
                n = p*10 + last_digit + 1
                s.push(m)
                s.push(n)

T = int(input().strip())
for i in range(0,T):
    N = int(input().strip())
    ar = [0]
    for j in range(1,10):
        dfs(N,j)
    ar.sort()
    print(*ar,end=" ")

            
        