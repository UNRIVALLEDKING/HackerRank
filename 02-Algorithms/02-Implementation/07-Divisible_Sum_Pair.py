# Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.

# Example

# ar = [1, 3, 2, 6, 1, 2]
# k = 3

# Output

# 5

# Explanation

# Here are the 5 valid pairs when k = 3:
# (0, 2) → ar[0] + ar[2] = 1 + 2 = 3
# (0, 5) → ar[0] + ar[5] = 1 + 2 = 3
# (1, 3) → ar[1] + ar[3] = 3 + 6 = 9
# (2, 4) → ar[2] + ar[4] = 2 + 1 = 3
# (4, 5) → ar[4] + ar[5] = 1 + 2 = 3


# Sample Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(n):
        for j in range(1, n):
            if ar[i] < ar[j] and (ar[i] + ar[j]) % k == 0:
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
