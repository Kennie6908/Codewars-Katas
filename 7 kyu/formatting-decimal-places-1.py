#Each floating-point number should be formatted that only the first two decimal places are returned. 
#You don't need to check whether the input is a valid number because only valid numbers are used in the tests.

#Don't round the numbers! Just cut them after two decimal places!

def two_decimal_places(number):
    a = int(number * 100)
    return a / 100.0