def sumElement(arr,n):
    return sum(arr)

if __name__ == '__main__':
    testCase=int(input())

    for _ in range(testCase):
        n=int(input())
        arr=[int(x) for x in input().split()]

        print(sumElement(arr,n))
