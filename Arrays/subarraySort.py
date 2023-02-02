#O(N)Time || O(1)Space
def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(array)):
        num =array[i]
        if isOutOfOrder(i,num,array):
            minOutOfOrder = min(minOutOfOrder , num)
            maxOutOfOrder = max(maxOutOfOrder , num)
    if maxOutOfOrder == float("-inf"):
        return[-1,-1]
    leftIdxOutOfOrder = 0
    while array[leftIdxOutOfOrder] <= minOutOfOrder:
        leftIdxOutOfOrder += 1
    rightIdxOutOfOrder = len(array) - 1
    while array[rightIdxOutOfOrder] >= maxOutOfOrder:
        rightIdxOutOfOrder -= 1
    return[leftIdxOutOfOrder , rightIdxOutOfOrder]
def isOutOfOrder(i,num,array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num < array[i - 1] or num > array[i + 1]