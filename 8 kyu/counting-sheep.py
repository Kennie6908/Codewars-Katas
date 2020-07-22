## Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    a = 0
    for x in sheep:
        if x == True:
            a+=1
    return a