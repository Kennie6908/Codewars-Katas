# Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?

# If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".

def balance(left, right):
    leftarray = list(left)
    rightarray = list(right)
    leftscore = 0
    rightscore = 0
    for leftitem in leftarray:
        if leftitem == "!":
            leftscore += 2
        if leftitem == "?":
            leftscore += 3
    for rightitem in rightarray:
        if rightitem == "!":
            rightscore += 2
        if rightitem == "?":
            rightscore += 3

    if leftscore == rightscore:
        return "Balance"
    elif leftscore > rightscore:
        return "Left"
    else:
        return "Right"
