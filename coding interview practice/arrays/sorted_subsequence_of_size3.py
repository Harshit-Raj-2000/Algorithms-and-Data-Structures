def find3number(A, n):
    result = []
    min = 0
    small = [0]*n
    small[0] = -1
    for i in range(1,n):
        if A[i] <= A[min]:
            min = i
            small[i] = -1
        else:
            small[i] = min
    max = n-1
    large = [0]*n
    large[n-1] = -1
    for i in range(n-2,-1,-1):
        if A[i] >= A[max]:
            max = i
            large[i] = -1
        else:
            large[i] = max
    for i in range(n):
        if large[i] != -1 and small[i] != -1:
            result.append(A[small[i]])
            result.append(A[i])
            result.append(A[large[i]])
            break
    return result
