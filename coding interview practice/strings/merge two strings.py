t = int(input())

while t>0:
    string1, string2 = input().strip().split()
    output = ""
    len1 = len(string1)
    len2 = len(string2)
    i = j = 0
    while i < len1 and j < len2:
        output += string1[i] + string2[j]
        i += 1
        j += 1
    if len1 > len2:
        while i < len1:
            output += string1[i]
            i += 1
    elif len2 > len1:
        while j < len2:
            output += string2[j]
            j += 1
    print(output)
    t -= 1
        
