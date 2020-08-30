# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    returned = ""
    text = text.split(" ")
    for word in text:
        if word.isalpha():
            returned += (word[1:] + word[0] + 'ay ')
        else:
            returned += word + ' '
    returned = returned[:-1]
    return returned
