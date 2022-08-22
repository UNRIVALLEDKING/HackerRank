# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# 1. The elements of the first array are all factors of the integer being considered
# 2. The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.


# Function Description

# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

# getTotalX has the following parameter(s):

# int a[n]: an array of integers
# int b[m]: an array of integers


# Returns

# int: the number of integers that are between the sets


# Sample Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    # count = []
    # final = []
    # for i in range(max(a), min(b)):
    #     for j in range(0, len(a)):
    #         if i % a[j] != 0:
    #             break
    #         else:
    #             count.append(i)
    # for k in count:
    #     for m in range(0, len(b)):
    #         if b[m] % k != 0:
    #             break
    #         else:
    #             final.append(k)
    # return len(set(final))
    ans = 0
    for i in range(1, 101):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
