# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others.
# Bob observed that one number usually differs from the others in evenness.
# Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

# Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    numOfMonths = 0
    while (startPriceOld + (numOfMonths * savingperMonth) < startPriceNew):
        startPriceOld = startPriceOld * ((100 - percentLossByMonth)/100)
        startPriceNew = startPriceNew * ((100 - percentLossByMonth)/100)
        if numOfMonths % 2 == 0:
            percentLossByMonth = percentLossByMonth + 0.5
        numOfMonths += 1

    return [numOfMonths, int(round((startPriceOld + (numOfMonths * savingperMonth) - startPriceNew)))]
