#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        alpha_array = [0]*26
        output = ""
        for i in A:
            alpha_array[ord(i)-97] = 1
        for i in B:
            if alpha_array[ord(i)-97] == 1 or alpha_array[ord(i)-97] == -1:
                alpha_array[ord(i)-97] = -1
            else:
                alpha_array[ord(i)-97] = 2
        for i  in range(26):
            if alpha_array[i] == 1 or alpha_array[i] == 2:
                output+=chr(i + 97)
        if output == "":
            return -1
        else:
            return output



#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends
