n = int(input().strip())

def find_even(n):
    t = [0,2]
    for i in range(2,n+1):
        t.append((4*t[-1])+t[-2])
    return t[n]

print(find_even(n))