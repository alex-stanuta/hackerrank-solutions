# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.
# Input Format
# The first line of input contains the original string. The next line contains the substring.
# Ex: "CDC" in "ABCDCDC" returns 2.

def count_substring(string, sub_string):
    l = []
    for i in range (len(string)):
        if string[i] == sub_string[0]:
            l.append(i)
    count = 0
    for i in l:
        if i + len (sub_string) > len (string):
            pass
        elif sub_string == string[i:i+len(sub_string)]:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)