# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

# the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.

def up_array(arr):
    number = ""
    returned = []
    if len(arr) == 0:
        return None
    for num in arr:
        if num < 0 or num > 9:
            return None
        number += str(num)
    number = int(number) + 1
    listofints = list(str(number))
    for ints in listofints:
        returned.append(int(ints))

    return returned
