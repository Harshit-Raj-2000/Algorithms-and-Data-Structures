A1,A2,N = [int(x) for x in input().split(' ')]

# nth term =  a + (n-1)D = a1 + (n-1)(a2-a1)

print(A1 + (N-1)*(A2-A1))