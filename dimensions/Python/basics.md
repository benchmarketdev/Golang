### Variables
- Underscore `_` in interactive interpreter
```
>>> 5 * 5
25
>>> _
25
```

- `__mro__`    # method resolution order
- `__main__`
- `sys` argv

### Reverse a word

```
word = "apple"
word[:]
word[::-1]
```

### Lists and Dictionaries
> Looking up an item in a list is *O*(n). Sorting / caring about order

> Looking up an item in a dict is *O*(1). Repeated lookups

```
# to list
word_list = [elt.strip() for elt in open("words.txt", "r").readlines()]

# to dictionary
word_dict = dict((elt, 1) for elt in word_list)

# to set
word_set = set(word_list)

# filter
[elt for elt in word_list if "UU" in elt]
```

### Matplotlib library
https://matplotlib.org/tutorials/index.html
> apt-get install python3-matplotlib

### Python Debugging
- python -i <python_script.py>
- import pdb
- pdb.pm()

> Make Objects printable and debuggable
```
class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price
    
    def __repr__(self):     # representation method
        return 'Holding({!r},{!r},{!r},{!r})'.format(self.name, self.date, self.shares, self.price)
        
    def __str__(self):
        return ''
```

### Sorting and Grouping
```
# portfolio is a list of dictionary objects
portfolio.sort()
>>> unorderable types

def holding_name(holding):
    return holding['name']    
portfolio.sort(key=holding_name)

portfolio.sort(key=lambda holding: hodling['name'])

# lambda function
a = lambda x, y: x + y
a(2, 3)
>>> 5

min(portfolio, key=lambda holding: holding['price'])
max(portfolio, key=lambda holding: holding['price'])

import itertools
for name, items in itertools.groupby(portfolio, key=lambda hodling: holding['name']):
   print('NAME: ', name)
   for item in items:
       print('      ', it)

```

### Module Basics
```
# only run can be seen here,but the simple module is fully loaded
from simple import run

# equivalent statements are
improt simpe
run = simple.run()

# Imported Modules are cached..the second import does not load the module again
import simple
import sys
sys.modules['simple']
sys.path   # python path

del sys.modules['simple']

# gloabl variable `__name__`
if __name__ = '__name__':
    # do something
```

### Package

```
mkdir <package_name>  # and move your python files into it

touch __init__.py  # init file of a package

# within the package use package-relative import
import <package_name>.reader
from . import reader

# Lifting symbols from submodules
from .port import read_portfolio
from .reader import read_csv

```

### Classes and Objects
```
getattr(claz, 'name')       # equals claz.name
setattr(claz, 'name', 50)   # equals claz.name = 50

# class method
class Data(object):
    def __init__(self, year, month, day):
        self.year =year
        self.month = month
        self.day = day
        
    @classmethod                        # class method declaration
    def from_string(cls, s):            # cls is "Date"
        parts = s.split('-')
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))
        
    @classmethod
    def today(cls):
        import time
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_today)
        
```

### Inheritance
- Building an extensible library

```
class Parent(object):
    def __init__(self, value):
        ...
    def spam(self):
         print('Parent.spam', self.value)
        
class Child(Parent):                   # Parent as the paremeter
    def __init__(self, value, extra):
        self.extra = extra;
        super().__init__(value)        # Initialize parent
        
    def yow(self):
        print('Yow')
        
    def spam(self):
        print('Child.spam')
        super().spam()                  # invokes the original method
        
class Child2(Parent1, Parent2):         # inheritance from multiple parents
    def...
```

- Abstract Base Classes(ABC)
```
import sys
from abc import ABC, abstractmethod

@abstractmethod
def headings(self, headers):
    pass    
```

### Making a Custom Context Manager
Resource management:
    - open, use and close
    - acquire, use and releaes
```
class Manager(object):
    def __enter__(self):
        print("___enter__")
    def __exit__(self):
        print("__exit__")
        
improt manager
m = manager.Manager()
with m:
    print("I'm here!)
    
__enter__
I'm here!
__exit__
```
