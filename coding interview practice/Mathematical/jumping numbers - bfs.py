class queue:
    def __init__(self):
        self.lst = []
    def enqueue(self,el):
        self.lst.append(el)
    def dequeue(self):
        return self.lst.pop(0)
    def isEmpty(self):
        return (self.lst == [])


def bfs(x,num):
    q = queue()

    if num <= x:
        q.enqueue(num)

    while not(q.isEmpty()):
        p = q.dequeue()
        last_digit = p%10
        if last_digit == 0:
            m = p*10+1
            if m<=x:
                q.enqueue(m)
        elif last_digit == 9:
            m = p*10+8
            if m<=x:
                q.enqueue(m)
        else:
            m = p*10 + last_digit - 1
            n = p*10 + last_digit + 1
            if m<=x:
                q.enqueue(m)
            if n<=x:
                q.enqueue(n)
        ar.append(p)

T = int(input().strip())
for i in range(0,T):
    ar = [0]
    N = int(input().strip())
    for j in range(1,10):
        bfs(N,j)
    ar.sort()
    print(*ar,end=" ")
    



    