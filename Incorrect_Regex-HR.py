# You are given a string s.
# Your task is to find out whether s is a valid regex or not.

# Input Format
# The first line contains integer n, the number of test cases.
# The next n lines contains the string s.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def test_regex(string):
    for i in range (len(string)-1):
        if string[i] == "/":
            return False
        elif string[i] in ".\*+$^":
            if string[i] in "*+" and string[i+1] in "*+":
                return False
    return True

n = int(input())
for i in range (1,n+1):
    print(test_regex(input()))