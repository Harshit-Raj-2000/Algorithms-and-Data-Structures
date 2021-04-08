#User function Template for python3

# return the smallest window in S with all the characters of P
# if no such window exists, return "-1"
class Solution:
    def smallestWindow(self, s, p):
        len_string = len(s)
        len_pat = len(p)
        if len_pat > len_string:
            return -1
        pat_hash = [0]*256
        str_hash = [0]*256
        start,start_index,min_len = 0,-1,float('inf')
        count = 0

        for i in p:
            pat_hash[ord(i)] += 1

        for i in range(len_string):
            str_hash[ord(s[i])] += 1

            if str_hash[ord(s[i])] <= pat_hash[ord(s[i])]:
                count += 1
            if count == len_pat:
                while (pat_hash[ord(s[start])] == 0) or \
                (str_hash[ord(s[start])]>pat_hash[ord(s[start])]):
                    if str_hash[ord(s[start])]>pat_hash[ord(s[start])]:
                        str_hash[ord(s[start])] -= 1
                    start += 1
                length = i - start + 1
                if min_len > length:
                    min_len = length
                    start_index = start
        if start_index == -1:
            return -1
        else:
            return s[start_index:start_index + min_len]



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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends
