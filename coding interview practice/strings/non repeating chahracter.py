from collections import OrderedDict

class Solution:
    #User function Template for python3

    '''
    	Your task is to return the index of lefmost non-repeating
    	character or return
    	-1 if all characters occur more than once.

    	Function Arguments: s (given string)
    	Return Type: integer
    '''

    def nonrepeatingCharacter(self,s):
        alpha_dict = OrderedDict()
        for i in s:
            if i in alpha_dict:
                alpha_dict[i] += 1
            else:
                alpha_dict[i] = 1
        for i in alpha_dict:
            if alpha_dict[i] == 1:
                return i
        return '$'



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
        obj = Solution()
        ans=obj.nonrepeatingCharacter(s)
        if(ans!='$'):
            print(ans)
        else:
            print(-1)

# } Driver Code Ends
