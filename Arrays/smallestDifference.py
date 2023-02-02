#O(nlog(n) + mlog(m)) Time || O(1)Space 
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    currentSmallest = 0
    smallest= float('inf')
    pairOfSmallest = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum =arrayTwo[idxTwo]
        if firstNum < secondNum:
            currentSmallest = secondNum - firstNum
            idxOne +=1
        elif  secondNum  < firstNum:
            currentSmallest =  firstNum - secondNum
            idxTwo +=1
        else:
            return[firstNum , secondNum]

        if smallest > currentSmallest:
            smallest = currentSmallest
            pairOfSmallest= [firstNum , secondNum]
    return pairOfSmallest
            
            