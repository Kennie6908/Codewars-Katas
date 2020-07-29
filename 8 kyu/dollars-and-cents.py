#The company you work for has just been awarded a contract to build a payment gateway.
#In order to help move things along, you have volunteered to create a function that will take a float and return the amount formatting in dollars and cents.

#39.99 becomes $39.99

def format_money(amount):
    a = '$' + format(amount, '.2f')
    return a