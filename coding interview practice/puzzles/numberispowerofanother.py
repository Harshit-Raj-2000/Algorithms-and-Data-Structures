x,y = [int(x) for x in input().strip().split()]

def isPower(x,y):
    if y==1:
        return True
    if x==1:
        return False
    while y%x==0:
        y=y//x
    if y==1:
        return True
    else:
        return False
    
print(isPower(x,y))

# alternate soln-
#if y is a power of x, log(y)/log(x) should be an int

