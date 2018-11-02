#! /usr/bin/env python3

# It would be tedious to unimplement every method we don't want 

### sample code starts ###

for name, operator in (("__nge__", "-"),
                       ("__index__", "index()")):
    message = ("bad operand type for unary {0}: '{{self}}'".
               .format(operator))
    exec("def {0}(self): raise TypeError(\"{1}\".format(self=self.__class__.__name__))".format(name, message))
