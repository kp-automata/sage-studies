#!/usr/bin/env sage -python
"""Source: https://github.com/nadialafreniere/SD130.5/blob/main/Intro_to_Sage_ETS_problems.ipynb

Problem 1 in Combinatorics using mathematical databases
Defintions: path -> a sequence of y coordinates subject to n number of up actions and n number of down actions
mountain -> a path of y coordinates (with x strictly increasing by 1) that stays in the positive x,y quadrant for the duration of the path and lands on the x-axis

Given n from 1 to 8, count all mountains in all possible paths. Create a sequence of these counts.
Analyze this sequence using the online encylopedia of integer sequences

Answer: [1, 2, 5, 14, 42, 132, 429]
oeis ID A000108
comment 3: Consider all the binomial(2n,n) paths on squared paper that (i) start at (0, 0), (ii) end at (2n, 0) and (iii) at each step, either make a (+1,+1) step or a (+1,-1) s
tep. Then the number of such paths that never go below the x-axis (Dyck paths) is C(n). [Chung-Feller]

"""
from sage.all import *

def create_rules(n: int):
    rule = [1] * n + [-1] * n
    permutations = Permutations(rule)
    return permutations

def create_paths(rules):
    paths = []
    y_n = 0
    for rule in rules:
        path = []
        path.append(y_n)
        for action in rule:
            y_next = path[-1] + action
            path.append(y_next)
        paths.append(path)
    return paths

def check_mountain_state(path) -> bool:
    if path[-1] != 0:
        return False
    for point in path:
        if point < 0:
            return False
    return True

def find_mountains(paths):
    mountains = [path for path in paths if check_mountain_state(path)]
    return mountains

def solve():
    sequence = []
    for n in range(1, 8):
        all_paths = create_paths(create_rules(n))
        mountains = find_mountains(all_paths)
        sequence.append(len(mountains))
    return sequence

def find_oeis(sequence):
    oeis_sequence = oeis(sequence)
    print(oeis_sequence[0])
    print(oeis_sequence[0].comments()[3])

if __name__ == "__main__":
    sequence = solve()
    print(sequence)
    print(find_oeis(sequence))
