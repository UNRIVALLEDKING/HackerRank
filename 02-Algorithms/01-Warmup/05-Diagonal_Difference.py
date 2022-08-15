# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix arr is shown below:

# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal 1 + 5 + 9 = 15. The right to left diagonal 3 + 5 + 9 = 17. Their absolute difference is |15 - 17| = 2 .

# Function description

# Complete the DiagonalDifference function in the editor below.

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Return

# int: the absolute diagonal difference


# Sample Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# Sample Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    left = []
    right = []
    for i in range(len(arr)):
        new = arr[i]
        right.append(new[-i-1])
        left.append(new[i])
    sumLeft = 0
    sumRight = 0
    for i in left:
        sumLeft += i
    for i in right:
        sumRight += i
    dif = sumLeft-sumRight
    if dif < 0:
        dif = dif*-1
    else:
        dif = dif
    return dif


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
