# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


# Sample Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    arr = []
    arr.append(s[:2])
    arr.append(s[3:5])
    arr.append(s[6:8])
    arr.append(s[-2:])

    hr = arr[0]
    minute = arr[1]
    sec = arr[2]
    target = arr[3]
    military_time = []

    if target == "AM":
        if int(hr) > 12:
            military_time.append(str(int(hr)-12))
        elif int(hr) == 12:
            military_time.append(str(format(int(hr)-12, "02d")))
        else:
            military_time.append(str(hr))
    else:
        if int(hr) < 12:
            military_time.append(str(int(hr)+12))
        else:
            military_time.append(str(int(hr)))

    military_time.append(minute)
    military_time.append(sec)
    military_time = ":".join(military_time)
    return military_time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
