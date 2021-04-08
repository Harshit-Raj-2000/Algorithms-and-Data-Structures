x1,y1,x2,y2,x3,y3,x4,y4 = [int(x) for x in input().strip().split()]

def dist_sq(x1,y1,x2,y2):
    return (x2-x1)**2 + (y2-y1)**2

d2 = dist_sq(x1,y1,x2,y2)
d3 = dist_sq(x1,y1,x3,y3)
d4 = dist_sq(x1,y1,x4,y4)

if d2==0 or d3==0 or d4==0:
    print('No')
elif d2==d3 and d4==2*d2 and dist_sq(x2,y2,x3,y3)==2*dist_sq(x2,y2,x4,y4):
    print('Yes')
elif d2==d4 and d3==2*d2 and dist_sq(x2,y2,x4,y4)==2*dist_sq(x2,y2,x3,y3):
    print('Yes')
elif d3==d4 and d2==2*d3 and dist_sq(x4,y4,x3,y3)==2*dist_sq(x2,y2,x4,y4):
    print('Yes')
else:
    print('No')
