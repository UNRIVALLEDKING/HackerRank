# You are choreographing a circus show with various animals.
# For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show.
# If it is possible, return YES, otherwise return NO.

# Function Description

# Complete the function kangaroo in the editor below.

# kangaroo has the following parameter(s):

# int x1, int v1: starting position and jump distance for kangaroo 1
# int x2, int v2: starting position and jump distance for kangaroo 2
# Returns

# string: either YES or NO

# Constraints

# 0<=x1<x2<=10000
# 1<=v1<=10000
# 1<=v2<=10000

# Sample Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def kangaroo(x1, v1, x2, v2):
    # Write your code here
    target = "NO"
    for i in range(10001):
        if x1+(i*v1) == x2+(i*v2):
            target = "YES"
    return target


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
