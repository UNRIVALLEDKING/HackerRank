# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age.
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# Example
# Candles = [4,4,1,3]

# The maximum height candles are 4 units high. There are 2 of them, so return 2.


# Sample Code


#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    # Write your code here
    candles = sorted(candles)
    max = candles[-1]
    count = 0
    for i in candles:
        if max == i:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(raw_input().strip())

    candles = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
