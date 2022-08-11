# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Sample Code


if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        thislist = [name, score]
        records.append(thislist)
records = sorted(records, key=lambda x: float(x[1]))

minlist = records[0]
minscore = minlist[1]
li = []
newlist = []
for i in records:
    if minscore in i:
        li.append(i)
    else:
        newlist.append(i)

secondGrade = newlist[0]
marks = secondGrade[1]
newlist = sorted(newlist)
for i in newlist:
    if marks in i:
        print(i[0])
