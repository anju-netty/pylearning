#!/bin/python

import math
import os
import random
import re
import sys

# Complete the superDigit function below.

def sum_of_digits(p):
    sum_of_p = 0

    while p != 0:

        sum_of_p = sum_of_p + p%10
        p = int(p/10)

    return sum_of_p

def calculate_digit(p):

    s = sum_of_digits(p)
    
    if int(s/10) == 0: 
        return s
 
    return calculate_digit(s)

# superDigit(9,2) -> calculate_digit(99) -> calculate_digit(18) <-- 9

def superDigit(n, k):

    result = calculate_digit(n) * k

    while int(result /10) != 0:
        result = calculate_digit(result)

    return result
if __name__ == '__main__':
    

    n = 100

    k = 4

    result = superDigit(n, k)

    print(result)
