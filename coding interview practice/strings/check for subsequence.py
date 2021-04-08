class Solution:
    def isSubSequence(self, A, B):
        pointer = 0
        n = len(B)
        m = len(A)
        for i in range(n):
            if B[i] == A[pointer]:
                pointer += 1
            if pointer == m:
                return True
        return False


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A,B = input().split()
        ob = Solution()
        if ob.isSubSequence(A,B):
            print(1)
        else:
            print(0)

# } Driver Code Ends
