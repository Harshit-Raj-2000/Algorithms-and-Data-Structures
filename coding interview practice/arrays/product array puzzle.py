#User function Template for python3

def productExceptSelf(arr, n):
    product_on_left = [1]*n
    temp = 1
    for i in range(1,n):
        product_on_left[i] = product_on_left[i-1]*arr[i-1]
    for i in range(n-1,-1,-1):
        product_on_left[i] *= temp
        temp *= arr[i]
    return product_on_left


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends
