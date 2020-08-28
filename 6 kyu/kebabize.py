# Modify the kebabize function so that it converts a camel case string into a kebab case.

# kebabize('camelsHaveThreeHumps') // camels-have-three-humps
# kebabize('camelsHave3Humps') // camels-have-humps

def kebabize(string):
    returnedword = ""
    for x in string:
        if (x.isalpha()):
            if (x.isupper()):
                returnedword += '-'
            returnedword += x

    returnedword = returnedword.lower()
    if (len(returnedword) > 0):
        if (returnedword[0] == "-"):
            returnedword = returnedword[1:]
        if (returnedword[len(returnedword)-1] == "-"):
            returnedword = returnedword[:len(returnedword)-1]

    return returnedword
