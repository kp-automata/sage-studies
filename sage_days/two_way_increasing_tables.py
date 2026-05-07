#!/usr/bin/env sage -python
"""Source:  https://github.com/nadialafreniere/SD130.5/blob/main/Intro_to_Sage_ETS_problems.ipynb

Problem 3 in Combinatorics using mathematical databases

Definitions:
    partition lambda of n -> a weakly decreasing sequence of positive integers whose sum is n
    diagram -> collection of boxes s.t. lambda_1 is on top, lambda_2 is below and so on...
    table -> is a filling of the diagram
    two-way increasing -> fillings increasing along the rows (left to right) and increasing down the columns (up to down)

Count the number of two-way increasing tables of shape (n, n) for n
from 1 to 8

Answer:
    We get a sequence of Catalan numbers and see that a_n is the number of SYT of shape(n, n)

Note:
    Unsure of result of why shape (n, n - 1) yields the same count. Need to think on it. 

"""
from sage.all import *

def count_tableaux():
    # SYT are two-way increasing by defintion, increasing tableaux not strict enough
    return[StandardTableaux([n, n]).cardinality() for n in range(1, 9)]

def oeis_lookup(sequence):
    oeis_sequence = oeis(sequence)
    # A000108: Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!).
    print(oeis_sequence[0])
    # a(n) is also the number of standard Young tableaux of shape (n,n). - _Thotsaporn Thanatipanonda_, Feb 25 2012
    print(oeis_sequence[0].comments()[42])

def count_tableaux_variant():
    return[StandardTableaux([n, n - 1]).cardinality() for n in range(1, 9)]

def compare(sequence):
    print(f"shape of (n, n) {sequence}")
    print(f"shape of (n, n - 1) {count_tableaux_variant()}")

if __name__ == "__main__":
    sequence = count_tableaux()
    oeis_lookup(sequence)
    compare(sequence)
