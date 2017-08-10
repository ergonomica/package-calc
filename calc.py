
import sys
import operator

from prompt_toolkit.shortcuts import clear as raw_clear

CALCULATOR_WELCOME_MESSAGE = "Ergonomica Calculator v0.0.1-alpha.1"

try:
    input = raw_input
except NameError:
    pass

stack = []

operators = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y,
             '^': lambda x, y: x ** y,
             '%': lambda x, y: x % y}

def calc(argc):
    """Calc: a simple RPN calculator for Ergonomica.
    
    Usage:
        calc
    """            
    
    raw_clear()
    print(CALCULATOR_WELCOME_MESSAGE)
    
    while True:
    
        i = input()
        if i in operators:
            try:
                y,x = stack.pop(), stack.pop()
                z = operators[i](x,y)
            except IndexError:
                print("End of stack!")
        else:
            try:
                z = float(i)
            except ValueError:
                print("Invalid number")
                continue
        stack.append(z)
    
        raw_clear()
        print(CALCULATOR_WELCOME_MESSAGE)
    
        print("\n".join([str(x) for x in stack]))
        
exports = {"calc": calc}
