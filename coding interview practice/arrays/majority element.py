


class Solution:
    def majorityElement(self, A, N):
        dict_element = {}
        for each in A:
            if each in dict_element:
                dict_element[each] +=1
            else:
                dict_element[each] = 1
        for x,y in dict_element.items():
            if y> N//2:
                return x
        return -1


#{
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):

            N=int(input())

            A=[int(x) for x in input().strip().split()]


            obj = Solution()
            print(obj.majorityElement(A,N))

            T-=1


if __name__ == "__main__":
    main()
