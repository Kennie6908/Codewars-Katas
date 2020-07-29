#Complete the solution so that it splits the string into pairs of two characters. 
#If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

def solution(s):
    if len(s) == 0:
        return []
    else:
        count = 0
        placeholder = ''
        result = []
        for x in s:
            if count == 2:
                result.append(placeholder)
                count = 0
                placeholder = ''
            count += 1
            placeholder += x
        result.append(placeholder)
        if len(result[-1]) == 1:
            result[-1] += '_'
        return result