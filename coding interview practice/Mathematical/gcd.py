A,B = [int(x) for x in input().strip().split(' ')]
dividend = max(A,B) #48
divisor = min(A,B)  #18


while divisor != 0:
    m = dividend%divisor #12
    dividend = divisor  #18
    divisor = m       #12

print(dividend)
    