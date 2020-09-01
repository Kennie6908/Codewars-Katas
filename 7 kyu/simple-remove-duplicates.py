# In this Kata, you will remove the left-most duplicates from a list of integers and return the result.

def solve(arr):
    returnedarray = []
    for item in arr[::-1]:
        if item not in returnedarray:
            returnedarray.insert(0, item)
    return returnedarray
