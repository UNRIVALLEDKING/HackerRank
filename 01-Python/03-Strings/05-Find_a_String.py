# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.


# Concept

# Some string processing examples, such as these, might be useful.
# There are a couple of new concepts:
# In Python, the length of a string is found by the function len(s), where s is the string.
# To traverse through the length of a string, use a for loop:

# for i in range(0, len(s)):
#     print (s[i])
# A range function is used to loop over some length:

# range (0, 5)
# Here, the range loops over 0 to 4. 5 is excluded.


# Sample Code


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)


# Note

# a = ["a", "d", "e", "d", "v", "u", "t", "h"]
# print(a[5:])
# print(a[:5])
