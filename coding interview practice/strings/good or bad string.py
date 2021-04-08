t = int(input())

while t>0:
    string = input()
    vowels = ['a','e','i','o','u']
    consecutive_vowel = 0
    consecutive_consonant = 0
    flag = 1

    for i in string:
        if i in vowels:
            consecutive_vowel += 1
            consecutive_consonant = 0
        elif i == '?':
            consecutive_vowel += 1
            consecutive_consonant += 1
        else:
            consecutive_consonant += 1
            consecutive_vowel = 0

        if consecutive_consonant > 3 or consecutive_vowel > 5:
            flag = 0
            break
    if flag == 0:
        print(0)
    else:
        print(1)
    t -= 1
