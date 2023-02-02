def balancedBrackets(string):
    # O(N)TS.
    stack = []
    for i in string:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        elif i == ")" or i == "]" or i == "}":
            if len(stack) == 0:
                return False
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
 
    return len(stack) == 0