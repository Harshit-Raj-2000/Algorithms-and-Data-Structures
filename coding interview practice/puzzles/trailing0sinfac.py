# import sys

# def fac(n):
#     lookup_table = [1]
#     for i in range(1,n+1):
#         lookup_table.append(i*lookup_table[i-1])
#     a = lookup_table[n]
#     del lookup_table
#     return a


# s = 0
# n = 9
# a = fac(n)
# while a%10==0:
#     a=a//10
#     s+=1
# print(s)

#alternatemehod
#since any number num of 5's > num of 2's as prime factors
#num of trailing 0's = num of 5's in n!

def num(n):
    count = 0
    i = 5
    while n/i >=1:
        count += n//i
        i*=5
    print(count)

num(100)