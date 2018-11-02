# function.py

import csv

def portfolio_cost(filename):
    '''
    Computes total shares*price for a CSV file
    '''
    
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            row[2] = int(row[2])
            row[3] = float(row[3])
            total += row[2] * row[3]
        return total

total = portfolio_cost('data/portfolio.csv')
print('Total cost:', total)

def function_name(a, b, *, key=value):
    """
    Use `*` as a parameter in its own right, to signify that there is no positional arguments after `*`
    """
    pass

def fucntion_name(*, key=value):
    """
    By making `*` as the first parameter we can pervent any positional arguments from being used.
    """
    passs

    
s = lambda x: "" if x == 1 else "s"
print("{0} file{1} processed".format(count, s(count)))
