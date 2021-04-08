t = int(input())

while t>0:
    string = input()
    odd = 0
    alpha_array = [0]*26
    for i in string:
        alpha_array[ord(i)-97] += 1
    for each in alpha_array:
        if each %2 != 0:
            odd += 1
    if odd > 1:
        print("No")
    else:
        print("Yes")
    t -= 1
