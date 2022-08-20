# Sam's house has an apple tree and an orange tree that yield an abundance of fruit.
# Using the information given below, determine the number of apples and oranges that land on Sam's house.

# In the diagram below:

# The red region denotes the house, where s is the start point, and t is the endpoint.
# The apple tree is to the left of the house, and the orange tree is to its right.
# Assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.
# When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis.
# *A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right. *

# Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t] )?


# Function Description

# Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

# countApplesAndOranges has the following parameter(s):

# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.

# Sample Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appleFall = 0
    orangeFall = 0
    for i in apples:
        if a+i >= s and a+i <= t:
            appleFall += 1
    for i in oranges:
        if b + i <= t and b+i >= s:
            orangeFall += 1
    print(appleFall)
    print(orangeFall)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
