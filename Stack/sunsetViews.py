def sunsetViews(buildings, direction):
    #O(N)ts
    n = len(buildings)
    if n == 0:
        return []
    stack = []
    if direction == "EAST":
        directionViewEAST(stack ,buildings)
    else:
        dirctionviewWEST(stack , buildings)
    stack.sort()
    return stack

def directionViewEAST(stack ,buildings):
    n = len(buildings)
    for i in range(n- 1):
            for j in range(i + 1, n):
                if buildings[i] <= buildings[j]:
                    break
            else:
                stack.append(i)
    stack.append(n - 1)
def dirctionviewWEST(stack , buildings):
    n = len(buildings)
    for i in reversed(range(1, n)):
            for j in reversed(range(i)):
                if buildings[i] <= buildings[j]:
                    break
            else:
                stack.append(i)
    stack.append(0)
