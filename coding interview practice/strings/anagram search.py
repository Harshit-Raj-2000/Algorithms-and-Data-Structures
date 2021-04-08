# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1,str2):
    str1 = str1.strip()
    str2 = str2.strip()
    alpha_array = [0]*26
    delete_char = 0
    for i in str1:
            alpha_array[ord(i)-97] += 1
    for i in str2:
        alpha_array[ord(i)-97] -= 1
    for i in alpha_array:
        if(i):
            delete_char += abs(i)
    return delete_char

#{
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends
