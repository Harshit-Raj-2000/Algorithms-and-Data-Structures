N =int(input().strip())
#last 2 digits of a ibonacci repeat after  300 digits
N = N%300

def fibonacci(n):
    table = [0,1]
    for i in range(2,n+1):
        table.append(table[-1]+table[-2])
    return table[n]

a = fibonacci(N)
# last_digit = a%10
# second_last = (a//10)%10

# print(second_last*10+last_digit)
print(a%100)