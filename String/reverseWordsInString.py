def reverseWordsInString(string):
    #O(N) TS
    stack = []
    reversed_string = []
    for i in range(len(string) - 1, -1, -1):
        if string[i] != ' ':
            stack.append(i)
        elif string[i] == ' ':
            while stack:
                reversed_string.append(string[stack.pop()])
            reversed_string.append(' ')
    while stack:
        reversed_string.append(string[stack.pop()])
    return ''.join(reversed_string)

