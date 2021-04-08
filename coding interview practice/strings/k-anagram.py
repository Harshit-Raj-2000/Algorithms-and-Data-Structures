# Your task is to complete this function
# Function should return 1/0 or True/False
def areKAnagrams(str1, str2, k):
    if len(str1) != len(str2):
        return False
    alpha_array = [0]*26
    sum = 0
    n = len(str1)
    for i in range(n):
        alpha_array[ord(str1[i])-97] += 1
        alpha_array[ord(str2[i])-97] -= 1
    for i in range(26):
        if alpha_array[i] > 0:
            sum += alpha_array[i]
        if sum > k:
            return False
    return True


#{
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        k = int(input())
        if areKAnagrams(arr[0], arr[1], k):
            print(1)
        else:
            print(0)
# Contributed By: Harshit sidhwa
# } Driver Code Ends
