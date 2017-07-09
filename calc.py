
import sys
import operator

stack = []

operators = {'+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: x/y}
            
while True:
    i = input()
    if i in operators:
        y,x = stack.pop(), stack.pop()
        z = operators[i](x,y)
    else:
        z = float(i)
    stack.append(z)
    print("\n".join([str(x) for x in stack]), flush=True)