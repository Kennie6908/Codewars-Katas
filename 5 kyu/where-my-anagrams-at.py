# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none.

def anagrams(word, words):
    returnedarray = []
    word = sorted(word)
    for givenword in words:
        if sorted(givenword) == word:
            returnedarray.append(givenword)

    return returnedarray
