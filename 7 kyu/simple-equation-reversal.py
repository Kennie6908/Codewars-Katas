# Given a mathematical equation that has *,+,-,/, reverse it as follows:

# solve("100*b/y") = "y/b*100"
# solve("a+b-c/d*30") = "30*d/c-b+a"

def solve(eq):
    s = eq.replace('+',' + ').replace('-',' - ').replace('/',' / ').replace('*',' * ')
    s = s.split()
    s = s[::-1]
    return ''.join(s)
