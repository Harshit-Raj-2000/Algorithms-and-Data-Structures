class Solution:

    # arr[] : the input array
    # N : size of the array arr[]

    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        elements_dict = set()
        subsequence_length = 0
        for each in arr:
            elements_dict.add(each)
        for each in arr:
            if each - 1 in elements_dict:
                continue
            k = each
            while k in elements_dict:
                k = k+1
            subsequence_length = max(subsequence_length,k-each)
        return subsequence_length

#{
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends
