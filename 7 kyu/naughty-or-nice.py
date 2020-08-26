# In this kata, you will write a function that receives an array of string and returns a string that is either 'naughty' or 'nice'.
# Strings that start with the letters b, f, or k are naughty. Strings that start with the letters g, s, or n are nice.
# Other strings are neither naughty nor nice.

# If there is an equal amount of bad and good actions, return 'naughty'

def what_list_am_i_on(actions):
    naughty = 0
    nice = 0
    for action in actions:
        if (action[0] == 'b' or action[0] == 'f' or action[0] == 'k'):
            naughty += 1
        elif (action[0] == 'g' or action[0] == 's' or action[0] == 'n'):
            nice += 1

    if nice > naughty:
        return "nice"
    elif naughty > nice:
        return "naughty"
    else:
        return "naughty"
