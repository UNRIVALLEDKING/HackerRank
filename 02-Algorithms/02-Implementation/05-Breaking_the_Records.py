# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
# She tabulates the number of times she breaks her season record for most points and least points in a game.
# Points scored in the first game establish her record for the season, and she begins counting from there.

# Example

# scores = [12,24,10,24]


# Scores are in the same order as the games played. She tabulates her results as follows:

#                                      Count
#     Game  Score  Minimum  Maximum   Min Max
#      0      12     12       12       0   0
#      1      24     12       24       0   1
#      2      10     10       24       1   1
#      3      24     10       24       1   1
# Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

# Function Description

# Complete the breakingRecords function in the editor below.

# breakingRecords has the following parameter(s):

# int scores[n]: points scored per game

# Returns

# int[2]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking least points records.


# Sample Code

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here
    minimun = scores[0]
    maximum = scores[0]
    maxcount = 0
    mincount = 0
    for i in range(1, len(scores)):
        if scores[i] > maximum:
            maximum = scores[i]
            maxcount += 1
        elif scores[i] < minimun:
            minimun = scores[i]
            mincount += 1
    return [maxcount, mincount]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
