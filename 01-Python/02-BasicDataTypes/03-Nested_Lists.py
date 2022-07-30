# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Sample Code


# if __name__ == '__main__':
thislist = [('basd', 6.0), ('sadsa', 3.0), ('asdfj', 8.0)]
records = []

# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     thislist = [name, score]
#     print(thislist)
#     records.append(thislist)


# thislist.sort()
# thislist = sorted(thislist, key=lambda x: float(x))
thislist = sorted(thislist, key=lambda x: float(x[1]))
print(thislist)
