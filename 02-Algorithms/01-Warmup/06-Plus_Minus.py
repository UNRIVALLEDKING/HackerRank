# # Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# # Print the decimal value of each fraction on a new line with 6 places after the decimal.

# # Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10**-4 are acceptable.


# Function Description

# Complete the plusMinus function in the editor below.

# plusMinus has the following parameter(s):

# int arr[n]: an array of integers
# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal.
# The function should not return a value.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    positive = []
    negative = []
    zero = []
    for i in arr:
        if i < 0:
            negative.append(i)
        elif i > 0:
            positive.append(i)
        else:
            zero.append(i)
    print(format(len(positive)/len(arr), "6f"))
    print(format(len(negative)/len(arr), "6f"))
    print(format(len(zero)/len(arr), "6f"))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
