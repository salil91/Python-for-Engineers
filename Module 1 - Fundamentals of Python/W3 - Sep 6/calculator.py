# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:31:41 2022

@author: salil.bavdekar
"""

def add_numbers(x, y):
     
    return x+y


def multiply_numbers(x, y):
    
    return x*y


def square_number(x):
    
    return x**2


pi = 3.14159
e = 2.71828

def main():
    # print(__name__)
    
    added = add_numbers(pi, e)
    multiplied  = multiply_numbers(pi, e)
    squared = square_number(pi)
    
    print(f"The sum of pi and e is {added}")
    print(f"The product of pi and e is {multiplied}")
    print(f"The square of pi is {squared}")
    
    
if __name__ == "__main__":
    main()

