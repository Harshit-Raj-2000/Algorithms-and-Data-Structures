class Solution:
    def trappingWater(self, arr,n):
        water = 0
        left = [-1]*n
        right = [-1]*n
        for i in range(1,n):
            left[i] = max(left[i-1],arr[i-1])
        for j in range(n-2,-1,-1):
            right[j] = max(right[j+1],arr[j+1])
        for i in range(1,n-1):
            if (arr[i] < left[i]) and (arr[i] < right[i]):
                water += min(left[i],right[i]) - arr[i]
        return water


#{
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):

            n=int(input())

            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))


            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends
