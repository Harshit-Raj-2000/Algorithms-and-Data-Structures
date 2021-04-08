class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,arr, n):
        index = {}
        for i in range(n):
            if arr[i] in index:
                index[arr[i]].append(i)
            else:
                index[arr[i]] = [i]
        arr.sort()
        max_diff = 0
        temp = n
        for i in range(n):
            if index[arr[i]][0]<temp:
                temp = index[arr[i]][0]
            max_diff = max(max_diff,index[arr[i]][-1]-temp)
        return max_diff



#{
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):

            n=int(input())

            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))


            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
