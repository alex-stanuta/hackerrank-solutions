# Consider a list (list = []). You can perform the following commands:
# 1. insert i e : Insert integer at position .
# 2. print: Print the list.
# 3. remove e : Delete the first occurrence of integer .
# 4. append e : Insert integer at the end of the list.
# 5. sort: Sort the list.
# 6. pop : Pop the last element from the list.
# 7. reverse : Reverse the list.
# Initialize your list and read in the value of followed by lines of commands where each command will
# be of the types listed above. Iterate through each command in order and perform the corresponding
# operation on your list.
# Input Format
# The first line contains an integer, , denoting the number of commands.
# Each line of the subsequent lines contains one of the commands described above.

if __name__ == '__main__':
    operations = []
    a_list = []
    N = int(input())
    for _ in range(N):
        operations.append(list(map(str, input().split())))
    for operation in operations:
        if operation[0] == "insert":
            a_list.insert(int(operation[1]), int(operation[2]))
        elif operation[0] == "print":
            print (a_list)
        elif operation[0] == "remove":
            a_list.remove(int(operation[1]))
        elif operation[0] == "append":
            a_list.append(int(operation[1]))
        elif operation[0] == "sort":
            a_list.sort()
        elif operation[0] == "pop":
            a_list.pop()
        elif operation[0] == "reverse":
            a_list.reverse()