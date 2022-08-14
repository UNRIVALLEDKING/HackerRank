# In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

# Function Description

# Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

# aVeryBigSum has the following parameter(s):

# int ar[n]: an array of integers .
# Return

# long: the sum of all array elements


# Note

# The range of the 32-bit integer is (-2)**31 to (2**31 -1) or[-2147483648, 2147483647] .
# When we add several integer values, the resulting sum might exceed the above range. You might need to use long int C/C++/Java to store such sums.


# Sample Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#


def aVeryBigSum(ar):
    # Write your code here
    sum = 0
    for i in range(ar_count):
        sum += int(ar[i])
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
