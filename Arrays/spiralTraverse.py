def spiralTraverse(array):
    #O(N)TS
    res = []
    startR , endRow = 0 ,len(array) - 1
    startC , endCol = 0 , len(array[0]) - 1
    while startR <= endRow and startC <= endCol:
        for col in range(startC , endCol +1):
            res.append(array[startR][col])
        for row in range(startR + 1 , endRow+1):
            res.append(array[row][endCol])
        for col in reversed(range(startC,endCol)):
            if startR == endRow:
                break
            res.append(array[endRow][col])
        for row in reversed(range(startR+1 , endRow)):
            if startC == endCol:
                break
            res.append(array[row][startC])
        startR +=1
        startC +=1
        endRow -=1
        endCol -=1
    return res