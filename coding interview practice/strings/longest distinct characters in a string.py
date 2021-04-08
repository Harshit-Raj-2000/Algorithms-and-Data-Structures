#User function Template for python3

#space complexity is O(1), can't create a hash table
# can create a hash table as hash table has fixed size of 26
#time complexity isO(|s|), can iterate through the string in O(|s|)

class Solution:

    def longestSubstrDitinctChars(self, S):
        alpha_dict = [0]*26
        max_length = 1
        i = j = 0
        n = len(S)
        while j < n:
            if alpha_dict[ord(S[j])-97] == 1:
                max_length = max(max_length,j-i)
                while S[i] != S[j]:
                    alpha_dict[ord(S[i])-97] = 0
                    i += 1
                i += 1
                j += 1
            else:
                alpha_dict[ord(S[j])-97] = 1
                j += 1
        max_length = max(max_length,j-i)
        return max_length


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDitinctChars(S)

        print(ans)

# } Driver Code Ends
