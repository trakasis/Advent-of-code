# Advent of Code Day 1
import os
import sys
import numpy
import math

def main():
    data = numpy.loadtxt("input.txt")
    first_row = data[:,0]
    second_row = data[:,1]
    print(abs(first_row[0] - second_row[0]))
    
if __name__ == "__main__":
    main()