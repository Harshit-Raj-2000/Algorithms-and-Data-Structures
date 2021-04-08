# Your task is to complete all
# three functions

# if the element is found in the list
# function  must return true or else
# return false
def searchEle(a, x):
    if x in a:
        return True
    else:
        return False

# fucntion must return true if
# insertion is successful or else
# return false
def insertEle(a, y, yi):
    a.insert(yi,y)
    return True


# fucntion must return true if
# deletion is successful or else
# return false
def deleteEle(a, z):
    try:
        i = list.index(z)
        del(a[i])
        return True
    except:
        return True
