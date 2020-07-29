#Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

#Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. 
#In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 
#1666 uses each Roman symbol in descending order: MDCLXVI.

def solution(n):
      if (n - 1000 >= 0):
        return "M" + solution(n - 1000)  
      if (n - 900 >= 0):
        return "CM" + solution(n - 900)
      if (n - 500 >= 0):
        return "D" + solution(n - 500)
      if (n - 400 >= 0):
        return "CD" + solution(n - 400)
      if (n - 100 >= 0):
        return "C" + solution(n - 100)
      if (n - 90 >= 0):
        return "XC" + solution(n - 90)
      if (n - 50 >= 0):
        return "L" + solution(n - 50)
      if (n - 40 >= 0): 
        return "XL" +solution(n - 40)
      if (n - 10 >= 0):
        return "X" + solution(n - 10)
      if (n - 9 >= 0):
        return "IX" + solution(n - 9)
      if (n - 5 >= 0):
        return "V" + solution(n - 5)
      if (n - 4 >= 0):
        return "IV" + solution(n - 4)
      if (n - 1 >= 0):
        return "I" + solution(n - 1)
      return "";

