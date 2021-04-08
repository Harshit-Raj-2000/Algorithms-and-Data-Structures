
# def overlapping(x1,y1,x2,y2,a1,b1,a2,b2):

#     if (x1<a1 and a1<x2) and(y2<b1 and b1<y1):
#         print(1)
#         return True
#     if (x1<a2 and a2<x2) and(y2<b1 and b1<y1):
#         print(2)
#         return True
#     if (x1<a1 and a1<x2) and(y2<b2 and b2<y1):
#         print(3)
#         return True
#     if (x1<a2 and a2<x2) and(y2<b2 and b2<y1):
#         return True
#     if (b1==y1 and b2==y2) and((x1<a1 and a1<x2) or (x1<a2 and a2<x1)):
#         return True
#     if (a1==x1 and a2==x2) and((y1<b1 and b1<y2) or (y1<b2 and b2<y1)):
#         return True
#     if (x1==a1 and y1==b1 and x2==a2 and y2==b2):
#         return True
#     return False

# print(overlapping(0,10,10,0,5,5,15,20))

#it can be asumed that the rectangles are parallel to the cordinate axis
#the above is too heavy a code, we we were checking the conditions, when 2 rectangles overlap
#we should have instead checked for condition if 2 rectangles don't overlap.

def overlap(x1,y1,x2,y2,a1,b1,a2,b2):
    if (b2>y1) or (y2>b1):
        return False
    if (x2<a1) or (a2<x1):
        return False
    return True

print(overlap(0,2,1,1,-1,-3,0,2))