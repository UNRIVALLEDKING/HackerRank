# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

# Let's try to understand this with an example.

# You are given an immutable string, and you want to make changes to it.

# Example

# >>> string = "abracadabra"
# You can access an index by:

# >>> print string[5]
# a
# What if you would like to assign a value?

# >>> string[5] = 'k'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# How would you approach this?

# One solution is to convert the string to a list and then change the value.


# Sample Code

def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = "".join(string)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
