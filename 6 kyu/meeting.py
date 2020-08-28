# John has invited some friends. His list is:
# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

# Could you make a program that makes this string uppercase gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

# So the result of function meeting(s) will be: "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

def meeting(s):
    returned = ""
    firstnames = []
    lastnames = []
    s = s.upper()
    st = s.split(";")
    for item in st:
        list = item.split(":")
        firstnames.append(list[1])
        lastnames.append(list[0])

    sortedlist = sorted(zip(firstnames, lastnames ))
    print(sortedlist)
    for name in sortedlist:
        returned += "(" + name[0] + ", " + name[1] + ")"

    return returned
