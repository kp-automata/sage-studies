#!/usr/bin/env sage -python
"""
1, 4, 9, 16, 25 ...first few perfect squares

Among the first 759 thousand square numbers,
what is the sum of all the odd squares?

Note: Didn't need to use sage at all.
"""
from sage.all import *
numbers = [n*n for n in range(1, 759001) if  n % 2 != 0]
total = sum(numbers)
print(total)
