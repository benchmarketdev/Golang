# exception.py

import csv

def portfolio_cost(filename, errors='warn'):
    '''
    Computes total shares*price for a CSV file
    '''
    
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")
    
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:         # Exception for catching all errors
                if erros == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Reason:', err)
                elif errors = 'raise':
                    raise           # Reraise the last exception
                else:
                    pass
                continue            # Skips to the next row
            
            total += row[2] * row[3]
        return total

total = portfolio_cost('data/portfolio.csv', errors='silent')
print('Total cost:', total)


fh = None
try:
    fh = open(filename, 'w', encoding="utf-8")
    fh.write(html)
except EnvironmentError as err:
    print("Error: ", err)
else:
    print("Saved skeleton: ", filename)
finally:
    if fh is not None:
        fh.close()
    
