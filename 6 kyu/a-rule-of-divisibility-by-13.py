# When you divide the successive powers of 10 by 13 you get the following remainders of the integer divisions:

# 1, 10, 9, 12, 3, 4.

# Then the whole pattern repeats.

# Hence the following method: Multiply the right most digit of the number with the left most number in the sequence shown above,
# the second right most digit to the second left most digit of the number in the sequence.
# The cycle goes on and you sum all these products.
# Repeat this process until the sequence of sums is stationary.

def thirt(n):
    tempremainder = 0
    listofdivisors = [1,10,9,12,3,4]
    divisornum = 0
    notreversed = str(n)
    reversednum = str(n)[::-1]
    while True:
        for num in reversednum:
            tempremainder += (int(num) * listofdivisors[divisornum])
            divisornum += 1

            if divisornum > 5:
                divisornum = 0

        if str(tempremainder) == notreversed:
            return tempremainder

        else:
            reversednum = str(tempremainder)[::-1]
            notreversed = str(tempremainder)
            tempremainder = 0
            divisornum = 0
