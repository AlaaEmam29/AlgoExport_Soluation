def oneEdit(stringOne, stringTwo):
    #O(N + M)TS
    sLen , tLen = len(stringOne) , len(stringTwo)
    if abs(sLen - tLen) > 1:
        
        return False
    for i in range(min(sLen , tLen)):
        if stringOne[i] != stringTwo[i]:
            if sLen > tLen:
                return stringOne[i+1 : ] == stringTwo[i : ]
            elif tLen > sLen:
                return stringTwo[i + 1 : ] == stringOne[i : ]
            else:
                return stringOne[i+1:] == stringTwo[i+1:]
    return True

def oneEdit(stringOne, stringTwo):
    #O(N)T |O(1)Space
    startOne , startTwo = 0,0
    madeChange =False
    while startOne < len(stringOne) and startTwo < len(stringTwo):
        if stringOne[startOne] == stringTwo[startTwo]:
            startOne +=1
            startTwo +=1
        else:
            madeChange != madeChange
            if len(stringOne) > len(stringTwo):
                startOne +=1
            elif len(stringTwo) > len(stringOne):
                startTwo +=1
            else:
                startOne +=1
                startTwo +=1
    if startOne < len(stringOne) or startTwo < len(stringTwo):
        madeChange = True
    return True

                

                
