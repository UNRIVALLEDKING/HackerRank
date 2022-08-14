# Given an integer, n, print the following values for each integer i from 1 to n:

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Function Description

# Complete the print_formatted function in the editor below.

# print_formatted has the following parameters:

# int number: the maximum value to print
# Prints

# The four values must be printed on a single line in the order specified above for each i from 1 to number.
# Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.


# Sample Code


def print_formatted(number):
    # your code goes here
    length = len(bin(number)[2:])

    for i in range(1, number+1):
        print(str(i).rjust(length, " "), oct(i)[2:].rjust(length, " "), hex(
            i)[2:].upper().rjust(length, " "), bin(i)[2:].rjust(length, " "))

    # for i in range(1, number + 1):
    #     f = ""
    #     for c in "doXb":
    #         if f:
    #             f += " "
    #         f += "{:>" + str(length) + c + "}"
    #     print(f.format(i, i, i, i))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
