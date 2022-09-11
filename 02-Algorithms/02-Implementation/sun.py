s = [2, 2, 1, 3, 2]
d = 4
m = 2

count = 0

for i in range(len(s)-1):
    if s[i] + s[i+1]== d:
        count += 1

print(count)
