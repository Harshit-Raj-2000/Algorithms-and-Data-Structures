class Solution:
    # User function Template for python3

    def reverseWords(self,S):
        words_list = S.split('.')
        words_list.reverse()
        output = ('.').join(words_list)
        return output


#{
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends
