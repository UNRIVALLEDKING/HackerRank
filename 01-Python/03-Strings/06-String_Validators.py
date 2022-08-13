# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
# Like --> print 'ab123'.isalnum()
# True
# Like --> print 'ab123#'.isalnum()
# False


# str.isalpha()
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).
# Like --> print 'abcD'.isalpha()
# True
# Like --> print 'abcd1'.isalpha()
# False


# str.isdigit()
# This method checks if all the characters of a string are digits (0-9).
# Like --> print '1234'.isdigit()
# True
# Like --> print '123edsd'.isdigit()
# False


# str.islower()
# This method checks if all the characters of a string are lowercase characters (a-z).
# Like --> print 'abcd123#'.islower()
# True
# Like --> print 'Abcd123#'.islower()
# False


# str.isupper()
# This method checks if all the characters of a string are uppercase characters (A-Z).
# Like --> print 'ABCD123#'.isupper()
# True
# Like --> print 'Abcd123#'.isupper()
# False


# Task
# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Sample Code


if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
