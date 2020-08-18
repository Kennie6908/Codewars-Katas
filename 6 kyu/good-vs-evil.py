# https://www.codewars.com/kata/52761ee4cffbc69732000738
# Description is too long. 

def goodVsEvil(good, evil):
    good_split = good.split(' ')
    evil_split = evil.split(' ')

    goodworth = 0
    evilworth = 0

    for counter, oldvalue in enumerate(good_split):
        value = int(oldvalue)
        if counter == 0:
            goodworth += (value * 1)
        elif counter == 1:
            goodworth += (value * 2)
        elif counter == 2:
            goodworth += (value * 3)
        elif counter == 3:
            goodworth += (value * 3)
        elif counter == 4:
            goodworth += (value * 4)
        elif counter == 5:
            goodworth += (value * 10)

    for counter, oldvalue in enumerate(evil_split):
        value = int(oldvalue)
        if counter == 0:
            evilworth += (value * 1)
        elif counter == 1:
            evilworth += (value * 2)
        elif counter == 2:
            evilworth += (value * 2)
        elif counter == 3:
            evilworth += (value * 2)
        elif counter == 4:
            evilworth += (value * 3)
        elif counter == 5:
            evilworth += (value * 5)
        elif counter == 6:
            evilworth += (value * 10)

    if goodworth > evilworth:
        return "Battle Result: Good triumphs over Evil"
    elif goodworth < evilworth:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
