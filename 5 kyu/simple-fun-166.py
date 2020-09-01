# kata description at https://www.codewars.com/kata/58b38256e51f1c2af0000081

def best_match(goals1, goals2):
    num = goals1[0] - goals2[0]
    index = 0
    for i in range(len(goals1)):
        if goals1[i] - goals2[i] < num:
            num = goals1[i] - goals2[i]
            index = i
        if goals1[i] - goals2[i] == num:
            if goals2[i] > goals2[index]:
                index = i
    return index
