class Solution:
    def extractMaximum(self,S):
        max_digit = -1
        num = ""
        for i in S:
            if i.isdigit():
                num += i
            else:
                if num!="":
                    max_digit = max(int(num),max_digit)
                    num = ""
        if num!= "":
            max_digit = max(max_digit,int(num))
        return max_digit



#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        print(ob.extractMaximum(S))

# } Driver Code Ends
