# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.


# Sample Code

if __name__ == '__main__':
    N = int(input())

    thisList = []
    for i in range(N):
        order = input().split()
        cmd = order[0]
        if cmd == "insert":
            thisList.insert(int(order[1]), int(order[2]))
        elif cmd == "print":
            print(thisList)
        elif cmd == "remove":
            thisList.remove(int(order[1]))
        elif cmd == "append":
            thisList.append(int(order[1]))
        elif cmd == "sort":
            thisList.sort()
        elif cmd == "pop":
            thisList.pop(-1)
        elif cmd == "reverse":
            thisList.reverse()
