#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxSumPath(self,arr1, arr2, m, n):
        i = 0
        j = 0
        result = 0
        sum1 = 0
        sum2 = 0
        while i<m and j<n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                result += max(sum1,sum2)
                sum1 = sum2 = 0
                while i<m and j <n and arr1[i] == arr2[j]:
                    result += arr1[i]
                    i += 1
                    j += 1
        for k in range(j,n):
            sum2 += arr2[k]
        for k in range(i,m):
            sum1 += arr1[k]
        result += max(sum1,sum2)
        return result







#{
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        m,n = list(map(int, input().strip().split()))
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        print(Solution().maxSumPath(arr1, arr2, m, n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
