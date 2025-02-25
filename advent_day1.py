# Advent of Code Day 1
import os
import sys
import numpy
import math

def main():
    
    left_col = []
    right_col = []
    with open("input.txt", "r") as f:
        for line in f:
            n1, n2 = line.strip().split()
            left_col.append(int(n1))
            right_col.append(int(n2))
    
    left_col.sort()
    right_col.sort()
    sumnum = 0
    
    for a, b in zip(left_col, right_col):
        sumnum += (abs(a-b))
    print(sumnum)
    
if __name__ == "__main__":
    main()