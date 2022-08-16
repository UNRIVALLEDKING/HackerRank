# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Sample Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    # Method 1
    arr.sort()
    minimun = 0
    maximum = 0
    for i in range(4):
        minimun += arr[i]
    for i in range(1, 5):
        maximum += arr[i]
    print(minimun, maximum)

    # Method 2 (Use any one, comment other to pass all text cases)

    total = sum(arr)
    minimun = total - max(arr)
    maximum = total - min(arr)
    print(minimun, maximum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
