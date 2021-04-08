#version1

# def is_prime(num):
#     if num<=1:
#         return False
#     if num<=3:
#         return True
#     if num%2==0 or num%3==0:
#         return False

#     k = 5

#     while k*k<=num:
#         if num%k == 0 or num%(k+2) == 0:
#             return False
#         k = k+6
#     return True

# def LPF(num):
#     i = 1
#     while True:
#         if num//i == num/i:
#             if is_prime(num/i):
#                 return int(num/i)
#         i += 1

# num = int(input().strip())
# print(LPF(num))

#i don't know if this is the optimized solution.
#above code not optimised, getting time limit error.

#better sol'n and much simpler sol'n was to write the program to get the prime factors of a number and to prin the largest prime factor-

import math

def lpf(num):

    while num%2 == 0:
        num = num//2
        maxprime = 2

    for i in range(3,int(math.sqrt(num))+1,2):

        while num%i == 0:
            num = num//i
            maxprime = i

    if num>2:
        maxprime = num

    return maxprime

num = int(input().strip())
print(lpf(num))
