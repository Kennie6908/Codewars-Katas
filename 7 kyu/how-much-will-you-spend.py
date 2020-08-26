# How much will you spend?
# Given a dictionary of items and their costs and an array specifying the items bought, calculate the total cost of the items plus a given tax.

# If item doesn't exist in the given cost values, the item is ignored.

# Output should be rounded to two decimal places.

def get_total(costs, items, tax):
    quantity = 0
    for item in items:
        if item in costs:
            quantity += costs[item]

    quantity = quantity + (quantity * tax)
    formatted = "{:.2f}".format(quantity)
    formatted = float(formatted)
    return formatted
