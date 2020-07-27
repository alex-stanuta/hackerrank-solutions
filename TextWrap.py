# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

import textwrap

def wrap(string, max_width):
    result = textwrap.wrap(string, max_width)
    text = ""
    for i in result:
        text = text + i + "\n"
    return text

if __name__ == '__main__':
    string, max_width = input(), int(input()) #The first line contains a string, S.The second line contains the width, w.
    result = wrap(string, max_width)
    print(result)