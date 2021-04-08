#User function Template for python3
class Solution:
    def ReverseSort(self, s):
        output = ""
        alpha_array =[0]*26
        for i in s:
            alpha_array[ord(i)-97] += 1
        for i in range(25,-1,-1):
            for k in range(0,alpha_array[i]):
                output += chr(97+i)
        return output

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.ReverseSort(s))
# } Driver Code Ends
