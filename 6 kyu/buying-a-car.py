# Let us begin with an example:

# A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000.
# He wants to keep his old car until he can buy the secondhand one.

# He thinks he can save $1000 each month but the prices of his old car and of the new one decrease of 1.5 percent per month.
# Furthermore this percent of loss increases of 0.5 percent at the end of every two months. Our man finds it difficult to make all these calculations.

# Can you help him? How many months will it take him to save up enough money to buy the car he wants, and how much money will he have left over?

def iq_test(numbers):
    evens = odds = 0
    index = oddindex = evenindex = 1
    numberssplit = numbers.split(" ")
    for number in numberssplit:
        if int(number) % 2 == 0:
            evens += 1
            evenindex = index
        else:
            odds += 1
            oddindex = index
        index+=1

    if (odds > evens):
        return evenindex
    else:
        return oddindex
