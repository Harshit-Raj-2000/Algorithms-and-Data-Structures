def saveIronman (s) :
    s = s.lower()
    alpha_array = [0]*256
    odd = 0
    for i in s:
        if i.isalpha() or i.isdigit():
            alpha_array[ord(i)] += 1
    for each in alpha_array:
        if each & 1:
            odd += 1
        if odd>1:
            return False
    return True



#{
#  Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    s = input()
    ans = saveIronman(s)
    if(ans == True):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends
