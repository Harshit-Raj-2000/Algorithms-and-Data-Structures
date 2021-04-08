# Given a string, find the first repeated character in it.
# We need to find the character that occurs more than once and whose index of
# second occurrence is smallest.

#sample test case
#Input - geeksforgeeks
#Output - 'e'
#Input - gekmke
#Output - 'k' -- because index of the point where element is repeated is less

#one pointer in the beginning, one at the end,but the end pointer should not move
#if the element at the beginning is not repeating, one way is to make a hash table,
# and check for the values


def find_repeating(string):
    alpha_set = set()
    for each in string:
        if each in alpha_set:
            return each
        else:
            alpha_set.add(each)
    return -1

string = 'mjabkkmj'
print(find_repeating(string))
