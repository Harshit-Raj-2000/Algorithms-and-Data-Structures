#this is sakamoto's algorithm.
#i have kind of memorised it

def day(d,m,y):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    month = [0,3,2,5,0,3,5,1,4,6,2,4]
    y -= m<3
    b = (y + y//4 + y//400 - y//100 + month[m-1] + d)%7
    return days[b]

d,m,y = [int(x) for x in input().strip().split()]
print(day(d,m,y))