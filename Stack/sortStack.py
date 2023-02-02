def sortStack(stack):
    #O(N^2)time O(n)space
    ans = []
    while stack: 
        temp = stack.pop()
        while ans and ans[-1] > temp:
            stack.append(ans.pop()) 
        ans.append(temp) 
    return ans 
