# Kata can be found here https://www.codewars.com/kata/5d23d89906f92a00267bb83d

def get_order(order):
    menu = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    fixed = ''
    for item in menu:
        fixed += (item.capitalize() + ' ') * order.count(item)
    return fixed[:-1]
